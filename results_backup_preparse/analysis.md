# Four Vows Harness — integrated analysis

Total records: 18752

# Master table
## gemma3:27b x cm_hard
  baseline         n= 300 acc=0.850 CI=[0.810,0.890] parse=1.000 refuse=0.000
  generic_ethics   n= 300 acc=0.743 CI=[0.693,0.793] parse=1.000 refuse=0.000
  virtue_ethics    n= 300 acc=0.843 CI=[0.800,0.883] parse=0.993 refuse=0.000
  vows_static      n= 300 acc=0.770 CI=[0.723,0.817] parse=1.000 refuse=0.000
  vows_loop        n= 300 acc=0.727 CI=[0.677,0.777] parse=1.000 refuse=0.000
  McNemar vows_static vs baseline: +14/-38 p=0.0012
  McNemar vows_static vs generic_ethics: +34/-26 p=0.3663
  McNemar vows_loop vs baseline: +11/-48 p=0.0000
  McNemar vows_loop vs generic_ethics: +30/-35 p=0.6201

## gemma3:27b x cm_test
  baseline         n= 200 acc=0.870 CI=[0.820,0.915] parse=1.000 refuse=0.000
  generic_ethics   n= 200 acc=0.690 CI=[0.625,0.750] parse=1.000 refuse=0.000
  virtue_ethics    n= 200 acc=0.850 CI=[0.800,0.900] parse=1.000 refuse=0.000
  vows_static      n= 200 acc=0.785 CI=[0.725,0.840] parse=1.000 refuse=0.000
  vows_loop        n= 200 acc=0.805 CI=[0.750,0.860] parse=1.000 refuse=0.000
  McNemar vows_static vs baseline: +8/-25 p=0.0046
  McNemar vows_static vs generic_ethics: +30/-11 p=0.0043
  McNemar vows_loop vs baseline: +3/-16 p=0.0044
  McNemar vows_loop vs generic_ethics: +31/-8 p=0.0003

## gemma3:27b x mc_low
  baseline         n= 300 acc=0.990 CI=[0.977,1.000] parse=1.000 refuse=0.000
  generic_ethics   n= 300 acc=0.790 CI=[0.743,0.837] parse=1.000 refuse=0.000
  virtue_ethics    n= 300 acc=0.890 CI=[0.853,0.923] parse=1.000 refuse=0.000
  vows_static      n= 300 acc=0.680 CI=[0.627,0.730] parse=1.000 refuse=0.000
  vows_loop        n= 300 acc=0.930 CI=[0.900,0.957] parse=1.000 refuse=0.000
  McNemar vows_static vs baseline: +2/-95 p=0.0000
  McNemar vows_static vs generic_ethics: +33/-66 p=0.0012
  McNemar vows_loop vs baseline: +2/-20 p=0.0001
  McNemar vows_loop vs generic_ethics: +57/-15 p=0.0000

## gemma3:27b x scruples
  baseline         n= 300 acc=0.677 CI=[0.623,0.730] parse=1.000 refuse=0.000
  generic_ethics   n= 300 acc=0.560 CI=[0.503,0.617] parse=1.000 refuse=0.000
  virtue_ethics    n= 300 acc=0.657 CI=[0.603,0.710] parse=1.000 refuse=0.000
  vows_static      n= 300 acc=0.610 CI=[0.553,0.663] parse=1.000 refuse=0.000
  vows_loop        n= 300 acc=0.653 CI=[0.600,0.707] parse=1.000 refuse=0.000
  McNemar vows_static vs baseline: +22/-42 p=0.0169
  McNemar vows_static vs generic_ethics: +75/-60 p=0.2281
  McNemar vows_loop vs baseline: +35/-42 p=0.4944
  McNemar vows_loop vs generic_ethics: +76/-48 p=0.0150

## gpt-oss:20b x cm_hard
  baseline         n= 300 acc=0.893 CI=[0.857,0.927] parse=1.000 refuse=0.000
  generic_ethics   n= 300 acc=0.887 CI=[0.850,0.920] parse=1.000 refuse=0.000
  virtue_ethics    n= 300 acc=0.757 CI=[0.707,0.803] parse=0.807 refuse=0.000
  vows_static      n= 300 acc=0.880 CI=[0.843,0.913] parse=1.000 refuse=0.000
  vows_loop        n= 300 acc=0.817 CI=[0.770,0.860] parse=1.000 refuse=0.000
  McNemar vows_static vs baseline: +9/-13 p=0.5235
  McNemar vows_static vs generic_ethics: +8/-10 p=0.8145
  McNemar vows_loop vs baseline: +14/-37 p=0.0018
  McNemar vows_loop vs generic_ethics: +16/-37 p=0.0055

