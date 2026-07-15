# Paper Outline — Target: AI and Ethics (Springer)

**Working title:** Vows, Not Posters: Prompted Buddhist Ethics Shifts Moral
Frameworks in Open-Weight Language Models — and Reveals Whose Morality
Benchmarks Measure

**Alt title (safer):** Cultivating Ethical AI with the Four Great Bodhisattva
Vows: Framework Transfer, Process–Content Dissociation, and the Cultural
Assumptions of Moral Benchmarks

**Type:** Original empirical research / ~9,000–10,000 words + appendix
**Citation:** APA 7 / **Preprint:** arXiv (cs.CY) at submission

## Central thesis (one sentence)

Prompting an open-weight LLM with the Four Great Bodhisattva Vows does not
make it "more ethical" by Western benchmark lights — it *transfers* the
model's moral framework in doctrinally coherent directions that Western
crowd-labeled benchmarks record as errors; and the transfer helps rather
than harms real-life dilemma judgment when the vows are implemented as a
reflective process instead of a static creed.

## Three headline findings (evidence map)

- **F1 Framework transfer, one-directional (4/4 models).** Vow conditions
  raise "acceptable→WRONG" strictness (gemma .27→.49; gpt-oss .06→.29;
  qwen .07→.19; llama .13→.14) with no rise in leniency. Flipped items:
  butterfly net, wedding doves (不殺生), unasked borrowing (不与取),
  workplace gossip (正語). Data: strictness table, analysis.md.
- **F2 Process–content dissociation.** Static vows hurt everywhere
  (SCRUPLES: qwen −8.3pt p=.011, gemma −6.7pt p=.017); the 4-stage
  reflective loop is top condition on SCRUPLES for qwen (.663) and gpt-oss
  (.713, beats generic p=.007), n.s. for gemma. Loop > static in 11/12
  model×dataset paired tests.
- **F3 Clear-cut judgments survive.** MoralChoice-low ≈ ceiling in all
  conditions (no alignment tax on unambiguous harm) — except gemma×static
  (.68), whose errors explicitly cite Vow 1 to justify rule-breaking
  compassion; the loop restores .98. Deliberation disciplines the creed.
- (Methodological) **F4 Compliance confound.** gpt-oss×virtue collapses to
  parse rate .54 (counter-questions/refusals), accuracy unchanged on the
  parsed subset — ethics-prompting studies must report response compliance
  separately.

## Sections

1. **Introduction** (~1,200 w)
   - Ethical-AI aspiration; prompting as the accessible lever for
     open-weight local models (democratization angle: consumer hardware).
   - Gap: ethics prompting studied almost only with Western frameworks and
     judged against Western crowd labels.
   - RQs: RQ1 Does a Buddhist vow harness change moral judgment? RQ2 Is the
     change content- or process-driven? RQ3 What do the resulting benchmark
     "errors" tell us about the benchmarks?
   - Contributions list (F1–F4 + open artifacts).

2. **Background** (~1,800 w)
   2.1 Ethics prompting & persona effects (Moral Persuasion; persona
       susceptibility; ProMoral-Bench).
   2.2 Moral benchmarks and their provenance: ETHICS (MTurk, US),
       MoralChoice, SCRUPLES (Reddit AITA) — annotator populations.
   2.3 The Four Great Vows: doctrinal structure; why they are a *practice
       program* (発達的自己修養) rather than a value list; relation to
       precepts (不殺生・不与取・正語).
   2.4 Related: machine ethics beyond the West (Ubuntu, Confucian, and
       Buddhist-inspired AI ethics proposals — mostly theoretical, no
       empirical harness evaluation → our gap).

3. **The Four Vows Harness** (~1,400 w)
   - Design rationale: vow → computational operation mapping table
     (stakeholder enumeration / affliction introspection / multi-
     perspective review / aspirational revision).
   - Static vs loop implementations (5-turn dialogue); full prompts in
     Appendix A; translation/operationalization caveats (limitation §7).

4. **Methods** (~1,600 w)
   - Models: qwen3.6-35B, gemma3-27B, gpt-oss-20B, llama3.3-70B (ollama,
     4-bit quantized — stated), consumer/local hardware.
   - Conditions (5) incl. two controls: generic-ethics, virtue-ethics.
   - Datasets: ETHICS-cm test+hard (binary), MoralChoice-low (2-choice,
     position-randomized), SCRUPLES Dilemmas (2-choice + 5-annotator vote
     distribution + controversial flag). ~19,500 judgments total.
   - Metrics: accuracy w/ bootstrap CI; McNemar paired tests; strictness/
     leniency decomposition; human vote-share alignment; compliance rate.
   - Robustness: paraphrase variants of system prompt and loop stages
     (Appendix B). Reproducibility: full code/data release.
   - **Loop-content controls** (reviewer-anticipated confound: procedure
     vs content): identical 4-stage procedure under (a) secular framing
     (reflect_loop), (b) virtue framing (virtue_loop), vs vows_loop —
     on qwen & gemma, cm_test + SCRUPLES. Interpretation contingency:
     vows-only advantage → framework-specific effect; all-loops advantage
     → reflective-procedure effect with vows as one instantiation. Either
     outcome feeds Discussion §6; title emphasis shifts accordingly
     (value-grounded reflective reasoning as the general frame).

5. **Results** (~2,200 w)
   5.1 F1 strictness shift (table + flipped-item examples).
   5.2 F2 dissociation (SCRUPLES table; loop vs static forest plot).
   5.3 F3 ceiling tasks + gemma×static qualitative analysis (vow-cited
       rule-breaking; position-bias check).
   5.4 Consensus vs controversial split (loop gains concentrate on
       human-consensus items).
   5.5 F4 compliance; cost accounting (loop ≈5× calls/tokens).

6. **Discussion** (~1,800 w)
   - Framework transfer ≠ degradation: benchmarks encode a population's
     morality; scoring Buddhist-consistent judgments as errors is a
     category mistake → implications for "ethics leaderboards".
   - Why process beats content: parallels to virtue cultivation & moral
     development (practice over creed); connection to deliberative
     prompting literature (self-critique, debate).
   - East–West claim: what we can and cannot say (model's *representation*
     of Buddhism vs actual Buddhist-culture judgments); path to testing
     with JCommonsenseMorality / human annotators.
   - Practical guidance: if you value-load a local model, load a process.

7. **Limitations** (~700 w) — researcher-made vow translation (no
   doctrinal authority); English-only; quantized models; single-prompt
   families mitigated by paraphrase robustness; crowd labels as "human"
   anchor; no fine-tuning (future: process distillation).

8. **Conclusion** (~400 w)

9. Statements: ethics, AI-use disclosure, data availability (code + all
   19.5k judgments), funding (上廣 if awarded), CRediT.

**Appendices:** A full prompts (5 conditions + variants); B robustness
results; C flipped-item catalog with precept coding; D per-model tables.

## Figures/Tables plan

- T1 vow→operation mapping; T2 master accuracy (model×dataset×condition);
- F1 strictness-shift dot plot (4 models); F2 SCRUPLES forest plot
  (loop/static vs baseline); F3 consensus-vs-controversial bars;
- T3 compliance rates; T4 token/latency overhead.

## Writing order

Methods → Results → Harness → Background → Discussion → Intro → Abstract
(bilingual EN + 日本語は投稿誌要件になし; EN only) → polish pass
(writing-quality checklist) → internal peer review (5-dimension) → LaTeX
(Springer sn-jnl) → arXiv + submit.
