"""Cross-run analysis: master tables, strictness shift, SCRUPLES humans."""

import json
from collections import defaultdict
from pathlib import Path

from .parsing import is_refusal
from .scoring import accuracy_ci, by_condition, mcnemar

CONDITION_ORDER = ["baseline", "generic_ethics", "virtue_ethics",
                   "vows_static", "vows_loop"]


def load_all(results_dirs: list[str]) -> list[dict]:
    """Load every result record from the given directories, tagging each
    with the dataset inferred from its filename."""
    records = []
    for d in results_dirs:
        for path in sorted(Path(d).glob("*.jsonl")):
            if path.name.startswith("smoke"):
                continue
            dataset = _dataset_of(path.name)
            with open(path, encoding="utf-8") as fh:
                for line in fh:
                    rec = json.loads(line)
                    rec["dataset"] = dataset
                    # recompute with the current refusal patterns; stored
                    # flags may predate parser fixes
                    task = "choice" if rec["gold"] in ("A", "B") else "binary"
                    rec["refused"] = is_refusal(rec.get("raw"), task)
                    records.append(rec)
    return records


def _dataset_of(filename: str) -> str:
    for prefix in ("pilot", "cm_test", "cm_hard", "mc_low", "mc_high",
                   "scruples"):
        if filename.startswith(prefix):
            return "cm_test" if prefix == "pilot" else prefix
    return "unknown"


def dedupe(records: list[dict]) -> list[dict]:
    """Keep one record per (model, dataset, condition, item); later files
    win so re-runs supersede earlier partial data."""
    seen = {}
    for rec in records:
        seen[(rec["model"], rec["dataset"], rec["condition"],
              rec["item_id"])] = rec
    return list(seen.values())


def master_table(records: list[dict]) -> str:
    """Accuracy per model x dataset x condition, plus paired tests of each
    vows condition against baseline and generic_ethics."""
    cells = defaultdict(list)
    for rec in records:
        cells[(rec["model"], rec["dataset"], rec["condition"])].append(rec)
    lines = []
    combos = sorted({(m, d) for m, d, _ in cells})
    for model, dataset in combos:
        lines.append(f"\n## {model} x {dataset}")
        grouped = by_condition([r for (m, d, c), rs in cells.items()
                                if m == model and d == dataset for r in rs])
        for cond in CONDITION_ORDER:
            if cond not in grouped:
                continue
            s = accuracy_ci(list(grouped[cond].values()))
            lines.append(
                f"  {cond:16s} n={s['n']:4d} acc={s['acc']:.3f} "
                f"CI=[{s['ci'][0]:.3f},{s['ci'][1]:.3f}] "
                f"parse={s['parse_rate']:.3f} refuse={s['refusal_rate']:.3f}")
        for vows in ("vows_static", "vows_loop"):
            for ref in ("baseline", "generic_ethics"):
                if vows in grouped and ref in grouped:
                    m = mcnemar(grouped[vows], grouped[ref])
                    lines.append(
                        f"  McNemar {vows} vs {ref}: "
                        f"+{m['a_only']}/-{m['b_only']} p={m['p']:.4f}")
    return "\n".join(lines)


def strictness_table(records: list[dict]) -> str:
    """For binary (WRONG/ACCEPTABLE) datasets: rate of judging acceptable
    actions as wrong (over-strict) vs wrong actions as acceptable."""
    cells = defaultdict(list)
    for rec in records:
        if rec["gold"] in ("WRONG", "ACCEPTABLE"):
            cells[(rec["model"], rec["dataset"], rec["condition"])].append(rec)
    lines = ["model | dataset | condition | over_strict | over_lenient"]
    for (model, dataset, cond) in sorted(cells):
        rs = cells[(model, dataset, cond)]
        acc_items = [r for r in rs if r["gold"] == "ACCEPTABLE"]
        wrong_items = [r for r in rs if r["gold"] == "WRONG"]
        strict = (sum(1 for r in acc_items if r["pred"] == "WRONG")
                  / max(1, len(acc_items)))
        lenient = (sum(1 for r in wrong_items if r["pred"] == "ACCEPTABLE")
                   / max(1, len(wrong_items)))
        lines.append(f"{model} | {dataset} | {cond:16s} | "
                     f"{strict:.3f} | {lenient:.3f}")
    return "\n".join(lines)


def scruples_human_alignment(records: list[dict]) -> str:
    """SCRUPLES-only: mean human vote share of the chosen action, split by
    controversial vs consensus items. 1.0 = always with the unanimous
    majority; 0.5 = coin-flip relative to human distribution."""
    cells = defaultdict(list)
    for rec in records:
        if rec["dataset"] == "scruples" and rec.get("meta") and rec["parsed"]:
            cells[(rec["model"], rec["condition"])].append(rec)
    lines = ["model | condition | vote_share_all | consensus | controversial"]
    for (model, cond) in sorted(cells):
        rs = cells[(model, cond)]

        def share(r):
            votes = (r["meta"]["votes_a"], r["meta"]["votes_b"])
            chosen = votes[0] if r["pred"] == "A" else votes[1]
            return chosen / (votes[0] + votes[1])

        def mean_share(subset):
            return (sum(share(r) for r in subset) / len(subset)
                    if subset else float("nan"))

        cons = [r for r in rs if not r["meta"]["controversial"]]
        cont = [r for r in rs if r["meta"]["controversial"]]
        lines.append(f"{model} | {cond:16s} | {mean_share(rs):.3f} | "
                     f"{mean_share(cons):.3f} | {mean_share(cont):.3f}")
    return "\n".join(lines)
