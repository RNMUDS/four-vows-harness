"""Scoring: per-condition accuracy, bootstrap CIs, McNemar paired tests."""

import json
from collections import defaultdict

import numpy as np
from scipy import stats


def load_results(path) -> list[dict]:
    with open(path, encoding="utf-8") as fh:
        return [json.loads(line) for line in fh]


def by_condition(records: list[dict]) -> dict:
    """Group records by condition, keyed by item_id for pairing."""
    grouped = defaultdict(dict)
    for rec in records:
        grouped[rec["condition"]][rec["item_id"]] = rec
    return grouped


def accuracy_ci(records: list[dict], n_boot: int = 10_000,
                seed: int = 0) -> dict:
    """Accuracy with a percentile bootstrap 95% CI. Unparsed answers count
    as incorrect (conservative)."""
    correct = np.array([r["correct"] for r in records], dtype=float)
    if len(correct) == 0:
        return {"n": 0, "acc": None, "ci": (None, None)}
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(correct), size=(n_boot, len(correct)))
    boots = correct[idx].mean(axis=1)
    return {
        "n": len(correct),
        "acc": float(correct.mean()),
        "ci": (float(np.percentile(boots, 2.5)),
               float(np.percentile(boots, 97.5))),
        "parse_rate": float(np.mean([r["parsed"] for r in records])),
        "refusal_rate": float(np.mean([r.get("refused", False)
                                       for r in records])),
    }


def mcnemar(cond_a: dict, cond_b: dict) -> dict:
    """Exact McNemar test on paired items (a correct/b wrong vs a wrong/b
    correct). Returns discordant counts and two-sided p-value."""
    shared = sorted(set(cond_a) & set(cond_b))
    a_only = sum(1 for k in shared
                 if cond_a[k]["correct"] and not cond_b[k]["correct"])
    b_only = sum(1 for k in shared
                 if cond_b[k]["correct"] and not cond_a[k]["correct"])
    n_disc = a_only + b_only
    if n_disc == 0:
        return {"n_pairs": len(shared), "a_only": 0, "b_only": 0, "p": 1.0}
    p = stats.binomtest(a_only, n_disc, 0.5).pvalue
    return {"n_pairs": len(shared), "a_only": a_only, "b_only": b_only,
            "p": float(p)}


def summarize(path, reference: str = "vows_loop") -> str:
    """Print per-condition accuracy and paired tests against `reference`."""
    grouped = by_condition(load_results(path))
    lines = []
    for cond, items in sorted(grouped.items()):
        s = accuracy_ci(list(items.values()))
        lines.append(
            f"{cond:16s} n={s['n']:4d} acc={s['acc']:.3f} "
            f"CI=[{s['ci'][0]:.3f}, {s['ci'][1]:.3f}] "
            f"parse={s['parse_rate']:.3f} refuse={s['refusal_rate']:.3f}")
    if reference in grouped:
        for cond in sorted(grouped):
            if cond == reference:
                continue
            m = mcnemar(grouped[reference], grouped[cond])
            lines.append(
                f"McNemar {reference} vs {cond}: "
                f"+{m['a_only']}/-{m['b_only']} p={m['p']:.4f}")
    return "\n".join(lines)
