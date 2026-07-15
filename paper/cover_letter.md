# Cover Letter — AI and Ethics (Springer)

Dear Editors of AI and Ethics,

Please consider our manuscript, "Vows, Not Posters: Separating Value Content from Reflective Procedure in Open-Weight Language Models," for
publication as an original research article.

Operators of open-weight language models can align their systems only
through what they write into the context window, and they usually write
value statements. The manuscript asks whether values do their work as
statements possessed or as practices performed. We implement the Four
Great Bodhisattva Vows both as a static system prompt and as a
four-stage reflective procedure, and evaluate four open-weight model
families on four benchmarks (27,352 judgments) against generic-ethics,
virtue-ethics, paraphrase, and procedure-matched controls. Three
results emerge. Sustained ethical deliberation of any framing shifted
commonsense moral judgments toward strictness — a framework shift that
crowd-labelled benchmarks record as error. No static value prompt
produced a significant improvement on any model tested, whereas the
reflective procedure raised accuracy on real-life dilemmas,
significantly on one of three models, and was never significantly
outperformed by any value-framed variant. And value prompts altered
response style enough that unvalidated answer extraction produced
spurious effects larger than the true ones, which we audit and correct
with a released, unit-tested extraction suite.

We believe the manuscript suits AI and Ethics because it connects
empirical evaluation with questions the journal's readership works on
directly: how operators of locally deployed models should load values
in practice, how the results bear on procedural versus substantive
conceptions of alignment and on value pluralism, and whose morality
current moral benchmarks encode. To our knowledge, no prior study has
implemented and empirically evaluated a harness derived from a Buddhist
liturgical formula, or compared a religious value harness against
procedure-matched secular controls.

All code, prompts, and per-item records (including raw model responses)
are publicly available at https://github.com/RNMUDS/four-vows-harness,
and every experiment reproduces on consumer hardware. The manuscript is
not under consideration elsewhere. We have no conflicts of interest;
the use of an AI coding assistant is disclosed in the manuscript's
declarations.

Thank you for your consideration.

Sincerely,
Ryota Nakamura
Faculty of Data Science, Musashino University
ryota.nakamura@ds.musashino-u.ac.jp
