# Four Vows Harness

Code, prompts, and complete per-item results for the paper:

> **Vows, Not Posters: Separating Value Content from Reflective
> Procedure in Open-Weight Language Models** (submitted; preprint link
> forthcoming)

We render the Four Great Bodhisattva Vows (四弘誓願) as (a) a static
system prompt and (b) a four-stage reflective reasoning procedure, and
evaluate four open-weight model families (20-70B, run locally via
ollama) on ETHICS, MoralChoice, SCRUPLES, and MMLU against generic-
ethics, virtue-ethics, paraphrase, and procedure-matched secular
controls — 27,352 judgments in total.

## Layout

```
harness/          experiment library (conditions, runner, parsing, scoring, analysis)
tests/            pytest suite (44 tests; includes the verdict-extraction cases)
run_exp.py        one model x one dataset x 5 primary conditions
run_pilot.py      ETHICS commonsense test-split runner
run_variants.py   paraphrase-control conditions
run_loop_controls.py  secular/virtue procedure-matched controls
run_tax.py        MMLU capability control
analyze.py        integrated analysis -> results/analysis.md
results/          per-item JSONL records (validated extraction pass)
results_backup_preparse/  same records under the naive first-pass parser
                  (audit evidence for the paper's Appendix C)
scripts/fetch_data.sh     downloads the third-party benchmarks
paper/            manuscript sources (markdown sections + LaTeX build)
```

## Reproduction

Requirements: Python 3.11+, `requests numpy scipy pandas pytest`,
[ollama](https://ollama.com) >= 0.30 with the models
`qwen3.6:latest`, `gemma3:27b`, `gpt-oss:20b`, `llama3.3:70b`.

```bash
./scripts/fetch_data.sh          # ETHICS, MoralChoice, SCRUPLES, MMLU
python3 -m pytest tests/ -q      # 44 tests
python3 run_exp.py gemma3:27b scruples 300   # example run
python3 analyze.py               # regenerate results/analysis.md
```

All generation is at temperature 0 with fixed sampling seeds; runs are
resumable per (model, condition, item) and deterministic. A remote
ollama can be targeted with `OLLAMA_URL=http://host:11434`.

Each results record stores the raw model response, so the entire
analysis (including the extraction audit in `results_backup_preparse/`)
can be recomputed without re-running any model.

## Datasets

Third-party benchmarks are not redistributed here; `scripts/fetch_data.sh`
downloads them from their original sources. Please cite the original
papers (Hendrycks et al. 2021; Scherrer et al. 2023; Lourie et al. 2021)
when using them.

## License

MIT (code and our result records). Third-party datasets retain their
own licenses.
