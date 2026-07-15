# Appendix B. Robustness: paraphrase and loop-content controls

Over-strict: P(pred=WRONG | gold=ACCEPTABLE); over-lenient: the
converse. Choice tasks have no strictness decomposition.

### B.1 Qwen 3.6 x ETHICS commonsense (test split)

| condition | n | accuracy | over-strict | over-lenient |
|---|---|---|---|---|
| baseline | 200 | 0.945 | 0.090 | 0.020 |
| generic_ethics | 200 | 0.955 | 0.080 | 0.010 |
| virtue_ethics | 200 | 0.930 | 0.120 | 0.020 |
| vows_static | 200 | 0.900 | 0.120 | 0.080 |
| vows_static_v2 | 200 | 0.915 | 0.110 | 0.060 |
| vows_static_v3 | 200 | 0.915 | 0.120 | 0.050 |
| vows_loop | 200 | 0.895 | 0.190 | 0.020 |
| vows_loop_v2 | 200 | 0.900 | 0.160 | 0.040 |
| reflect_loop | 200 | 0.885 | 0.210 | 0.020 |
| virtue_loop | 200 | 0.875 | 0.230 | 0.020 |

### B.2 Qwen 3.6 x ETHICS commonsense (hard split)

| condition | n | accuracy | over-strict | over-lenient |
|---|---|---|---|---|
| baseline | 300 | 0.923 | 0.067 | 0.087 |
| generic_ethics | 300 | 0.917 | 0.067 | 0.100 |
| virtue_ethics | 300 | 0.923 | 0.100 | 0.053 |
| vows_static | 300 | 0.907 | 0.093 | 0.093 |
| vows_loop | 300 | 0.900 | 0.147 | 0.053 |

### B.3 Qwen 3.6 x SCRUPLES

| condition | n | accuracy | over-strict | over-lenient |
|---|---|---|---|---|
| baseline | 300 | 0.630 | — | — |
| generic_ethics | 300 | 0.590 | — | — |
| virtue_ethics | 300 | 0.657 | — | — |
| vows_static | 300 | 0.547 | — | — |
| vows_static_v2 | 300 | 0.587 | — | — |
| vows_static_v3 | 300 | 0.607 | — | — |
| vows_loop | 300 | 0.663 | — | — |
| vows_loop_v2 | 300 | 0.667 | — | — |
| reflect_loop | 300 | 0.707 | — | — |
| virtue_loop | 300 | 0.683 | — | — |

### B.4 Gemma 3 x ETHICS commonsense (test split)

| condition | n | accuracy | over-strict | over-lenient |
|---|---|---|---|---|
| baseline | 200 | 0.870 | 0.230 | 0.030 |
| generic_ethics | 200 | 0.845 | 0.290 | 0.020 |
| virtue_ethics | 200 | 0.875 | 0.210 | 0.040 |
| vows_static | 200 | 0.870 | 0.230 | 0.030 |
| vows_static_v2 | 200 | 0.835 | 0.310 | 0.020 |
| vows_static_v3 | 200 | 0.845 | 0.280 | 0.030 |
| vows_loop | 200 | 0.825 | 0.300 | 0.050 |
| vows_loop_v2 | 200 | 0.850 | 0.260 | 0.040 |
| reflect_loop | 200 | 0.845 | 0.290 | 0.020 |
| virtue_loop | 200 | 0.840 | 0.290 | 0.030 |

### B.5 Gemma 3 x ETHICS commonsense (hard split)

| condition | n | accuracy | over-strict | over-lenient |
|---|---|---|---|---|
| baseline | 300 | 0.853 | 0.267 | 0.027 |
| generic_ethics | 300 | 0.823 | 0.327 | 0.027 |
| virtue_ethics | 300 | 0.850 | 0.213 | 0.073 |
| vows_static | 300 | 0.840 | 0.287 | 0.033 |
| vows_loop | 300 | 0.797 | 0.327 | 0.080 |

### B.6 Gemma 3 x SCRUPLES

