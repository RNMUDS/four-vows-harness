# 3. The Four Vows Harness

## 3.1 Why these vows

The Four Great Bodhisattva Vows (四弘誓願, *shigu seigan*) are recited
daily across East Asian Mahayana traditions:

1. 衆生無辺誓願度 — Beings are numberless; I vow to save them all.
2. 煩悩無尽誓願断 — Delusions are inexhaustible; I vow to end them all.
3. 法門無量誓願学 — Dharma gates are boundless; I vow to learn them all.
4. 仏道無上誓願成 — The Buddha way is unsurpassable; I vow to attain it.

Two properties make them a sharper instrument for this study than a list
of precepts would be. First, they are *aspirational commitments rather
than rules*: each names an inexhaustible object (all beings, all
delusions, all teachings, an unsurpassable way) and binds the practitioner to a direction rather than a boundary. Second, they already have the shape of a procedure.
Read in order, they describe a movement of attention — outward to those
affected, inward to one's own distortions, sideways to other
understandings, and forward toward a better answer — that corresponds to a sequence of reasoning steps. The harness makes that mapping
explicit.

## 3.2 From vow to operation

Table 1 gives the translation we operationalize.

| Vow | Doctrinal object | Computational operation |
|---|---|---|
| 1 衆生無辺誓願度 | all sentient beings | enumerate every affected party; note harm and benefit to each |
| 2 煩悩無尽誓願断 | the three poisons (貪瞋癡) | inspect the model's own draft reasoning for people-pleasing (craving), harshness (aversion), and overconfident bias (delusion) |
| 3 法門無量誓願学 | boundless teachings | articulate at least two moral perspectives that dispute the current reaction |
| 4 仏道無上誓願成 | the unsurpassable way | revise toward the wisest and most compassionate answer available |

The second row does the most interpretive work and deserves defence. The
three poisons are classically dispositions of a person, not properties
of a text. We map them onto the failure modes they produce in
conversational systems: craving onto sycophancy (telling the user what
they want to hear), aversion onto dismissiveness, and delusion onto
overconfidence and unexamined bias. These correspondences are not ours
alone; each mirrors a documented behavioural failure of instruction-tuned
models (Sharma et al., 2024). Still, the mapping is a modelling decision made
by the authors, not a doctrinal authority, and we flag it as such in the
Limitations.

## 3.3 Two implementations

The harness exists in two forms because the difference between them is
the object of the experiment.

**Static** (vows as content): the vows and their glosses are placed in
the system prompt, and the model answers the task question directly. This
is how value-loading is usually done in practice, from persona prompts to
constitution-style instruction lists.

**Loop** (vows as procedure): the same system prompt, followed by a
five-turn exchange in which the model first reacts, then executes one
turn per vow as specified in Table 1, and finally answers the task
question. The model's intermediate reflections remain in context, so the
final verdict is conditioned on its own stakeholder enumeration,
self-inspection, and counter-perspectives. Nothing else changes: same
scenario, same answer format, same decoding parameters.

Any difference between the two conditions is therefore attributable to
executing the vows rather than possessing them. The loop-content
controls of Section 4.2 close the remaining gap by running the identical
procedure without the vows, so that content and procedure can be priced
separately. The full prompt texts, including all paraphrase variants,
are reproduced in Appendix A.
