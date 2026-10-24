# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| results/week2/T1_unseen_mlp | progress | 0.048 | -128 (36) | 11 of 46 (6 to 17) | 0.023 | -160 (30) | 10 of 46 (5 to 16) |
| results/week2/T1_unseen_mlp | mlp | 0.133 | -76 (16) | 5 of 46 (1 to 9) | 0.121 | -132 (14) | 1 of 46 (0 to 3) |
| results/week2/T1_unseen_mlp | combined | 0.116 | -80 (23) | 6 of 46 (2 to 11) | 0.071 | -80 (16) | 5 of 46 (1 to 10) |
| results/week2/T1_unseen_mlp | mlp_cusum | 0.030 | -104 (31) | 6 of 46 (2 to 11) | 0.012 | -136 (29) | 3 of 46 (0 to 7) |
| results/week2/T1_unseen_mlp | combined_cusum | 0.036 | -124 (32) | 8 of 46 (3 to 13) | 0.024 | -208 (25) | 4 of 46 (1 to 8) |
| results/week2/T1_unseen_mlp | mlp_phys | 0.040 | -112 (19) | 3 of 46 (0 to 7) | 0.012 | -116 (18) | 3 of 46 (0 to 7) |
| results/week2/T1_unseen_mlp | mlp_phys_cusum | 0.106 | -40 (8) | 3 of 46 (0 to 7) | 0.101 | -48 (7) | 2 of 46 (0 to 5) |
| results/week2/T1_unseen_mlp | mlp_physvla | 0.164 | -48 (37) | 16 of 46 (10 to 22) | 0.105 | -80 (35) | 12 of 46 (7 to 18) |
| results/week2/T1_unseen_mlp | mlp_physvla_cusum | 0.109 | -48 (38) | 11 of 46 (6 to 17) | 0.069 | -72 (37) | 9 of 46 (4 to 14) |
| results/week2/T1_unseen_mlp | mlp_physall | 0.133 | -132 (22) | 5 of 46 (1 to 10) | 0.124 | -128 (21) | 5 of 46 (1 to 10) |
| results/week2/T1_unseen_mlp | mlp_physall_cusum | 0.042 | -84 (30) | 4 of 46 (1 to 8) | 0.015 | -112 (27) | 4 of 46 (1 to 8) |
| results/week2/T1_unseen_gru | progress | 0.048 | -128 (36) | 11 of 46 (6 to 17) | 0.023 | -160 (30) | 10 of 46 (5 to 16) |
| results/week2/T1_unseen_gru | gru | 0.090 | -80 (35) | 12 of 46 (6 to 18) | 0.034 | -96 (33) | 11 of 46 (6 to 17) |
| results/week2/T1_unseen_gru | gru_cusum | 0.077 | -96 (32) | 11 of 46 (6 to 17) | 0.046 | -84 (26) | 10 of 46 (5 to 16) |
| results/week2/T1_unseen_gru | gru_phys | 0.112 | +12 (26) | 14 of 46 (8 to 20) | 0.086 | +12 (26) | 14 of 46 (8 to 20) |
| results/week2/T1_unseen_gru | gru_phys_cusum | 0.067 | -120 (13) | 2 of 46 (0 to 5) | 0.059 | -124 (12) | 2 of 46 (0 to 5) |
| results/week2/T1_unseen_gru | gru_physvla | 0.082 | -84 (30) | 10 of 46 (5 to 16) | 0.047 | -88 (29) | 10 of 46 (5 to 16) |
| results/week2/T1_unseen_gru | gru_physvla_cusum | 0.143 | -72 (28) | 10 of 46 (5 to 16) | 0.129 | -72 (27) | 9 of 46 (4 to 15) |
| results/week2/T1_unseen_gru | gru_physall | 0.034 | -88 (36) | 8 of 46 (3 to 13) | 0.019 | -104 (35) | 8 of 46 (3 to 13) |
| results/week2/T1_unseen_gru | gru_physall_cusum | 0.127 | -72 (35) | 10 of 46 (5 to 16) | 0.117 | -80 (31) | 8 of 46 (3 to 13) |
| results/week2/T1_unseen_conv | progress | 0.048 | -128 (36) | 11 of 46 (6 to 17) | 0.023 | -160 (30) | 10 of 46 (5 to 16) |
| results/week2/T1_unseen_conv | conv | 0.117 | -112 (34) | 8 of 46 (3 to 13) | 0.052 | -128 (29) | 5 of 46 (1 to 9) |
| results/week2/T1_unseen_conv | conv_cusum | 0.078 | -88 (35) | 12 of 46 (6 to 18) | 0.043 | -76 (30) | 12 of 46 (6 to 18) |
| results/week2/T1_unseen_conv | conv_phys | 0.000 | +96 (4) | 2 of 46 (0 to 5) | 0.000 | +192 (3) | 2 of 46 (0 to 5) |
| results/week2/T1_unseen_conv | conv_phys_cusum | 0.003 | -40 (1) | 0 of 46 (0 to 0) | 0.003 | -56 (1) | 0 of 46 (0 to 0) |
| results/week2/T1_unseen_conv | conv_physvla | 0.052 | -124 (36) | 9 of 46 (4 to 14) | 0.020 | -128 (32) | 7 of 46 (3 to 12) |
| results/week2/T1_unseen_conv | conv_physvla_cusum | 0.102 | -80 (37) | 10 of 46 (5 to 16) | 0.077 | -112 (31) | 8 of 46 (3 to 13) |
| results/week2/T1_unseen_conv | conv_physall | 0.039 | -88 (41) | 11 of 46 (6 to 17) | 0.022 | -112 (37) | 9 of 46 (4 to 15) |
| results/week2/T1_unseen_conv | conv_physall_cusum | 0.070 | -80 (39) | 10 of 46 (5 to 16) | 0.047 | -88 (37) | 7 of 46 (3 to 12) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week2/T1_unseen_mlp | progress | 11 of 46 (6 to 17) | 25 / 10 |  | +128 (36) | 36 of 743 (0.048) | 23 of 27 | 0.049 of 472 / 0.048 of 271 |
| results/week2/T1_unseen_mlp | mlp | 5 of 46 (1 to 9) | 11 / 30 | -6 (-13 to +1) | +76 (16) | 99 of 743 (0.133) | 7 of 27 | 0.108 of 472 / 0.177 of 271 |
| results/week2/T1_unseen_mlp | combined | 6 of 46 (2 to 11) | 17 / 23 | -5 (-12 to +2) | +80 (23) | 86 of 743 (0.116) | 4 of 27 | 0.085 of 472 / 0.170 of 271 |
| results/week2/T1_unseen_mlp | mlp_cusum | 6 of 46 (2 to 11) | 25 / 15 | -5 (-11 to +1) | +104 (31) | 22 of 743 (0.030) | 12 of 27 | 0.023 of 472 / 0.041 of 271 |
| results/week2/T1_unseen_mlp | combined_cusum | 8 of 46 (3 to 13) | 24 / 14 | -3 (-9 to +3) | +124 (32) | 27 of 743 (0.036) | 4 of 27 | 0.019 of 472 / 0.066 of 271 |
| results/week2/T1_unseen_mlp | mlp_phys | 3 of 46 (0 to 7) | 16 / 27 | -8 (-15 to -1) | +112 (19) | 30 of 743 (0.040) | 4 of 27 | 0.030 of 472 / 0.059 of 271 |
| results/week2/T1_unseen_mlp | mlp_phys_cusum | 3 of 46 (0 to 7) | 5 / 38 | -8 (-14 to -2) | +40 (8) | 79 of 743 (0.106) | 15 of 27 | 0.083 of 472 / 0.148 of 271 |
| results/week2/T1_unseen_mlp | mlp_physvla | 16 of 46 (10 to 22) | 21 / 9 | +5 (-3 to +13) | +48 (37) | 122 of 743 (0.164) | 11 of 27 | 0.119 of 472 / 0.244 of 271 |
| results/week2/T1_unseen_mlp | mlp_physvla_cusum | 11 of 46 (6 to 17) | 27 / 8 | +0 (-7 to +7) | +48 (38) | 81 of 743 (0.109) | 13 of 27 | 0.083 of 472 / 0.155 of 271 |
| results/week2/T1_unseen_mlp | mlp_physall | 5 of 46 (1 to 10) | 17 / 24 | -6 (-13 to +1) | +132 (22) | 99 of 743 (0.133) | 7 of 27 | 0.104 of 472 / 0.185 of 271 |
| results/week2/T1_unseen_mlp | mlp_physall_cusum | 4 of 46 (1 to 8) | 26 / 16 | -7 (-13 to -1) | +84 (30) | 31 of 743 (0.042) | 11 of 27 | 0.038 of 472 / 0.048 of 271 |
| results/week2/T1_unseen_gru | progress | 11 of 46 (6 to 17) | 25 / 10 |  | +128 (36) | 36 of 743 (0.048) | 23 of 27 | 0.049 of 472 / 0.048 of 271 |
| results/week2/T1_unseen_gru | gru | 12 of 46 (6 to 18) | 23 / 11 | +1 (-5 to +7) | +80 (35) | 67 of 743 (0.090) | 9 of 27 | 0.061 of 472 / 0.140 of 271 |
| results/week2/T1_unseen_gru | gru_cusum | 11 of 46 (6 to 17) | 21 / 14 | +0 (-5 to +5) | +96 (32) | 57 of 743 (0.077) | 8 of 27 | 0.064 of 472 / 0.100 of 271 |
| results/week2/T1_unseen_gru | gru_phys | 14 of 46 (8 to 20) | 12 / 20 | +3 (-4 to +10) | -12 (26) | 83 of 743 (0.112) | 6 of 27 | 0.093 of 472 / 0.144 of 271 |
| results/week2/T1_unseen_gru | gru_phys_cusum | 2 of 46 (0 to 5) | 11 / 33 | -9 (-15 to -3) | +120 (13) | 50 of 743 (0.067) | 1 of 27 | 0.104 of 472 / 0.004 of 271 |
| results/week2/T1_unseen_gru | gru_physvla | 10 of 46 (5 to 16) | 20 / 16 | -1 (-7 to +5) | +84 (30) | 61 of 743 (0.082) | 1 of 27 | 0.059 of 472 / 0.122 of 271 |
| results/week2/T1_unseen_gru | gru_physvla_cusum | 10 of 46 (5 to 16) | 18 / 18 | -1 (-7 to +5) | +72 (28) | 106 of 743 (0.143) | 2 of 27 | 0.133 of 472 / 0.159 of 271 |
| results/week2/T1_unseen_gru | gru_physall | 8 of 46 (3 to 13) | 28 / 10 | -3 (-9 to +3) | +88 (36) | 25 of 743 (0.034) | 8 of 27 | 0.015 of 472 / 0.066 of 271 |
| results/week2/T1_unseen_gru | gru_physall_cusum | 10 of 46 (5 to 16) | 25 / 11 | -1 (-7 to +5) | +72 (35) | 94 of 743 (0.127) | 7 of 27 | 0.121 of 472 / 0.137 of 271 |
| results/week2/T1_unseen_conv | progress | 11 of 46 (6 to 17) | 25 / 10 |  | +128 (36) | 36 of 743 (0.048) | 23 of 27 | 0.049 of 472 / 0.048 of 271 |
| results/week2/T1_unseen_conv | conv | 8 of 46 (3 to 13) | 26 / 12 | -3 (-9 to +3) | +112 (34) | 87 of 743 (0.117) | 10 of 27 | 0.085 of 472 / 0.173 of 271 |
| results/week2/T1_unseen_conv | conv_cusum | 12 of 46 (6 to 18) | 23 / 11 | +1 (-5 to +7) | +88 (35) | 58 of 743 (0.078) | 16 of 27 | 0.072 of 472 / 0.089 of 271 |
| results/week2/T1_unseen_conv | conv_phys | 2 of 46 (0 to 5) | 2 / 42 | -9 (-14 to -4) | -96 (4) | 0 of 743 (0.000) | 0 of 27 | 0.000 of 472 / 0.000 of 271 |
| results/week2/T1_unseen_conv | conv_phys_cusum | 0 of 46 (0 to 0) | 1 / 45 | -11 (-17 to -6) | +40 (1) | 2 of 743 (0.003) | 0 of 27 | 0.000 of 472 / 0.007 of 271 |
| results/week2/T1_unseen_conv | conv_physvla | 9 of 46 (4 to 15) | 27 / 10 | -2 (-9 to +5) | +124 (36) | 39 of 743 (0.052) | 5 of 27 | 0.025 of 472 / 0.100 of 271 |
| results/week2/T1_unseen_conv | conv_physvla_cusum | 10 of 46 (5 to 16) | 27 / 9 | -1 (-7 to +5) | +80 (37) | 76 of 743 (0.102) | 8 of 27 | 0.083 of 472 / 0.137 of 271 |
| results/week2/T1_unseen_conv | conv_physall | 11 of 46 (6 to 17) | 30 / 5 | +0 (-6 to +6) | +88 (41) | 29 of 743 (0.039) | 8 of 27 | 0.006 of 472 / 0.096 of 271 |
| results/week2/T1_unseen_conv | conv_physall_cusum | 10 of 46 (5 to 16) | 29 / 7 | -1 (-7 to +5) | +80 (39) | 52 of 743 (0.070) | 10 of 27 | 0.049 of 472 / 0.107 of 271 |
