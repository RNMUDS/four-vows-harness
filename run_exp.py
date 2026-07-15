#!/usr/bin/env python3
"""Run one model over a named dataset, all 5 conditions.

Usage: python3 run_exp.py <model> <dataset> [n_items]
Datasets: cm_test | cm_hard | mc_low | mc_high
"""

import sys
import time

from harness.conditions import CONDITIONS
from harness.datasets import (load_ethics_commonsense, load_moralchoice,
                              load_scruples_dilemmas)
from harness.runner import run_experiment

LOADERS = {
    "cm_test": lambda n: load_ethics_commonsense("test", n=n),
    "cm_hard": lambda n: load_ethics_commonsense("test_hard", n=n),
    "mc_low": lambda n: load_moralchoice("low", n=n),
    "mc_high": lambda n: load_moralchoice("high", n=n),
    "scruples": lambda n: load_scruples_dilemmas("test", n=n),
}


def main() -> None:
    model, dataset = sys.argv[1], sys.argv[2]
    n_items = int(sys.argv[3]) if len(sys.argv) > 3 else 300
    items = LOADERS[dataset](n_items)
    out_name = f"{dataset}_{model.replace(':', '_').replace('/', '_')}"

    def log(msg: str) -> None:
        print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)

    log(f"exp: model={model} dataset={dataset} items={len(items)}")
    path = run_experiment(model, list(CONDITIONS), items, out_name, log=log)
    log("done.")
    try:
        from harness.scoring import summarize
        print(summarize(path))
    except ImportError:
        log("scoring deps unavailable here; summarize locally.")


if __name__ == "__main__":
    main()
