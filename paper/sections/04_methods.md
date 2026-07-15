# 4. Methods

## 4.1 Models

We evaluated four open-weight instruction-tuned models spanning four
independent model families and 20-70B parameters: Qwen 3.6 35B, Gemma 3
27B, GPT-OSS 20B, and Llama 3.3 70B. All models ran locally through
ollama with the default 4-bit quantization, on consumer and workstation
hardware (an Apple M4 Max with 64 GB of unified memory, an NVIDIA DGX
Spark, a single RTX 5090 workstation, and an Apple Mac Studio with 256 GB
of unified memory). This choice is deliberate. Value-loading through
prompting is the only intervention available to most practitioners who
deploy open-weight models on their own infrastructure, so the population
of models we study is the population the question is about. Quantization
is part of that deployment reality; we return to its implications in the
Limitations section.

Concretely: ollama 0.30.6 throughout; model tags qwen3.6:latest
(35B), gemma3:27b, gpt-oss:20b, llama3.3:70b, pulled July 2026; Qwen,
Gemma, and Llama in ollama's default 4-bit GGUF quantization, GPT-OSS
in its native MXFP4. Qwen ran on the M4 Max, Llama on the DGX Spark,
Gemma on the RTX 5090 workstation, GPT-OSS on the Mac Studio; hardware
affects latency only, not outputs, at temperature 0.

GPT-OSS 20B is a reasoning model whose deliberation channel cannot be
disabled. We capped its reasoning effort at the lowest setting and raised
the generation budget so that a visible answer always followed the
reasoning; without this adjustment the model spent its entire token
budget reasoning and returned empty answers (Section 5.5 reports the
associated compliance findings).

## 4.2 Conditions

Every item was presented under five primary conditions:

1. **baseline** — no system prompt.
2. **generic ethics** — a system prompt instructing the model to "always
   act ethically" and weigh moral implications.
3. **virtue ethics** — a system prompt framing right action as what a
   fully virtuous person would characteristically do, following the
   framing used in prior ethics-prompting work (Huang et al., 2024).
4. **vows static** — a system prompt stating the Four Great Bodhisattva
   Vows (四弘誓願) with a one-sentence behavioural gloss per vow
   (Appendix A gives all prompts verbatim).
5. **vows loop** — the same vow system prompt, plus a five-turn
   reflective procedure executed before every answer: the model states an
   initial reaction, then works through one turn per vow — enumerating
   affected parties (vow 1), inspecting its own reasoning for craving,
   aversion, and delusion in their conversational guises of
   people-pleasing, harshness, and overconfident bias (vow 2), weighing
   at least two dissenting moral perspectives (vow 3) — and finally
   issues a revised verdict (vow 4).

Two families of controls address the confound the design would otherwise
leave open, namely whether any observed effect comes from the vows or
from the procedure that carries them:

- **Loop-content controls.** The identical four-stage procedure was run
  under a secular framing with no evaluative vocabulary beyond the
  generic-ethics system prompt (**reflect loop**) and under a virtue-
  ethics framing (**virtue loop**). The three loops differ only in what
  the stages are done in the name of; the operations are word-for-word
  parallel.
- **Paraphrase controls.** Two independently reworded versions of the
  vow system prompt and one reworded set of loop-stage instructions
  guard against effects specific to a single phrasing (Appendix B).

Paraphrase controls were run on Qwen 3.6 and Gemma 3 (the models
showing the largest primary effects) on one binary and one dilemma
benchmark; loop-content controls were run on those two models plus
GPT-OSS on SCRUPLES.

**Design coverage.** Not every model x benchmark cell was run. Llama
3.3 70B has full data on the two ETHICS splits only (its per-item
deliberation cost was prohibitive on our hardware; the vow-loop cell on
the hard split was curtailed at n = 52), and it lacks MoralChoice,
SCRUPLES, and MMLU. MMLU was run on Qwen and Gemma only. Table 2 marks
every missing or curtailed cell explicitly.

## 4.3 Benchmarks

Four English-language benchmarks with complementary properties:

- **ETHICS commonsense**, test and adversarially filtered hard split
  (Hendrycks, Burns, Basart, Critch, et al., 2021): first-person scenarios labelled morally wrong or
  acceptable by US crowdworkers. Binary judgment; we sampled 200 (test)
  and 300 (hard) items per condition, balanced across labels, fixed seed.
- **MoralChoice low-ambiguity** (Scherrer et al., 2023): two-action decisions in
  which one action clearly conforms to a common moral rule. 300 items;
  the position of the rule-conforming action was randomized per item to
  control position bias.
- **SCRUPLES Dilemmas** (Lourie et al., 2021): paired real-life actions from
  community anecdotes, each annotated by five crowdworkers as to which
  action is more ethically wrong, retaining the full vote distribution
  and a controversiality flag. 300 items, positions randomized. This
  benchmark carries the human-disagreement structure that single-label
  sets discard.
- **MMLU** (Hendrycks, Burns, Basart, Zou, et al., 2021), 300 questions sampled across all 57 subjects,
  as a capability control for an alignment tax.

## 4.4 Procedure and metrics

All generations used temperature 0. Answers were requested in a fixed
one-token format per task ("WRONG"/"ACCEPTABLE", or an option letter)
and extracted by a rule-based parser whose final-line-first heuristic and
negation handling were unit-tested; refusals and non-compliant responses
(counter-questions, meta-commentary) were detected separately. We report:

- **Accuracy** against benchmark labels, with 95% percentile bootstrap
  confidence intervals (10,000 resamples). Unparsed responses count as
  incorrect, which is conservative; compliance is reported alongside.
- **Paired condition contrasts** by exact McNemar tests on items shared
  between conditions, the appropriate test given that every condition
  saw identical items.
- **Error direction** on binary tasks, decomposed into over-strictness
  (acceptable items judged wrong) and over-leniency (wrong items judged
  acceptable).
- **Human-distribution alignment** on SCRUPLES: the mean share of the
  five annotator votes received by the option the model chose, reported
  separately for consensus and controversial items. A model that always
  sides with a unanimous majority scores 1.0; chance is 0.5.
- **Compliance**: the fraction of responses from which any verdict could
  be extracted, and the refusal rate within the remainder.
- **Cost**: median tokens and latency per item, and calls per item.

In total the study comprises 27,352 judgments (all conditions,
including controls and paraphrase variants).

**Statistical framing.** Given the number of pairwise contrasts, we
treat all tests as exploratory and report exact two-sided McNemar
p-values without correction, noting for each headline result whether it
survives a Holm correction within its model's contrast family. Claims
in the abstract are limited to results that do. All code, prompts,
and raw per-item records are released for exact reproduction; every
run is resumable and deterministic given the fixed seeds and zero
temperature.
