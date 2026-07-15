#!/usr/bin/env python3
"""Generate the two manuscript figures from per-item results.

Fig 1: over-strictness by condition, 4 models, ETHICS commonsense (test).
Fig 2: SCRUPLES accuracy by condition with 95% CI, 3 models.
Colors: Okabe-Ito colorblind-safe (blue = static-type, vermillion =
loop-type, dark gray = baseline).
"""

import json
import math
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "paper" / "figures"

BLUE, VERM, GRAY = "#0072B2", "#D55E00", "#444444"

LABELS = {
    "baseline": "baseline", "generic_ethics": "generic ethics",
    "virtue_ethics": "virtue ethics", "vows_static": "vows (static)",
    "vows_loop": "vows loop", "reflect_loop": "reflect loop",
    "virtue_loop": "virtue loop",
}


def wilson(k: int, n: int) -> tuple:
    if n == 0:
        return (0.0, 0.0)
    z = 1.96
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h


def load(path: Path) -> dict:
    by = defaultdict(list)
    for line in open(path, encoding="utf-8"):
        r = json.loads(line)
        by[r["condition"]].append(r)
    return by


def dotpanel(ax, rows, xlabel, baseline_x):
    ys = range(len(rows))
    ax.axvline(baseline_x, color=GRAY, lw=0.8, ls="--", zorder=1)
    for y, (label, val, lo, hi, color) in zip(ys, rows):
        ax.plot([lo, hi], [y, y], color=color, lw=1.8, zorder=2,
                solid_capstyle="round")
        ax.plot(val, y, "o", color=color, ms=6.5, zorder=3)
    ax.set_yticks(list(ys))
    ax.set_yticklabels([r[0] for r in rows], fontsize=9.5)
    ax.invert_yaxis()
    ax.set_xlabel(xlabel, fontsize=9.5)
    ax.tick_params(axis="x", labelsize=8.5)
    ax.grid(axis="x", color="#dddddd", lw=0.5)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)


def color_of(cond: str) -> str:
    if cond == "baseline":
        return GRAY
    return VERM if cond.endswith("loop") else BLUE


def fig1() -> None:
    models = [("qwen3.6:latest", "pilot_qwen3.6_latest.jsonl", "Qwen 3.6 35B"),
              ("gemma3:27b", "pilot_gemma3_27b.jsonl", "Gemma 3 27B"),
              ("gpt-oss:20b", "cm_test_gpt-oss_20b.jsonl", "GPT-OSS 20B"),
              ("llama3.3:70b", "remote/pilot_llama3.3_70b.jsonl",
               "Llama 3.3 70B")]
    conds = ["baseline", "generic_ethics", "virtue_ethics", "vows_static",
             "vows_loop"]
    fig, axes = plt.subplots(1, 4, figsize=(9.6, 2.6), sharex=True)
    for ax, (_, fname, title) in zip(axes, models):
        by = load(ROOT / "results" / fname)
        rows, base = [], None
        for c in conds:
            rs = [r for r in by.get(c, []) if r["gold"] == "ACCEPTABLE"]
            if not rs:
                continue
            k = sum(1 for r in rs if r["pred"] == "WRONG")
            lo, hi = wilson(k, len(rs))
            val = k / len(rs)
            if c == "baseline":
                base = val
            rows.append((LABELS[c], val, lo, hi, color_of(c)))
        dotpanel(ax, rows, "over-strictness", base)
        ax.set_title(title, fontsize=10.5)
        if ax is not axes[0]:
            ax.set_yticklabels([])
    fig.tight_layout()
    fig.savefig(OUT / "fig1_strictness.pdf", bbox_inches="tight")
    plt.close(fig)


def fig2() -> None:
    models = [("scruples_qwen3.6_latest.jsonl", "Qwen 3.6 35B"),
              ("scruples_gemma3_27b.jsonl", "Gemma 3 27B"),
              ("scruples_gpt-oss_20b.jsonl", "GPT-OSS 20B")]
    conds = ["baseline", "generic_ethics", "virtue_ethics", "vows_static",
             "vows_loop", "reflect_loop", "virtue_loop"]
    fig, axes = plt.subplots(1, 3, figsize=(8.6, 2.9), sharex=True)
    for ax, (fname, title) in zip(axes, models):
        by = load(ROOT / "results" / fname)
        rows, base = [], None
        for c in conds:
            rs = by.get(c, [])
            if not rs:
                continue
            k = sum(1 for r in rs if r["correct"])
            lo, hi = wilson(k, len(rs))
            val = k / len(rs)
            if c == "baseline":
                base = val
            rows.append((LABELS[c], val, lo, hi, color_of(c)))
        dotpanel(ax, rows, "accuracy", base)
        ax.set_title(title, fontsize=10.5)
        if ax is not axes[0]:
            ax.set_yticklabels([])
    fig.tight_layout()
    fig.savefig(OUT / "fig2_scruples.pdf", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    fig1()
    fig2()
    print("figures written to", OUT)
