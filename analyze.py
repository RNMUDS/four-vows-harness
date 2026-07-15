#!/usr/bin/env python3
"""Aggregate all local + remote results into results/analysis.md."""

from harness.analysis import (dedupe, load_all, master_table,
                              scruples_human_alignment, strictness_table)


def main() -> None:
    records = dedupe(load_all(["results", "results/remote"]))
    report = "\n\n".join([
        "# Four Vows Harness — integrated analysis",
        f"Total records: {len(records)}",
        "# Master table" + master_table(records),
        "# Strictness shift (binary tasks)\n" + strictness_table(records),
        "# SCRUPLES human-distribution alignment\n"
        + scruples_human_alignment(records),
    ])
    with open("results/analysis.md", "w", encoding="utf-8") as fh:
        fh.write(report + "\n")
    print(report)


if __name__ == "__main__":
    main()