## gpt-oss:20b x cm_test
  baseline         n= 200 acc=0.920 CI=[0.880,0.955] parse=1.000 refuse=0.000
  generic_ethics   n= 200 acc=0.920 CI=[0.880,0.955] parse=1.000 refuse=0.000
  virtue_ethics    n= 200 acc=0.800 CI=[0.745,0.855] parse=0.885 refuse=0.000
  vows_static      n= 200 acc=0.910 CI=[0.870,0.945] parse=1.000 refuse=0.000
  vows_loop        n= 200 acc=0.860 CI=[0.810,0.905] parse=1.000 refuse=0.000
  McNemar vows_static vs baseline: +3/-5 p=0.7266
  McNemar vows_static vs generic_ethics: +2/-4 p=0.6875
  McNemar vows_loop vs baseline: +5/-17 p=0.0169
  McNemar vows_loop vs generic_ethics: +4/-16 p=0.0118

## gpt-oss:20b x mc_low
  baseline         n= 300 acc=1.000 CI=[1.000,1.000] parse=1.000 refuse=0.000
  generic_ethics   n= 300 acc=1.000 CI=[1.000,1.000] parse=1.000 refuse=0.000
  virtue_ethics    n= 300 acc=0.957 CI=[0.933,0.977] parse=0.960 refuse=0.000
  vows_static      n= 300 acc=1.000 CI=[1.000,1.000] parse=1.000 refuse=0.000
  vows_loop        n= 300 acc=0.993 CI=[0.983,1.000] parse=1.000 refuse=0.000
  McNemar vows_static vs baseline: +0/-0 p=1.0000
  McNemar vows_static vs generic_ethics: +0/-0 p=1.0000
  McNemar vows_loop vs baseline: +0/-2 p=0.5000
  McNemar vows_loop vs generic_ethics: +0/-2 p=0.5000

## gpt-oss:20b x scruples
  baseline         n= 300 acc=0.693 CI=[0.640,0.743] parse=0.980 refuse=0.020
  generic_ethics   n= 300 acc=0.640 CI=[0.583,0.693] parse=0.960 refuse=0.040
  virtue_ethics    n= 300 acc=0.380 CI=[0.327,0.433] parse=0.543 refuse=0.030
  vows_static      n= 300 acc=0.667 CI=[0.613,0.720] parse=1.000 refuse=0.000
  vows_loop        n= 300 acc=0.713 CI=[0.663,0.763] parse=1.000 refuse=0.000
  McNemar vows_static vs baseline: +20/-28 p=0.3123
  McNemar vows_static vs generic_ethics: +32/-24 p=0.3497
  McNemar vows_loop vs baseline: +30/-24 p=0.4966
  McNemar vows_loop vs generic_ethics: +42/-20 p=0.0071

## llama3.3:70b x cm_hard
  baseline         n= 300 acc=0.907 CI=[0.873,0.937] parse=1.000 refuse=0.000
  generic_ethics   n= 300 acc=0.913 CI=[0.880,0.943] parse=1.000 refuse=0.000
  virtue_ethics    n= 300 acc=0.940 CI=[0.913,0.967] parse=1.000 refuse=0.000
  vows_static      n= 300 acc=0.897 CI=[0.860,0.930] parse=1.000 refuse=0.000
  vows_loop        n=  52 acc=0.885 CI=[0.788,0.962] parse=1.000 refuse=0.000
  McNemar vows_static vs baseline: +5/-8 p=0.5811
  McNemar vows_static vs generic_ethics: +4/-9 p=0.2668
  McNemar vows_loop vs baseline: +3/-4 p=1.0000
  McNemar vows_loop vs generic_ethics: +2/-3 p=1.0000

## llama3.3:70b x cm_test
  baseline         n= 200 acc=0.950 CI=[0.920,0.980] parse=1.000 refuse=0.000
  generic_ethics   n= 200 acc=0.930 CI=[0.895,0.965] parse=1.000 refuse=0.000
  virtue_ethics    n= 200 acc=0.945 CI=[0.910,0.975] parse=1.000 refuse=0.000
  vows_static      n= 200 acc=0.920 CI=[0.880,0.955] parse=1.000 refuse=0.000
  vows_loop        n= 200 acc=0.905 CI=[0.860,0.945] parse=1.000 refuse=0.000
  McNemar vows_static vs baseline: +2/-8 p=0.1094
  McNemar vows_static vs generic_ethics: +2/-4 p=0.6875
  McNemar vows_loop vs baseline: +5/-14 p=0.0636
  McNemar vows_loop vs generic_ethics: +7/-12 p=0.3593

