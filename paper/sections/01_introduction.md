# 1. Introduction

Capable language models can now be run locally from openly released
weights on consumer hardware, by operators subject to no platform
provider's alignment process. For this rapidly growing population of
deployments, the entire apparatus of value alignment reduces to what can
be written into a context window: if the operator of a local model wants
it to be good, they must *tell* it to be good. What, then, should they
write?

The intuitive answer — stating one's values — is long established but
of limited reach. Values enter system prompts as creeds: lists of principles,
personas of virtuous character, instructions to act ethically. Prior
work shows such statements do change moral behaviour (Bai et al., 2022;
Scherrer et al., 2023), but
it rarely asks a question any contemplative tradition would put first:
whether values do their work as *statements possessed* or as *practices
performed*. Buddhism is unusually explicit on the point. The Four Great
Bodhisattva Vows (四弘誓願), recited daily across East Asian Mahayana
traditions, are not rules to satisfy but commitments to practise: to
attend to all beings, to cut one's own delusions, to study boundless
teachings, to keep walking an unsurpassable way. A creed one can paste;
a vow must be executed.

The choice of this formula is not arbitrary. The vows are ecologically
real: among the most widely recited formulas in the Mahayana world, not a
value set constructed for the experiment. They are decomposable: their
four objects specify four distinct movements of attention (toward those
affected, into one's own distortions, across other understandings,
onward to a better answer) that a dialogue system can literally
execute, one turn each. And they are aspirations rather than rules: a rule invites checking, an
aspiration demands practice, which is the contrast under study.
Section 3 develops the mapping.

This paper takes that distinction literally and tests it. We translate
the four vows into two harnesses for open-weight models: a *static*
form, in which the vows and behavioural glosses sit in the system prompt,
and a *loop* form, in which each vow becomes one turn of a mandatory
reflection procedure (enumerate the affected parties, audit one's own
reasoning for craving, aversion, and delusion, entertain dissenting
moral perspectives, then revise) executed before every answer. Against
these we run three controls that most studies omit: a generic
be-ethical prompt, a Western virtue-ethics prompt, and the *same
four-stage procedure with the vows removed*, which allows value content
and reasoning procedure to be estimated separately. Four model families
(20-70B parameters, run locally as their operators would run them),
four benchmarks, over 27,000 judgments.

We asked whether the vows would make models more ethical. The results instead address three narrower questions:

- **RQ1 (effect):** Value-loading moved judgment, but sustained moral
  deliberation of any framing, Buddhist or not, shifted commonsense
  verdicts toward strictness (static prompts did so model-dependently),
  and the shift is scored as *error* by benchmarks whose labels encode
  US crowdworker leniency.
- **RQ2 (mechanism):** On real-life dilemmas, the reflective procedure
  improved judgment while the creed never did, and the procedure
  worked at least as well with the vows removed, retaining only a
  one-line generic ethics instruction. The vows steer; the
  practice improves; the two are separable — the improvement belongs
  to the reflective procedure, not to the Buddhist content.
- **RQ3 (measurement):** A benchmark score summed over these effects
  conflates a change of moral framework with a change of competence. We
  show the two can be decomposed (by error direction, by
  human-vote-distribution alignment, and by compliance) and that
  ethics prompts also change response *style* enough to fabricate
  large pseudo-effects when answer extraction goes unvalidated.

Contributions. (1) To our knowledge, the first implemented, empirically
evaluated harness
that renders a Buddhist liturgical formula as an executable reasoning
procedure, with paraphrase and procedure-matched controls. (2) A
content/procedure dissociation for value prompting: no static creed
significantly improved judgment on any model tested, while the same
commitments executed as reflection can help, with the secular form of
the procedure performing at least as well as any value-framed one. (3) Evidence that moral benchmarks register framework shifts as
errors, with a decomposition that separates the two. (4) A methodological
audit showing that compliance and verdict-extraction artefacts can
exceed true condition effects, with a validated open-source extraction
suite. (5) Full release of code, prompts, and 27,000+ per-item records,
reproducible on consumer hardware.

The paper proceeds as follows. Section 2 situates the work; Section 3
presents the vow harness; Sections 4-5 give methods and results;
Section 6 discusses what steering, improving, and measuring each turn
out to mean; Sections 7-8 conclude.
