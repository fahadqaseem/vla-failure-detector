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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week2/T1_unseen_mlp | progress | 10 of 46 (5 to 16) | 20 / 16 |  | +160 (30) | 17 of 743 (0.023) | 20 of 27 | 0.025 of 472 / 0.018 of 271 |
| results/week2/T1_unseen_mlp | mlp | 1 of 46 (0 to 3) | 13 / 32 | -9 (-15 to -3) | +132 (14) | 90 of 743 (0.121) | 4 of 27 | 0.095 of 472 / 0.166 of 271 |
| results/week2/T1_unseen_mlp | combined | 5 of 46 (1 to 9) | 11 / 30 | -5 (-12 to +2) | +80 (16) | 53 of 743 (0.071) | 2 of 27 | 0.040 of 472 / 0.125 of 271 |
| results/week2/T1_unseen_mlp | mlp_cusum | 3 of 46 (0 to 7) | 26 / 17 | -7 (-13 to -1) | +136 (29) | 9 of 743 (0.012) | 8 of 27 | 0.011 of 472 / 0.015 of 271 |
| results/week2/T1_unseen_mlp | combined_cusum | 4 of 46 (1 to 8) | 21 / 21 | -6 (-13 to +0) | +208 (25) | 18 of 743 (0.024) | 1 of 27 | 0.013 of 472 / 0.044 of 271 |
| results/week2/T1_unseen_mlp | mlp_phys | 3 of 46 (0 to 7) | 15 / 28 | -7 (-14 to +0) | +116 (18) | 9 of 743 (0.012) | 1 of 27 | 0.008 of 472 / 0.018 of 271 |
| results/week2/T1_unseen_mlp | mlp_phys_cusum | 2 of 46 (0 to 5) | 5 / 39 | -8 (-14 to -3) | +48 (7) | 75 of 743 (0.101) | 15 of 27 | 0.074 of 472 / 0.148 of 271 |
| results/week2/T1_unseen_mlp | mlp_physvla | 12 of 46 (6 to 18) | 23 / 11 | +2 (-6 to +10) | +80 (35) | 78 of 743 (0.105) | 11 of 27 | 0.059 of 472 / 0.185 of 271 |
| results/week2/T1_unseen_mlp | mlp_physvla_cusum | 9 of 46 (4 to 15) | 28 / 9 | -1 (-7 to +5) | +72 (37) | 51 of 743 (0.069) | 12 of 27 | 0.055 of 472 / 0.092 of 271 |
| results/week2/T1_unseen_mlp | mlp_physall | 5 of 46 (1 to 10) | 16 / 25 | -5 (-12 to +2) | +128 (21) | 92 of 743 (0.124) | 6 of 27 | 0.095 of 472 / 0.173 of 271 |
| results/week2/T1_unseen_mlp | mlp_physall_cusum | 4 of 46 (1 to 8) | 23 / 19 | -6 (-12 to +0) | +112 (27) | 11 of 743 (0.015) | 9 of 27 | 0.008 of 472 / 0.026 of 271 |
| results/week2/T1_unseen_gru | progress | 10 of 46 (5 to 16) | 20 / 16 |  | +160 (30) | 17 of 743 (0.023) | 20 of 27 | 0.025 of 472 / 0.018 of 271 |
| results/week2/T1_unseen_gru | gru | 11 of 46 (6 to 17) | 22 / 13 | +1 (-5 to +7) | +96 (33) | 25 of 743 (0.034) | 6 of 27 | 0.030 of 472 / 0.041 of 271 |
| results/week2/T1_unseen_gru | gru_cusum | 10 of 46 (5 to 16) | 16 / 20 | +0 (-5 to +5) | +84 (26) | 34 of 743 (0.046) | 7 of 27 | 0.040 of 472 / 0.055 of 271 |
| results/week2/T1_unseen_gru | gru_phys | 14 of 46 (8 to 20) | 12 / 20 | +4 (-2 to +11) | -12 (26) | 64 of 743 (0.086) | 6 of 27 | 0.076 of 472 / 0.103 of 271 |
| results/week2/T1_unseen_gru | gru_phys_cusum | 2 of 46 (0 to 5) | 10 / 34 | -8 (-14 to -3) | +124 (12) | 44 of 743 (0.059) | 1 of 27 | 0.091 of 472 / 0.004 of 271 |
| results/week2/T1_unseen_gru | gru_physvla | 10 of 46 (5 to 16) | 19 / 17 | +0 (-6 to +5) | +88 (29) | 35 of 743 (0.047) | 1 of 27 | 0.034 of 472 / 0.070 of 271 |
| results/week2/T1_unseen_gru | gru_physvla_cusum | 9 of 46 (4 to 15) | 18 / 19 | -1 (-6 to +4) | +72 (27) | 96 of 743 (0.129) | 0 of 27 | 0.125 of 472 / 0.137 of 271 |
| results/week2/T1_unseen_gru | gru_physall | 8 of 46 (3 to 13) | 27 / 11 | -2 (-8 to +4) | +104 (35) | 14 of 743 (0.019) | 3 of 27 | 0.008 of 472 / 0.037 of 271 |
| results/week2/T1_unseen_gru | gru_physall_cusum | 8 of 46 (3 to 13) | 23 / 15 | -2 (-8 to +3) | +80 (31) | 87 of 743 (0.117) | 3 of 27 | 0.110 of 472 / 0.129 of 271 |
| results/week2/T1_unseen_conv | progress | 10 of 46 (5 to 16) | 20 / 16 |  | +160 (30) | 17 of 743 (0.023) | 20 of 27 | 0.025 of 472 / 0.018 of 271 |
| results/week2/T1_unseen_conv | conv | 5 of 46 (1 to 10) | 24 / 17 | -5 (-10 to +0) | +128 (29) | 39 of 743 (0.052) | 8 of 27 | 0.019 of 472 / 0.111 of 271 |
| results/week2/T1_unseen_conv | conv_cusum | 12 of 46 (6 to 18) | 18 / 16 | +2 (-4 to +8) | +76 (30) | 32 of 743 (0.043) | 12 of 27 | 0.036 of 472 / 0.055 of 271 |
| results/week2/T1_unseen_conv | conv_phys | 2 of 46 (0 to 5) | 1 / 43 | -8 (-13 to -3) | -192 (3) | 0 of 743 (0.000) | 0 of 27 | 0.000 of 472 / 0.000 of 271 |
| results/week2/T1_unseen_conv | conv_phys_cusum | 0 of 46 (0 to 0) | 1 / 45 | -10 (-16 to -5) | +56 (1) | 2 of 743 (0.003) | 0 of 27 | 0.000 of 472 / 0.007 of 271 |
| results/week2/T1_unseen_conv | conv_physvla | 7 of 46 (3 to 12) | 25 / 14 | -3 (-9 to +3) | +128 (32) | 15 of 743 (0.020) | 5 of 27 | 0.004 of 472 / 0.048 of 271 |
| results/week2/T1_unseen_conv | conv_physvla_cusum | 8 of 46 (3 to 13) | 23 / 15 | -2 (-7 to +3) | +112 (31) | 57 of 743 (0.077) | 7 of 27 | 0.066 of 472 / 0.096 of 271 |
| results/week2/T1_unseen_conv | conv_physall | 9 of 46 (4 to 15) | 28 / 9 | -1 (-6 to +4) | +112 (37) | 16 of 743 (0.022) | 6 of 27 | 0.002 of 472 / 0.055 of 271 |
| results/week2/T1_unseen_conv | conv_physall_cusum | 7 of 46 (3 to 12) | 30 / 9 | -3 (-8 to +1) | +88 (37) | 35 of 743 (0.047) | 8 of 27 | 0.032 of 472 / 0.074 of 271 |
