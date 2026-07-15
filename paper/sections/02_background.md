# 2. Background and Related Work

## 2.1 Steering moral judgment through prompts

That system prompts move the moral behaviour of language models is by
now well established. Persona assignment shifts moral-dilemma responses,
with susceptibility varying by model family and persona type (Costa et al., 2025); framing prompts with utilitarian, deontological, or virtue-
ethical vocabulary shifts judgments in framework-consistent directions
(Huang et al., 2024); and benchmark suites comparing prompting strategies for
moral reasoning report large spreads between paradigms on identical
items (Thomas et al., 2026). Constitutional approaches make value content
explicit at training time rather than inference time, but share the
underlying form: values enter the system as *statements* (Bai et al., 2022).
Two gaps remain. Almost all of this work draws its value content from
the Western ethical canon, and almost none of it separates the effect of
the value statement from the effect of the reasoning procedure it is
embedded in. Both gaps are the subject of this paper.

Separately, a growing literature shows that structured deliberation —
self-critique, multi-perspective debate, reflection before answering —
improves language-model reasoning on tasks with verifiable answers
(Madaan et al., 2023; Du et al., 2024). Our loop conditions import that insight into the moral
domain, where "improvement" itself becomes contested, which is what makes the transfer informative.

## 2.2 Moral benchmarks and whose morality they encode

The ETHICS suite operationalizes commonsense morality as the judgments
of US crowdworkers on short first-person scenarios (Hendrycks, Burns, Basart, Critch, et al., 2021);
MoralChoice generates two-action decisions ranked against common moral
rules (Scherrer et al., 2023); SCRUPLES collects real-life interpersonal
anecdotes with community verdicts, retaining full annotator
distributions and flagging items on which annotators split (Lourie et al., 2021). Recent critique has begun to press on the provenance of such
labels: moral benchmarks embed the demographics, language, and norms of
their annotator pools, and models tuned or evaluated against them
inherit that anchoring (Ramezani & Xu, 2023; Santurkar et al., 2023). What this critique has mostly
lacked is an experimental probe — an intervention that moves a model
toward a *specific, articulable* alternative framework so that the
benchmark's reaction can be observed. Our vow harness serves as such a
probe, and SCRUPLES's retained vote distributions let us score the same
behaviour against human disagreement rather than against a single label.

## 2.3 Buddhist ethics and AI

Proposals to bring Buddhist ethics to AI predate large language models
and have remained largely conceptual: analyses of what non-harm,
non-self, or karuna would imply for machine agency and AI governance
(Hongladarom, 2020), and comparative surveys positioning Buddhist frameworks
alongside consequentialist and deontological ones for machine ethics
(Vallor, 2016). What distinguishes the present work is implementation
and measurement: a specific liturgical formula is translated, operation
by operation, into an executable reasoning procedure, and its
behavioural consequences are measured against controls at scale. To our
knowledge no prior study has done this for any Buddhist formula, nor
compared a religious value harness against procedure-matched secular
controls.

## 2.4 The Four Great Vows

The Four Great Bodhisattva Vows condense the Mahayana bodhisattva path
into four commitments recited daily across East Asian traditions; their
canonical form in Japanese Zen liturgy pairs each vow with an
inexhaustible object — all beings, all afflictions, all teachings, the
unsurpassable way (Foulk, 2010). Doctrinally they are classed as
aspiration (praṇidhāna), not precept: they bind the practitioner to a
direction of effort rather than to a rule whose satisfaction could be
checked (Dayal, 1932). Section 3 argues that this makes them uniquely
suited to the present experiment, because an aspiration, unlike a rule,
must be *practised* — and practising, in a language model, is something
a prompt can either fake (by stating the aspiration) or approximate (by
executing it). Our conditions measure the distance between the two.
