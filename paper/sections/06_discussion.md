# 6. Discussion

## 6.1 Content steers, procedure improves, and benchmarks conflate the two

The dissociation at the centre of our results assigns different jobs to
the two things a value harness contains. The *content* of the harness,
whether vows, virtues, or a bare instruction to be ethical, changes which
morality the model enacts: attention to ethics of any flavour moved
judgments toward strictness, and the items that flipped wore the flavour
of the framing applied, from netted butterflies to broadcast lunch
companions. The *procedure*, the cycle of reacting, enumerating stakeholders,
inspecting one's own distortions, entertaining dissent, and revising,
changes how well the model judges: on real-life dilemmas the secular
form of the loop scored highest on two of three models (significantly
above baseline on one) and level on the third, while no value framing
ever beat it.

A benchmark that reports a single accuracy number cannot see this
structure. It scores the strictness shift as error (because its labels
encode one population's leniency), scores the deliberative gain as
improvement, and returns their sum. Two of our numbers make the point
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
capacity is exercised in practice, not possessed as principle (Vallor, 2016). The mechanism our transcripts suggest is prosaic. A static creed
acts as a standing bias on generation: it tilts the answer while adding
no information the answer could use. The loop converts the same
commitments into *evidence*. By the time the final verdict is requested,
the context holds an enumeration of affected parties, a self-audit, and
two dissenting perspectives, and the verdict is conditioned on all of
it. That the secular loop matches or beats the value-framed loops
suggests the evidence is doing the work, and the framing at best rides
along: an interpretation the strictness data corroborate from the
other side, since sustained deliberation shifted commonsense judgments
even with no values named at all.

## 6.3 What may and may not be claimed about East and West

It is tempting to headline these results as "Buddhist AI disagrees with
Western benchmarks." Two considerations restrain us. First, the
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
models in directions that current benchmarks can only register as error.

## 6.4 Practical guidance

For practitioners who value-load open-weight models, the results reduce
to four rules of thumb. Do not paste a creed into the system prompt and
expect improvement; across four models and every wording we tried, it
never helped. If judgment quality on contested cases matters, spend the
tokens on a reflective procedure (stakeholders, self-audit, dissent,
revise) and expect roughly fifty times the inference cost of a direct
answer. Expect any ethics prompt, creed or procedure, to stricten
commonsense judgments, and decide whether that is drift or alignment
with reference to the population you serve rather than to a leaderboard.
And when evaluating, report compliance and verdict-extraction procedures
alongside accuracy: in our study, response-style artefacts could
fabricate condition effects several times larger than the real ones
until validation caught them.

The cost multiplier invites an obvious continuation: distilling the
procedure into the weights. Our loop transcripts constitute training
data for exactly this, and process distillation, fine-tuning on
deliberations rather than on creeds, would test whether the
content/procedure dissociation survives the move from context to
parameters. We leave it to future work, with the present study's
prediction on record: tuning on the creed should reproduce its
inertness; tuning on the practice should carry the gains.
