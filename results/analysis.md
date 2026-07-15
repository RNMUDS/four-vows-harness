# Four Vows Harness — integrated analysis

Total records: 27352

# Master table
## gemma3:27b x cm_hard
  baseline         n= 300 acc=0.853 CI=[0.813,0.893] parse=1.000 refuse=0.000
  generic_ethics   n= 300 acc=0.823 CI=[0.780,0.867] parse=1.000 refuse=0.000
  virtue_ethics    n= 300 acc=0.850 CI=[0.807,0.890] parse=0.993 refuse=0.000
  vows_static      n= 300 acc=0.840 CI=[0.797,0.880] parse=1.000 refuse=0.000
  vows_loop        n= 300 acc=0.797 CI=[0.750,0.840] parse=1.000 refuse=0.000
  McNemar vows_static vs baseline: +7/-11 p=0.4807
  McNemar vows_static vs generic_ethics: +11/-6 p=0.3323
  McNemar vows_loop vs baseline: +11/-28 p=0.0095
  McNemar vows_loop vs generic_ethics: +16/-24 p=0.2682

## gemma3:27b x cm_test
  baseline         n= 200 acc=0.870 CI=[0.820,0.915] parse=1.000 refuse=0.000
  generic_ethics   n= 200 acc=0.845 CI=[0.790,0.890] parse=1.000 refuse=0.000
  virtue_ethics    n= 200 acc=0.875 CI=[0.825,0.920] parse=1.000 refuse=0.000
  vows_static      n= 200 acc=0.870 CI=[0.820,0.915] parse=1.000 refuse=0.000
  vows_loop        n= 200 acc=0.825 CI=[0.770,0.875] parse=1.000 refuse=0.000
  McNemar vows_static vs baseline: +4/-4 p=1.0000
  McNemar vows_static vs generic_ethics: +7/-2 p=0.1797
  McNemar vows_loop vs baseline: +3/-12 p=0.0352
  McNemar vows_loop vs generic_ethics: +6/-10 p=0.4545

## gemma3:27b x mc_low
  baseline         n= 300 acc=0.990 CI=[0.977,1.000] parse=1.000 refuse=0.000
  generic_ethics   n= 300 acc=1.000 CI=[1.000,1.000] parse=1.000 refuse=0.000
  virtue_ethics    n= 300 acc=1.000 CI=[1.000,1.000] parse=1.000 refuse=0.000
  vows_static      n= 300 acc=1.000 CI=[1.000,1.000] parse=1.000 refuse=0.000
  vows_loop        n= 300 acc=0.990 CI=[0.977,1.000] parse=1.000 refuse=0.000
  McNemar vows_static vs baseline: +3/-0 p=0.2500
  McNemar vows_static vs generic_ethics: +0/-0 p=1.0000
  McNemar vows_loop vs baseline: +3/-3 p=1.0000
  McNemar vows_loop vs generic_ethics: +0/-3 p=0.2500

## gemma3:27b x scruples
  baseline         n= 300 acc=0.680 CI=[0.627,0.733] parse=1.000 refuse=0.000
  generic_ethics   n= 300 acc=0.670 CI=[0.617,0.723] parse=1.000 refuse=0.000
  virtue_ethics    n= 300 acc=0.677 CI=[0.623,0.730] parse=1.000 refuse=0.000
  vows_static      n= 300 acc=0.670 CI=[0.617,0.723] parse=1.000 refuse=0.000
  vows_loop        n= 300 acc=0.677 CI=[0.623,0.730] parse=1.000 refuse=0.000
  McNemar vows_static vs baseline: +16/-19 p=0.7359
  McNemar vows_static vs generic_ethics: +18/-18 p=1.0000
  McNemar vows_loop vs baseline: +31/-32 p=1.0000
  McNemar vows_loop vs generic_ethics: +30/-28 p=0.8957

## gemma3:27b x unknown
  baseline         n= 300 acc=0.757 CI=[0.707,0.803] parse=0.997 refuse=0.000
  generic_ethics   n= 300 acc=0.723 CI=[0.673,0.773] parse=1.000 refuse=0.003
  virtue_ethics    n= 300 acc=0.713 CI=[0.660,0.763] parse=1.000 refuse=0.000
  vows_static      n= 300 acc=0.747 CI=[0.697,0.797] parse=1.000 refuse=0.000
  vows_loop        n= 300 acc=0.697 CI=[0.643,0.747] parse=0.993 refuse=0.007
  McNemar vows_static vs baseline: +19/-22 p=0.7552
  McNemar vows_static vs generic_ethics: +22/-15 p=0.3240
  McNemar vows_loop vs baseline: +24/-42 p=0.0356
  McNemar vows_loop vs generic_ethics: +28/-36 p=0.3817

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

