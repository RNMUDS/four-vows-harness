# 7. Limitations

**The vow translation is ours.** The mapping from doctrine to prompt
(the English rendering of the vows, the glossing of the three poisons as
sycophancy, dismissiveness, and overconfidence, and the ordering of the
loop) was made by the authors without doctrinal authority. Paraphrase
robustness (Appendix B) shows the results do not hang on our particular
wording, but a rendering endorsed by Buddhist scholars or practitioners
could differ in substance, not merely phrasing, and might behave
differently.

**One cultural anchor.** All benchmarks are in English and labelled by
US or English-speaking-community annotators. Our claims are accordingly
about divergence *from that anchor*, not about fidelity to Buddhist
moral judgment, which we did not measure. The decisive test, whether
vow-conditioned models track annotators from Buddhist cultural spheres
better than baseline, remains to be run.

**Models and precision.** Four models from four families, all
instruction-tuned and 4-bit quantized, evaluated at temperature 0. The
loop's benefit was model-dependent: significant on Qwen, positive but
not significant on Gemma, and absent on GPT-OSS; on Gemma the loop also
carried a small significant MMLU cost. The dissociation we
report is a pattern across models, not a law of each. Quantization and greedy decoding match
deployment practice for local models but may not transfer to full-
precision or sampled settings. Llama 3.3 70B lacks MoralChoice, SCRUPLES, and MMLU data entirely, and
its hard-split vow-loop cell was curtailed (n = 52) because its
per-item deliberation cost was prohibitive on our hardware; GPT-OSS
lacks MMLU. Section 4's design-coverage paragraph states exactly which
cells exist. Llama's evidence accordingly bears on the static
conditions primarily.

**Benchmark scope.** Three moral benchmarks and one capability control,
each with 200-300 sampled items per condition. MoralChoice's
low-ambiguity split saturated for every model, so it functions here
only as a negative control. SCRUPLES
inherits the demographics and norms of its source community; its
"human distribution" is one crowd's, not humanity's.

**Prompted values, not learned ones.** Everything here operates in
context. Whether the content/procedure dissociation survives fine-tuning,
with creeds reproducing the static harms while deliberations preserve
the gains, is an open question that our
released loop transcripts make testable.