## qwen3.6:latest x cm_hard
  baseline         n= 300 acc=0.923 CI=[0.893,0.950] parse=1.000 refuse=0.000
  generic_ethics   n= 300 acc=0.917 CI=[0.883,0.947] parse=1.000 refuse=0.000
  virtue_ethics    n= 300 acc=0.923 CI=[0.893,0.950] parse=1.000 refuse=0.000
  vows_static      n= 300 acc=0.907 CI=[0.873,0.937] parse=1.000 refuse=0.000
  vows_loop        n= 300 acc=0.900 CI=[0.863,0.933] parse=1.000 refuse=0.000
  McNemar vows_static vs baseline: +7/-12 p=0.3593
  McNemar vows_static vs generic_ethics: +10/-13 p=0.6776
  McNemar vows_loop vs baseline: +12/-19 p=0.2810
  McNemar vows_loop vs generic_ethics: +13/-18 p=0.4731

## qwen3.6:latest x cm_test
  baseline         n= 200 acc=0.945 CI=[0.910,0.975] parse=1.000 refuse=0.000
  generic_ethics   n= 200 acc=0.955 CI=[0.925,0.980] parse=1.000 refuse=0.000
  virtue_ethics    n= 200 acc=0.930 CI=[0.890,0.965] parse=1.000 refuse=0.000
  vows_static      n= 200 acc=0.900 CI=[0.855,0.940] parse=1.000 refuse=0.000
  vows_loop        n= 200 acc=0.895 CI=[0.850,0.935] parse=1.000 refuse=0.000
  McNemar vows_static vs baseline: +2/-11 p=0.0225
  McNemar vows_static vs generic_ethics: +0/-11 p=0.0010
  McNemar vows_loop vs baseline: +2/-12 p=0.0129
  McNemar vows_loop vs generic_ethics: +1/-13 p=0.0018

## qwen3.6:latest x mc_low
  baseline         n= 300 acc=1.000 CI=[1.000,1.000] parse=1.000 refuse=0.000
  generic_ethics   n= 300 acc=1.000 CI=[1.000,1.000] parse=1.000 refuse=0.000
  virtue_ethics    n= 300 acc=1.000 CI=[1.000,1.000] parse=1.000 refuse=0.000
  vows_static      n= 300 acc=1.000 CI=[1.000,1.000] parse=1.000 refuse=0.000
  vows_loop        n= 300 acc=1.000 CI=[1.000,1.000] parse=1.000 refuse=0.000
  McNemar vows_static vs baseline: +0/-0 p=1.0000
  McNemar vows_static vs generic_ethics: +0/-0 p=1.0000
  McNemar vows_loop vs baseline: +0/-0 p=1.0000
  McNemar vows_loop vs generic_ethics: +0/-0 p=1.0000

## qwen3.6:latest x scruples
  baseline         n= 300 acc=0.630 CI=[0.577,0.683] parse=1.000 refuse=0.000
  generic_ethics   n= 300 acc=0.590 CI=[0.533,0.643] parse=1.000 refuse=0.000
  virtue_ethics    n= 300 acc=0.657 CI=[0.603,0.710] parse=1.000 refuse=0.000
  vows_static      n= 300 acc=0.547 CI=[0.490,0.603] parse=1.000 refuse=0.000
  vows_loop        n= 300 acc=0.663 CI=[0.610,0.717] parse=0.983 refuse=0.000
  McNemar vows_static vs baseline: +32/-57 p=0.0105
  McNemar vows_static vs generic_ethics: +33/-46 p=0.1766
  McNemar vows_loop vs baseline: +50/-40 p=0.3428
  McNemar vows_loop vs generic_ethics: +59/-37 p=0.0315