## qwen3.6:latest x unknown
  baseline         n= 300 acc=0.830 CI=[0.787,0.870] parse=0.997 refuse=0.000
  generic_ethics   n= 300 acc=0.803 CI=[0.757,0.847] parse=0.993 refuse=0.000
  virtue_ethics    n= 300 acc=0.857 CI=[0.817,0.893] parse=0.997 refuse=0.000
  vows_static      n= 300 acc=0.823 CI=[0.780,0.863] parse=0.993 refuse=0.000
  vows_loop        n= 300 acc=0.817 CI=[0.773,0.860] parse=0.997 refuse=0.007
  McNemar vows_static vs baseline: +11/-13 p=0.8388
  McNemar vows_static vs generic_ethics: +18/-12 p=0.3616
  McNemar vows_loop vs baseline: +18/-22 p=0.6358
  McNemar vows_loop vs generic_ethics: +19/-15 p=0.6076

# Strictness shift (binary tasks)
model | dataset | condition | over_strict | over_lenient
gemma3:27b | cm_hard | baseline         | 0.267 | 0.027
gemma3:27b | cm_hard | generic_ethics   | 0.327 | 0.027
gemma3:27b | cm_hard | virtue_ethics    | 0.213 | 0.073
gemma3:27b | cm_hard | vows_loop        | 0.327 | 0.080
gemma3:27b | cm_hard | vows_static      | 0.287 | 0.033
gemma3:27b | cm_test | baseline         | 0.230 | 0.030
gemma3:27b | cm_test | generic_ethics   | 0.290 | 0.020
gemma3:27b | cm_test | reflect_loop     | 0.290 | 0.020
gemma3:27b | cm_test | virtue_ethics    | 0.210 | 0.040
gemma3:27b | cm_test | virtue_loop      | 0.290 | 0.030
gemma3:27b | cm_test | vows_loop        | 0.300 | 0.050
gemma3:27b | cm_test | vows_loop_v2     | 0.260 | 0.040
gemma3:27b | cm_test | vows_static      | 0.230 | 0.030
gemma3:27b | cm_test | vows_static_v2   | 0.310 | 0.020
gemma3:27b | cm_test | vows_static_v3   | 0.280 | 0.030
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
qwen3.6:latest | cm_test | reflect_loop     | 0.210 | 0.020
qwen3.6:latest | cm_test | virtue_ethics    | 0.120 | 0.020
qwen3.6:latest | cm_test | virtue_loop      | 0.230 | 0.020
qwen3.6:latest | cm_test | vows_loop        | 0.190 | 0.020
qwen3.6:latest | cm_test | vows_loop_v2     | 0.160 | 0.040
qwen3.6:latest | cm_test | vows_static      | 0.120 | 0.080
qwen3.6:latest | cm_test | vows_static_v2   | 0.110 | 0.060
qwen3.6:latest | cm_test | vows_static_v3   | 0.120 | 0.050

# SCRUPLES human-distribution alignment
model | condition | vote_share_all | consensus | controversial
gemma3:27b | baseline         | 0.650 | 0.848 | 0.552
gemma3:27b | generic_ethics   | 0.641 | 0.848 | 0.539
gemma3:27b | reflect_loop     | 0.665 | 0.869 | 0.565
gemma3:27b | virtue_ethics    | 0.647 | 0.838 | 0.552
gemma3:27b | virtue_loop      | 0.647 | 0.848 | 0.548
gemma3:27b | vows_loop        | 0.640 | 0.818 | 0.552
gemma3:27b | vows_loop_v2     | 0.657 | 0.859 | 0.557
gemma3:27b | vows_static      | 0.649 | 0.869 | 0.541
gemma3:27b | vows_static_v2   | 0.625 | 0.798 | 0.540
gemma3:27b | vows_static_v3   | 0.627 | 0.788 | 0.548
gpt-oss:20b | baseline         | 0.661 | 0.845 | 0.570
gpt-oss:20b | generic_ethics   | 0.647 | 0.853 | 0.545
gpt-oss:20b | reflect_loop     | 0.666 | 0.875 | 0.565
gpt-oss:20b | virtue_ethics    | 0.647 | 0.810 | 0.556
gpt-oss:20b | virtue_loop      | 0.658 | 0.859 | 0.559
gpt-oss:20b | vows_loop        | 0.659 | 0.859 | 0.561
gpt-oss:20b | vows_static      | 0.645 | 0.859 | 0.539
qwen3.6:latest | baseline         | 0.615 | 0.768 | 0.539
qwen3.6:latest | generic_ethics   | 0.573 | 0.657 | 0.532
qwen3.6:latest | reflect_loop     | 0.655 | 0.837 | 0.566
qwen3.6:latest | virtue_ethics    | 0.633 | 0.798 | 0.552
qwen3.6:latest | virtue_loop      | 0.646 | 0.818 | 0.561
qwen3.6:latest | vows_loop        | 0.639 | 0.794 | 0.564
qwen3.6:latest | vows_loop_v2     | 0.654 | 0.832 | 0.565
qwen3.6:latest | vows_static      | 0.551 | 0.626 | 0.514
qwen3.6:latest | vows_static_v2   | 0.578 | 0.677 | 0.529
qwen3.6:latest | vows_static_v3   | 0.599 | 0.737 | 0.531
