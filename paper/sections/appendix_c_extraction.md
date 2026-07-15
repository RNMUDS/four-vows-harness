# Appendix C. Verdict-extraction audit

Accuracy under the naive first-pass parser vs the validated final
parser, computed on identical stored raw responses. All cells with
|delta| >= .02 are shown, sorted by |delta|; every such cell is
Gemma 3. All other models' cells moved by less than .02.
(Files named 'pilot' are the ETHICS commonsense test-split runs;
'pilot' refers to run scheduling, not a separate item sample.)

| model | benchmark | condition | n | naive | final | delta |
|---|---|---|---|---|---|---|
| Gemma 3 | MoralChoice-low | vows_static | 300 | 0.680 | 1.000 | +0.320 |
| Gemma 3 | MMLU | generic_ethics | 300 | 0.420 | 0.723 | +0.303 |
| Gemma 3 | MoralChoice-low | generic_ethics | 300 | 0.790 | 1.000 | +0.210 |
| Gemma 3 | ETHICS cm (test) | generic_ethics | 400 | 0.690 | 0.845 | +0.155 |
| Gemma 3 | MMLU | vows_static | 300 | 0.610 | 0.747 | +0.137 |
| Gemma 3 | SCRUPLES | generic_ethics | 300 | 0.560 | 0.670 | +0.110 |
| Gemma 3 | MoralChoice-low | virtue_ethics | 300 | 0.890 | 1.000 | +0.110 |
| Gemma 3 | ETHICS cm (test) | vows_static_v3 | 200 | 0.740 | 0.845 | +0.105 |
| Gemma 3 | SCRUPLES | vows_loop_v2 | 300 | 0.607 | 0.700 | +0.093 |
| Gemma 3 | ETHICS cm (test) | vows_loop_v2 | 200 | 0.765 | 0.850 | +0.085 |
| Gemma 3 | MMLU | vows_loop | 300 | 0.613 | 0.697 | +0.083 |
| Gemma 3 | ETHICS cm (hard) | generic_ethics | 300 | 0.743 | 0.823 | +0.080 |
| Gemma 3 | MMLU | baseline | 300 | 0.680 | 0.757 | +0.077 |
| Gemma 3 | ETHICS cm (test) | vows_static_v2 | 200 | 0.760 | 0.835 | +0.075 |
| Gemma 3 | ETHICS cm (test) | vows_static | 295 | 0.793 | 0.868 | +0.075 |
| Gemma 3 | SCRUPLES | virtue_loop | 300 | 0.607 | 0.680 | +0.073 |
| Gemma 3 | ETHICS cm (hard) | vows_static | 300 | 0.770 | 0.840 | +0.070 |
| Gemma 3 | ETHICS cm (hard) | vows_loop | 300 | 0.727 | 0.797 | +0.070 |
| Gemma 3 | SCRUPLES | vows_static | 300 | 0.610 | 0.670 | +0.060 |
| Gemma 3 | MoralChoice-low | vows_loop | 300 | 0.930 | 0.990 | +0.060 |
| Gemma 3 | ETHICS cm (test) | reflect_loop | 200 | 0.805 | 0.845 | +0.040 |
| Gemma 3 | MMLU | virtue_ethics | 300 | 0.683 | 0.713 | +0.030 |
| Gemma 3 | ETHICS cm (test) | virtue_ethics | 400 | 0.850 | 0.875 | +0.025 |
| Gemma 3 | SCRUPLES | vows_loop | 300 | 0.653 | 0.677 | +0.023 |
| Gemma 3 | SCRUPLES | virtue_ethics | 300 | 0.657 | 0.677 | +0.020 |
| Gemma 3 | ETHICS cm (test) | vows_loop | 200 | 0.805 | 0.825 | +0.020 |
