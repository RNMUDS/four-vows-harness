# 5. Results

Table 2 reports accuracy for every model x benchmark x condition cell
with bootstrap confidence intervals; this section presents the four
findings, using paired McNemar tests for all contrasts. All numbers
reflect the final, validated answer-extraction pass described in
Section 4.4 and Appendix C.

## 5.1 Ethical attention shifts judgment toward strictness (F1)

On the ETHICS commonsense splits, no vow condition improved accuracy,
and reductions were significant for Qwen 3.6 (test split, static:
p = .023; loop: p = .013, both vs baseline) and for GPT-OSS under the
loop (test: p = .017; hard: p = .0018). Gemma 3 showed a smaller loop-
only reduction (test: p = .035); Llama 3.3 was numerically lower without
reaching significance.

The direction of the errors is the more informative result. Where accuracy fell, it
fell almost entirely on the strict side: the rate at which crowd-
labelled *acceptable* actions were judged wrong rose under the vow loop
from .060 to .287 for GPT-OSS and from .067 to .147 for Qwen (both hard
split), and from .230 to .300 for Gemma (test split), while the
opposite error stayed flat or fell (full strictness tables for both
splits: Appendix B). The items that flipped correspond closely to precept
concerns: trapping a butterfly in a net, releasing doves at a
wedding (non-harm, 不殺生), borrowing a neighbour's mower unasked (not
taking what is not given, 不与取), broadcasting whom a business partner
had lunch with (right speech, 正語). We note below that the
aggregate shift is not unique to vow content.

The loop-content controls locate the source. On Qwen, the secular
reflect loop (.210) and virtue loop (.230) raised over-strictness at
least as much as the vow loop (.190) from the .090 baseline; on Gemma
the static vow prompt produced *no* shift (.230, identical to baseline)
while the three canonical loops shifted mildly (.29-.30; the
reworded vow loop, .26). Sustained ethical
deliberation of any framing moralizes commonsense judgment; the vow
framing supplies the flavour of individual flips, not the aggregate
effect.

## 5.2 The procedure, not the creed, improves dilemma judgment (F2)

SCRUPLES separates the conditions cleanly (baselines .630-.693, well off
ceiling). Three results establish the dissociation:

**Static value injection never helps.** Accuracy under the static vow
prompt fell significantly below baseline for Qwen (.547 vs .630,
p = .011), numerically for GPT-OSS (.667 vs .693), and was flat for
Gemma (.670 vs .680). Two independently reworded vow prompts landed
below baseline on both models tested (Appendix B), so the absence of
benefit is not a wording accident.

**The reflective procedure helps where anything does.** The vow loop was
the top condition for GPT-OSS (.713, beating generic ethics, p = .007)
and beat generic ethics on Qwen (.663 vs .590, p = .032); it sat at
baseline for Gemma (.677). On SCRUPLES the loop met or exceeded the
static prompt on every model (significantly so on Qwen, p = .0002); on
the ETHICS splits and MoralChoice the two were statistically
indistinguishable.

**The help does not come from the vows.** With the vow framing removed
(the reflect loop retains only the one-line generic-ethics system
prompt), the secular procedure was the highest-scoring condition on
Qwen (.707 vs .630 baseline, p = .015; survives within-model Holm
correction) and on Gemma (.703 vs .680; not significant, p = .41,
with the reworded vow loop close behind at .700). On GPT-OSS the three
loops and baseline were statistically indistinguishable (.690-.713 vs
.693; vow loop vs baseline p = .50). No value framing significantly
outperformed the secular procedure anywhere. Where the procedure
helps, it supplies the gain; the value content adds nothing detectable
to accuracy.

Alignment with the human vote distribution shows the same pattern from
the annotators' side: on consensus items the Qwen loops matched the crowd at
.79-.81 vote-share against a .768 baseline while the static prompt fell
to .626; on controversial items every condition sat near .51-.56, as it
must when the crowd itself is split.

## 5.3 Unambiguous judgments and capabilities survive (F3)

MoralChoice low-ambiguity sat at ceiling for every model and condition
(.99-1.00 everywhere; GPT-OSS's virtue prompt reached only .96 through
non-compliance, not misjudgment — see 5.5). Value-loading, whether as
creed or as procedure, did not corrupt clear-cut moral choices.

MMLU (run on Qwen and Gemma) is close to the same pattern. Qwen scored
.803-.857 across all five conditions against a .830 baseline (no
significant movement). Gemma's static prompt was likewise inert (.747
vs .757), but its vow loop cost .06 (.697, p = .036) — a small but
real deliberation tax on this model, consistent with its loop-driven
strictness shift. The static prompt does not damage competence; sustained deliberation
can, mildly and model-dependently.

## 5.4 Robustness (Appendix B)

Both headline effects survived paraphrase. Reworded vow prompts
reproduced the strictness pattern on both models tested and the ordering
loop >= baseline > static on SCRUPLES (Qwen reworded loop .667 vs .663
original; reworded statics .587/.607 vs .547). Effect *magnitudes*
moved with wording — the static penalty on Qwen spanned -8.3 to -2.3
points across phrasings, and on Gemma the reworded vow loop scored
above the canonical one (.700 vs .677 on SCRUPLES) — but no rewording
reversed a reported direction.

## 5.5 Compliance, extraction, and cost (F4)

Two response-style phenomena would be mistaken for moral effects if
left unreported. First, non-compliance: GPT-OSS under the virtue prompt
answered only 54% of SCRUPLES items, returning counter-questions or
refusals; restricted to answered items, its accuracy (.699) matched the
baseline condition's answered-subset accuracy (.707; .693 with
non-compliance counted as error, as in Table 2). Second, extraction validity: ethics prompts changed not just
what models concluded but *how they formatted conclusions*: Gemma in particular switched to
answer-first-then-explain layouts or opened with prose in which the
article "A" is easily mistaken for an option letter by a naive parser
(all cells materially affected were Gemma's; every other model's
deltas were below two points, Appendix C). In early analysis passes these artefacts produced spurious condition
effects of up to 32 accuracy points before validation identified them (Appendix C tabulates all affected cells). We therefore treat verdict extraction as a threat to
validity in its own right: our final parser resolves explicit answer
markers first, restricts line heuristics to short verdict lines,
disambiguates article uses of "A", is covered by a unit-test suite
included in the release, and was re-applied to every stored raw response
(Appendix C). We recommend that ethics-prompting studies report
compliance and extraction procedures as routinely as accuracy.

The reflective loop is costly: median 4,764 tokens
and 12.7 s per item against 83 tokens and 0.6 s for baseline (a 57x
token multiplier at 5 calls per item); static prompts cost 4.9x baseline
tokens. Whether the SCRUPLES gains justify a 57x inference budget is a
deployment decision; Section 6 notes distillation of the procedure
as a direction for future work.
