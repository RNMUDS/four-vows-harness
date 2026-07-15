#!/usr/bin/env python3
"""Alignment-tax check: base 5 conditions on MMLU (capability control).

Usage: python3 run_tax.py <model> [n_items]
"""

import sys
import time

from harness.datasets import load_mmlu
from harness.runner import run_experiment

BASE_CONDITIONS = ["baseline", "generic_ethics", "virtue_ethics",
                   "vows_static", "vows_loop"]


def main() -> None:
    model = sys.argv[1]
    n_items = int(sys.argv[2]) if len(sys.argv) > 2 else 300
    items = load_mmlu(n=n_items)
    out_name = f"mmlu_{model.replace(':', '_').replace('/', '_')}"

    def log(msg: str) -> None:
        print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)

    log(f"tax check: model={model} items={len(items)}")
    run_experiment(model, BASE_CONDITIONS, items, out_name, log=log)
    log("done.")


if __name__ == "__main__":
    main()
