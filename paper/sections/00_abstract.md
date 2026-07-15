# Abstract

**Title:** Vows, Not Posters: Value Content, Reflective Procedure, and
What Moral Benchmarks Measure — Evidence from a Four Great Vows
Harness for Open-Weight Language Models

Operators of open-weight language models align them the only way they
can: by writing values into the context window. We ask whether values
work better as statements possessed or as practices performed, taking
the distinction from the Four Great Bodhisattva Vows (四弘誓願), a
Mahayana liturgical formula that binds practitioners to open-ended
practice rather than checkable rules. We implement the vows as a static
system prompt and, alternatively, as a four-stage reflective procedure
(enumerate affected parties; audit one's own reasoning; entertain
dissenting perspectives; revise), and evaluate four open-weight model
families (20-70B, run locally) on ETHICS, MoralChoice, SCRUPLES, and
MMLU — over 27,000 judgments — against generic-ethics, virtue-ethics,
paraphrase, and procedure-matched controls. We report three findings.
First, sustained ethical deliberation of any framing shifted
commonsense judgments toward strictness, a framework shift that
US-crowd-labelled benchmarks record as error, while general capability
was largely unaffected. Second, value content and reasoning procedure
dissociate: no static prompt produced a significant improvement on any
model tested, whereas the reflective procedure raised real-life dilemma
accuracy — significantly on one of three models — and was never
significantly outperformed by any value-framed variant. Third, ethics
prompts alter response style enough that unvalidated answer extraction
fabricated spurious effects larger than the true ones, motivating
compliance and extraction reporting as standard practice. Value content
steers the direction of judgment; reflective procedure supplies its
quality; crowd-labelled benchmarks of the kind we studied conflate the
two. Code, prompts, and per-item records are released.

**Keywords:** AI ethics; large language models; Buddhist ethics; moral
benchmarks; value alignment; reflective reasoning
