# Abstract

**Title:** Vows, Not Posters: Value Content, Reflective Procedure, and
What Moral Benchmarks Actually Measure — Evidence from a Four Great
Vows Harness for Open-Weight Language Models

Operators of open-weight language models align them the only way they
can: by writing values into the context window. We ask whether values
work better as statements possessed or as practices performed, taking
the distinction from the Four Great Bodhisattva Vows (四弘誓願), a
Mahayana liturgical formula that binds practitioners to open-ended
practice rather than checkable rules. We translate the vows into a
static system prompt and, alternatively, into a four-stage reflective
procedure (enumerate affected parties; audit one's own reasoning for
craving, aversion, and delusion; entertain dissenting perspectives;
revise), and evaluate four open-weight model families (20-70B, run
locally) across ETHICS, MoralChoice, SCRUPLES, and MMLU — over
27,000 judgments — against generic-ethics, virtue-ethics, paraphrase,
and procedure-matched secular controls. Three findings emerge. First,
every form of ethical attention shifted commonsense judgments toward
strictness (e.g., .06 to .29 false-"wrong" rate), a framework shift
that US-crowd-labelled benchmarks can only score as error, while
general capability (MMLU, two models tested) was largely unaffected. Second, value content and reasoning
procedure dissociate: static creeds never improved judgment on any
model or wording, whereas the reflective procedure raised real-life dilemma
accuracy, significantly so on one of three models tested and
numerically on the others — and the secular variant with the vows
removed did at least as well as any value-framed one. Third,
ethics prompts alter response style enough that unvalidated answer
extraction fabricated pseudo-effects exceeding the true ones,
motivating compliance and extraction reporting as standard practice.
Value content steers the direction of judgment; reflective procedure
supplies its quality; current moral benchmarks conflate the two. We
release all code, prompts, and per-item records.

**Keywords:** AI ethics; large language models; Buddhist ethics; moral
benchmarks; prompting; reflection; value alignment; open-weight models