| condition | n | accuracy | over-strict | over-lenient |
|---|---|---|---|---|
| baseline | 300 | 0.680 | — | — |
| generic_ethics | 300 | 0.670 | — | — |
| virtue_ethics | 300 | 0.677 | — | — |
| vows_static | 300 | 0.670 | — | — |
| vows_static_v2 | 300 | 0.637 | — | — |
| vows_static_v3 | 300 | 0.633 | — | — |
| vows_loop | 300 | 0.677 | — | — |
| vows_loop_v2 | 300 | 0.700 | — | — |
| reflect_loop | 300 | 0.703 | — | — |
| virtue_loop | 300 | 0.680 | — | — |

### B.7 GPT-OSS x ETHICS commonsense (hard split)

| condition | n | accuracy | over-strict | over-lenient |
|---|---|---|---|---|
| baseline | 300 | 0.893 | 0.060 | 0.153 |
| generic_ethics | 300 | 0.887 | 0.080 | 0.147 |
| virtue_ethics | 300 | 0.757 | 0.027 | 0.073 |
| vows_static | 300 | 0.880 | 0.133 | 0.107 |
| vows_loop | 300 | 0.817 | 0.287 | 0.080 |

### B.8 GPT-OSS x SCRUPLES (loop-content controls)

| condition | n | accuracy | over-strict | over-lenient |
|---|---|---|---|---|
| baseline | 300 | 0.693 | — | — |
| generic_ethics | 300 | 0.640 | — | — |
| virtue_ethics | 300 | 0.380 | — | — |
| vows_static | 300 | 0.667 | — | — |
| vows_loop | 300 | 0.713 | — | — |
| reflect_loop | 300 | 0.690 | — | — |
| virtue_loop | 300 | 0.700 | — | — |

### B.9 SCRUPLES human vote-share alignment

Mean share of the five annotator votes received by the chosen option,
over parsed responses; consensus = not flagged controversial.

| model | condition | n | all | consensus (n) | controversial (n) |
|---|---|---|---|---|---|
| Qwen 3.6 | baseline | 300 | 0.615 | 0.768 (99) | 0.539 (201) |
| Qwen 3.6 | generic_ethics | 300 | 0.573 | 0.657 (99) | 0.532 (201) |
| Qwen 3.6 | virtue_ethics | 300 | 0.633 | 0.798 (99) | 0.552 (201) |
| Qwen 3.6 | vows_static | 300 | 0.551 | 0.626 (99) | 0.514 (201) |
| Qwen 3.6 | vows_loop | 295 | 0.639 | 0.794 (97) | 0.564 (198) |
| Qwen 3.6 | reflect_loop | 299 | 0.655 | 0.837 (98) | 0.566 (201) |
| Qwen 3.6 | virtue_loop | 299 | 0.646 | 0.818 (99) | 0.561 (200) |
| Gemma 3 | baseline | 300 | 0.650 | 0.848 (99) | 0.552 (201) |
| Gemma 3 | generic_ethics | 300 | 0.641 | 0.848 (99) | 0.539 (201) |
| Gemma 3 | virtue_ethics | 300 | 0.647 | 0.838 (99) | 0.552 (201) |
| Gemma 3 | vows_static | 300 | 0.649 | 0.869 (99) | 0.541 (201) |
| Gemma 3 | vows_loop | 300 | 0.640 | 0.818 (99) | 0.552 (201) |
| Gemma 3 | reflect_loop | 300 | 0.665 | 0.869 (99) | 0.565 (201) |
| Gemma 3 | virtue_loop | 300 | 0.647 | 0.848 (99) | 0.548 (201) |
| GPT-OSS | baseline | 294 | 0.661 | 0.845 (97) | 0.570 (197) |
| GPT-OSS | generic_ethics | 288 | 0.647 | 0.853 (95) | 0.545 (193) |
| GPT-OSS | virtue_ethics | 163 | 0.647 | 0.810 (58) | 0.556 (105) |
| GPT-OSS | vows_static | 300 | 0.645 | 0.859 (99) | 0.539 (201) |
| GPT-OSS | vows_loop | 300 | 0.659 | 0.859 (99) | 0.561 (201) |
| GPT-OSS | reflect_loop | 294 | 0.666 | 0.875 (96) | 0.565 (198) |
| GPT-OSS | virtue_loop | 300 | 0.658 | 0.859 (99) | 0.559 (201) |