# Strictness shift (binary tasks)
model | dataset | condition | over_strict | over_lenient
gemma3:27b | cm_hard | baseline         | 0.273 | 0.027
gemma3:27b | cm_hard | generic_ethics   | 0.453 | 0.060
gemma3:27b | cm_hard | virtue_ethics    | 0.233 | 0.067
gemma3:27b | cm_hard | vows_loop        | 0.493 | 0.053
gemma3:27b | cm_hard | vows_static      | 0.400 | 0.060
gemma3:27b | cm_test | baseline         | 0.230 | 0.030
gemma3:27b | cm_test | generic_ethics   | 0.520 | 0.100
gemma3:27b | cm_test | virtue_ethics    | 0.260 | 0.040
gemma3:27b | cm_test | vows_loop        | 0.380 | 0.010
gemma3:27b | cm_test | vows_static      | 0.380 | 0.050
gpt-oss:20b | cm_hard | baseline         | 0.060 | 0.153
gpt-oss:20b | cm_hard | generic_ethics   | 0.080 | 0.147
gpt-oss:20b | cm_hard | virtue_ethics    | 0.027 | 0.073
gpt-oss:20b | cm_hard | vows_loop        | 0.287 | 0.080
gpt-oss:20b | cm_hard | vows_static      | 0.133 | 0.107
gpt-oss:20b | cm_test | baseline         | 0.090 | 0.070
gpt-oss:20b | cm_test | generic_ethics   | 0.100 | 0.060
gpt-oss:20b | cm_test | virtue_ethics    | 0.120 | 0.050
gpt-oss:20b | cm_test | vows_loop        | 0.240 | 0.040
gpt-oss:20b | cm_test | vows_static      | 0.130 | 0.050
llama3.3:70b | cm_hard | baseline         | 0.133 | 0.053
llama3.3:70b | cm_hard | generic_ethics   | 0.153 | 0.020
llama3.3:70b | cm_hard | virtue_ethics    | 0.107 | 0.013
llama3.3:70b | cm_hard | vows_loop        | 0.125 | 0.100
llama3.3:70b | cm_hard | vows_static      | 0.160 | 0.047
llama3.3:70b | cm_test | baseline         | 0.090 | 0.010
llama3.3:70b | cm_test | generic_ethics   | 0.120 | 0.020
llama3.3:70b | cm_test | virtue_ethics    | 0.080 | 0.030
llama3.3:70b | cm_test | vows_loop        | 0.140 | 0.050
llama3.3:70b | cm_test | vows_static      | 0.130 | 0.030
qwen3.6:latest | cm_hard | baseline         | 0.067 | 0.087
qwen3.6:latest | cm_hard | generic_ethics   | 0.067 | 0.100
qwen3.6:latest | cm_hard | virtue_ethics    | 0.100 | 0.053
qwen3.6:latest | cm_hard | vows_loop        | 0.147 | 0.053
qwen3.6:latest | cm_hard | vows_static      | 0.093 | 0.093
qwen3.6:latest | cm_test | baseline         | 0.090 | 0.020
qwen3.6:latest | cm_test | generic_ethics   | 0.080 | 0.010
qwen3.6:latest | cm_test | virtue_ethics    | 0.120 | 0.020
qwen3.6:latest | cm_test | vows_loop        | 0.190 | 0.020
qwen3.6:latest | cm_test | vows_static      | 0.120 | 0.080

# SCRUPLES human-distribution alignment
model | condition | vote_share_all | consensus | controversial
gemma3:27b | baseline         | 0.645 | 0.838 | 0.550
gemma3:27b | generic_ethics   | 0.546 | 0.626 | 0.506
gemma3:27b | virtue_ethics    | 0.623 | 0.768 | 0.551
gemma3:27b | vows_loop        | 0.609 | 0.737 | 0.545
gemma3:27b | vows_static      | 0.605 | 0.798 | 0.510
gpt-oss:20b | baseline         | 0.661 | 0.845 | 0.570
gpt-oss:20b | generic_ethics   | 0.647 | 0.853 | 0.545
gpt-oss:20b | virtue_ethics    | 0.647 | 0.810 | 0.556
gpt-oss:20b | vows_loop        | 0.659 | 0.859 | 0.561
gpt-oss:20b | vows_static      | 0.645 | 0.859 | 0.539
qwen3.6:latest | baseline         | 0.615 | 0.768 | 0.539
qwen3.6:latest | generic_ethics   | 0.573 | 0.657 | 0.532
qwen3.6:latest | virtue_ethics    | 0.633 | 0.798 | 0.552
qwen3.6:latest | vows_loop        | 0.639 | 0.794 | 0.564
qwen3.6:latest | vows_static      | 0.551 | 0.626 | 0.514
