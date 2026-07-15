#!/usr/bin/env python3
"""Loop-content controls: same 4-stage procedure, secular vs virtue framing.

Usage: python3 run_loop_controls.py <model> <dataset> <out_name> [n_items]
"""

import sys
import time

from harness.datasets import load_ethics_commonsense, load_scruples_dilemmas
from harness.runner import run_experiment

CONTROL_CONDITIONS = ["reflect_loop", "virtue_loop"]

LOADERS = {
    "cm_test": lambda n: load_ethics_commonsense("test", n=n),
    "scruples": lambda n: load_scruples_dilemmas("test", n=n),
}


def main() -> None:
    model, dataset, out_name = sys.argv[1], sys.argv[2], sys.argv[3]
    n_items = int(sys.argv[4]) if len(sys.argv) > 4 else 300
    items = LOADERS[dataset](n_items)

    def log(msg: str) -> None:
        print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)

    log(f"loop-controls: model={model} dataset={dataset} -> {out_name}")
    run_experiment(model, CONTROL_CONDITIONS, items, out_name, log=log)
    log("done.")


if __name__ == "__main__":
    main()
