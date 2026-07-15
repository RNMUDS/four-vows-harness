# 6. Discussion

## 6.1 Content steers, procedure improves, and benchmarks conflate the two

The dissociation at the centre of our results assigns different jobs to
the two things a value harness contains. The *content* of the harness,
whether vows, virtues, or a bare instruction to be ethical, changes which
morality the model enacts: attention to ethics of any flavour moved
judgments toward strictness, and the items that flipped reflected the framing
applied (Section 5.1). The *procedure*, the cycle of reacting, enumerating stakeholders,
inspecting one's own distortions, entertaining dissent, and revising,
changes how well the model judges: on real-life dilemmas the secular
form of the loop scored highest on two of three models (significantly
above baseline on one) and level on the third, while no value framing
ever beat it. To be explicit: our data do not show that Buddhist
content improves moral judgment. They show that a reflective procedure
can, whatever it is practised in the name of; the vows' distinctive
contribution is directional, and it is the benchmarks' reaction to that
direction that constitutes the paper's second finding.

A single-label accuracy score cannot see this structure. It records
the strictness shift as error (because its labels encode one
annotator population's leniency), records the deliberative gain as
improvement, and returns their sum. We stress the scope of this claim:
it is an observation about how the three crowd-labelled benchmarks we
studied respond to framework shifts, not an argument that such
benchmarks are useless. For screening clear harms — where our F3
results show value-loading changes nothing — a single label is exactly
the right instrument. The hazard is confined to comparative claims
about *values*, where a difference in framework and a difference in
competence arrive as the same number. Two of our numbers make the point
concretely: the same vow loop that loses two to eight points against US
crowd labels on ETHICS commonsense is among the conditions that best
match the SCRUPLES annotator majority on consensus items. Whether the
vows made the model worse or better is not a property of the model; it
is a property of whose judgments the evaluation treats as ground truth.

## 6.2 Why creeds fail where practice succeeds

That static value injection never helped (significantly harmful on one
model, inert on the others, and below baseline under every rewording
tested) while the same commitments embedded in a procedure were benign
or helpful, is the pattern a virtue-ethical reading would predict: moral
capacity is exercised in practice, not possessed as principle (Vallor, 2016). The mechanism suggested by the transcripts is straightforward. A static creed
acts as a standing bias on generation: it tilts the answer while adding
no information the answer could use. The loop converts the same
commitments into *evidence*. By the time the final verdict is requested,
the context holds an enumeration of affected parties, a self-audit, and
two dissenting perspectives, and the verdict is conditioned on all of
it. That the secular loop matches or beats the value-framed loops
suggests the evidence is doing the work, and the framing contributes little: an interpretation the strictness data corroborate from the
other side, since sustained deliberation shifted commonsense judgments
even with no values named at all.

## 6.3 What may and may not be claimed about East and West

These results might be summarized as showing that "Buddhist AI
disagrees with Western benchmarks." Two considerations argue against
that reading. First, the
loop-content controls showed that the aggregate strictness shift follows
ethical attention generally, not Buddhist content specifically; the
doctrinal signature lives in which items flip, which is qualitative
evidence, not in the aggregate rate. Second, what the vow prompt
instills is the model's *learned representation* of Buddhist ethics, a
representation acquired predominantly from English-language text, and
we evaluated it only against US and English-community crowd labels.
Showing genuine cultural-framework divergence would require the other
anchor: labels from annotators within Buddhist cultural spheres (for
example the Japanese-annotated JCommonsenseMorality (Takeshita et al., 2023)), and
a test of whether vow-conditioned judgments track them better than
baseline. We regard that as the natural next study, and the present
results as establishing its motivating phenomenon: value-loading moves
models in directions that single-label benchmarks of this kind can only
register as error.

## 6.4 Implications for value alignment

The content/procedure dissociation maps onto a distinction that the
alignment literature draws conceptually but rarely tests empirically:
between aligning a system to some *substantive* set of values and
equipping it with a *procedure* whose fairness or thoroughness can be
endorsed from many value positions (Gabriel, 2020). Our results offer modest empirical support for the procedural side. Substantive loading, in
the static form available to every operator today, produced no measurable quality
gain and imposed a direction that only some populations would
endorse; the procedure improved judgment while remaining, in itself,
neutral about which morality supplies the stakeholders' weights. This
is also where the results touch pluralistic alignment (Sorensen et al.,
2024): a model that enumerates affected parties, audits itself, and
entertains dissent before answering is a plausible substrate for
Overton-style pluralism — it generates the perspectives a pluralistic
answer must survey — whereas a model with a creed in its system prompt
has been moved to one point in value space. If alignment must
serve many moralities at once, our data suggest that the more effective lever is the procedure a
model executes before answering rather than the values it is
instructed to hold.

## 6.5 Practical guidance

For practitioners who value-load open-weight models, the results reduce
to four rules of thumb. Stating values in the system prompt should not, by itself, be expected
to improve judgment; across four models and every wording we tried, it
never did. If judgment quality on contested cases matters, spend the
tokens on a reflective procedure (stakeholders, self-audit, dissent,
revise) and expect roughly fifty times the inference cost of a direct
answer. Any ethics prompt, whether creed or procedure, can be expected to
shift commonsense judgments toward strictness; decide whether that is drift or alignment
with reference to the population you serve rather than to a leaderboard.
And when evaluating, report compliance and verdict-extraction procedures
alongside accuracy: in our study, response-style artefacts could
produce spurious condition effects several times larger than the real
ones until validation identified them.

The cost multiplier suggests a direct continuation: distilling the
procedure into the weights. Our loop transcripts constitute training
data for exactly this, and process distillation, fine-tuning on
deliberations rather than on creeds, would test whether the
content/procedure dissociation survives the move from context to
parameters. We leave it to future work, noting the prediction this study implies:
tuning on the creed should reproduce its inertness; tuning on the
practice should preserve the gains.
