#!/usr/bin/env python3
"""Pilot experiment: one model x all 5 conditions x ETHICS commonsense sample.

Usage: python3 run_pilot.py [model] [n_items]
"""

import sys
import time

from harness.conditions import CONDITIONS
from harness.datasets import load_ethics_commonsense
from harness.runner import run_experiment


def main():
    model = sys.argv[1] if len(sys.argv) > 1 else "qwen3.6:latest"
    n_items = int(sys.argv[2]) if len(sys.argv) > 2 else 200
    items = load_ethics_commonsense("test", n=n_items)
    out_name = f"pilot_{model.replace(':', '_').replace('/', '_')}"

    def log(msg):
        print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)

    log(f"pilot: model={model} items={len(items)} "
        f"conditions={list(CONDITIONS)}")
    path = run_experiment(model, list(CONDITIONS), items, out_name, log=log)
    log("done.")
    try:
        from harness.scoring import summarize
        print(summarize(path))
    except ImportError:
        log("scoring deps unavailable here; summarize locally.")


if __name__ == "__main__":
    main()
