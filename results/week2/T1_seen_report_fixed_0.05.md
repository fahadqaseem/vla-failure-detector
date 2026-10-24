# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| results/week2/T1_seen_mlp | progress | 0.046 | -124 (38) | 11 of 46 (6 to 17) | 0.020 | -160 (31) | 10 of 46 (5 to 16) |
| results/week2/T1_seen_mlp | mlp | 0.026 | -84 (38) | 4 of 46 (1 to 8) | 0.011 | -132 (34) | 3 of 46 (0 to 7) |
| results/week2/T1_seen_mlp | combined | 0.205 | -16 (42) | 19 of 46 (13 to 26) | 0.136 | -24 (42) | 15 of 46 (9 to 21) |
| results/week2/T1_seen_mlp | mlp_cusum | 0.022 | -84 (38) | 5 of 46 (1 to 9) | 0.007 | -112 (33) | 3 of 46 (0 to 7) |
| results/week2/T1_seen_mlp | combined_cusum | 0.203 | -16 (42) | 17 of 46 (11 to 24) | 0.136 | -24 (42) | 14 of 46 (8 to 20) |
| results/week2/T1_seen_mlp | mlp_phys | 0.059 | -16 (35) | 14 of 46 (8 to 20) | 0.022 | -32 (31) | 11 of 46 (6 to 17) |
| results/week2/T1_seen_mlp | mlp_phys_cusum | 0.051 | -32 (26) | 9 of 46 (4 to 14) | 0.028 | -32 (13) | 5 of 46 (1 to 10) |
| results/week2/T1_seen_mlp | mlp_physvla | 0.046 | -32 (41) | 13 of 46 (7 to 19) | 0.022 | -56 (40) | 7 of 46 (3 to 12) |
| results/week2/T1_seen_mlp | mlp_physvla_cusum | 0.047 | -32 (41) | 11 of 46 (6 to 17) | 0.023 | -48 (40) | 7 of 46 (3 to 12) |
| results/week2/T1_seen_mlp | mlp_physall | 0.042 | -40 (42) | 8 of 46 (3 to 13) | 0.020 | -72 (39) | 4 of 46 (1 to 8) |
| results/week2/T1_seen_mlp | mlp_physall_cusum | 0.040 | -40 (42) | 8 of 46 (3 to 13) | 0.017 | -72 (38) | 4 of 46 (1 to 8) |
| results/week2/T1_seen_gru | progress | 0.046 | -124 (38) | 11 of 46 (6 to 17) | 0.020 | -160 (31) | 10 of 46 (5 to 16) |
| results/week2/T1_seen_gru | gru | 0.052 | -64 (40) | 11 of 46 (6 to 17) | 0.027 | -96 (37) | 6 of 46 (2 to 11) |
| results/week2/T1_seen_gru | gru_cusum | 0.048 | -64 (39) | 9 of 46 (4 to 14) | 0.027 | -104 (37) | 5 of 46 (1 to 9) |
| results/week2/T1_seen_gru | gru_phys | 0.035 | -48 (38) | 13 of 46 (7 to 19) | 0.019 | -64 (37) | 10 of 46 (5 to 16) |
| results/week2/T1_seen_gru | gru_phys_cusum | 0.048 | -40 (39) | 14 of 46 (8 to 20) | 0.023 | -88 (21) | 3 of 46 (0 to 7) |
| results/week2/T1_seen_gru | gru_physvla | 0.038 | -56 (42) | 14 of 46 (8 to 20) | 0.019 | -80 (35) | 8 of 46 (3 to 13) |
| results/week2/T1_seen_gru | gru_physvla_cusum | 0.050 | -52 (42) | 12 of 46 (6 to 18) | 0.023 | -80 (35) | 8 of 46 (3 to 13) |
| results/week2/T1_seen_gru | gru_physall | 0.044 | -52 (42) | 14 of 46 (8 to 20) | 0.015 | -72 (41) | 9 of 46 (4 to 15) |
| results/week2/T1_seen_gru | gru_physall_cusum | 0.054 | -64 (43) | 12 of 46 (6 to 18) | 0.019 | -64 (41) | 10 of 46 (5 to 15) |
| results/week2/T1_seen_conv | progress | 0.046 | -124 (38) | 11 of 46 (6 to 17) | 0.020 | -160 (31) | 10 of 46 (5 to 16) |
| results/week2/T1_seen_conv | conv | 0.050 | -48 (40) | 10 of 46 (5 to 16) | 0.022 | -88 (39) | 6 of 46 (2 to 11) |
| results/week2/T1_seen_conv | conv_cusum | 0.054 | -48 (40) | 10 of 46 (5 to 16) | 0.020 | -76 (40) | 8 of 46 (3 to 13) |
| results/week2/T1_seen_conv | conv_phys | 0.048 | -40 (39) | 14 of 46 (8 to 20) | 0.023 | -48 (37) | 11 of 46 (6 to 17) |
| results/week2/T1_seen_conv | conv_phys_cusum | 0.052 | -32 (38) | 14 of 46 (8 to 20) | 0.020 | -56 (33) | 9 of 46 (4 to 14) |
| results/week2/T1_seen_conv | conv_physvla | 0.046 | -32 (42) | 17 of 46 (11 to 23) | 0.020 | -56 (40) | 9 of 46 (4 to 14) |
| results/week2/T1_seen_conv | conv_physvla_cusum | 0.050 | -40 (42) | 14 of 46 (8 to 20) | 0.020 | -48 (41) | 10 of 46 (5 to 16) |
| results/week2/T1_seen_conv | conv_physall | 0.044 | -36 (44) | 17 of 46 (11 to 23) | 0.024 | -56 (42) | 10 of 46 (5 to 16) |
| results/week2/T1_seen_conv | conv_physall_cusum | 0.054 | -32 (45) | 15 of 46 (9 to 21) | 0.022 | -48 (42) | 10 of 46 (5 to 16) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week2/T1_seen_mlp | progress | 11 of 46 (6 to 17) | 27 / 8 |  | +124 (38) | 34 of 743 (0.046) | 23 of 27 | 0.047 of 472 / 0.044 of 271 |
| results/week2/T1_seen_mlp | mlp | 4 of 46 (1 to 8) | 34 / 8 | -7 (-13 to -1) | +84 (38) | 19 of 743 (0.026) | 7 of 27 | 0.013 of 472 / 0.048 of 271 |
| results/week2/T1_seen_mlp | combined | 19 of 46 (13 to 26) | 23 / 4 | +8 (-1 to +16) | +16 (42) | 152 of 743 (0.205) | 18 of 27 | 0.148 of 472 / 0.303 of 271 |
| results/week2/T1_seen_mlp | mlp_cusum | 5 of 46 (1 to 9) | 33 / 8 | -6 (-12 to +0) | +84 (38) | 16 of 743 (0.022) | 9 of 27 | 0.013 of 472 / 0.037 of 271 |
| results/week2/T1_seen_mlp | combined_cusum | 17 of 46 (11 to 24) | 25 / 4 | +6 (-2 to +14) | +16 (42) | 151 of 743 (0.203) | 18 of 27 | 0.148 of 472 / 0.299 of 271 |
| results/week2/T1_seen_mlp | mlp_phys | 14 of 46 (8 to 20) | 21 / 11 | +3 (-4 to +10) | +16 (35) | 44 of 743 (0.059) | 10 of 27 | 0.044 of 472 / 0.085 of 271 |
| results/week2/T1_seen_mlp | mlp_phys_cusum | 9 of 46 (4 to 14) | 17 / 20 | -2 (-9 to +5) | +32 (26) | 38 of 743 (0.051) | 15 of 27 | 0.044 of 472 / 0.063 of 271 |
| results/week2/T1_seen_mlp | mlp_physvla | 13 of 46 (7 to 19) | 28 / 5 | +2 (-6 to +10) | +32 (41) | 34 of 743 (0.046) | 14 of 27 | 0.023 of 472 / 0.085 of 271 |
| results/week2/T1_seen_mlp | mlp_physvla_cusum | 11 of 46 (6 to 17) | 30 / 5 | +0 (-7 to +7) | +32 (41) | 35 of 743 (0.047) | 15 of 27 | 0.028 of 472 / 0.081 of 271 |
| results/week2/T1_seen_mlp | mlp_physall | 8 of 46 (3 to 13) | 34 / 4 | -3 (-10 to +4) | +40 (42) | 31 of 743 (0.042) | 13 of 27 | 0.017 of 472 / 0.085 of 271 |
| results/week2/T1_seen_mlp | mlp_physall_cusum | 8 of 46 (3 to 13) | 34 / 4 | -3 (-10 to +4) | +40 (42) | 30 of 743 (0.040) | 13 of 27 | 0.015 of 472 / 0.085 of 271 |
| results/week2/T1_seen_gru | progress | 11 of 46 (6 to 17) | 27 / 8 |  | +124 (38) | 34 of 743 (0.046) | 23 of 27 | 0.047 of 472 / 0.044 of 271 |
| results/week2/T1_seen_gru | gru | 11 of 46 (6 to 17) | 29 / 6 | +0 (-8 to +8) | +64 (40) | 39 of 743 (0.052) | 13 of 27 | 0.028 of 472 / 0.096 of 271 |
| results/week2/T1_seen_gru | gru_cusum | 9 of 46 (4 to 15) | 30 / 7 | -2 (-9 to +5) | +64 (39) | 36 of 743 (0.048) | 15 of 27 | 0.028 of 472 / 0.085 of 271 |
| results/week2/T1_seen_gru | gru_phys | 13 of 46 (7 to 19) | 25 / 8 | +2 (-5 to +9) | +48 (38) | 26 of 743 (0.035) | 9 of 27 | 0.019 of 472 / 0.063 of 271 |
| results/week2/T1_seen_gru | gru_phys_cusum | 14 of 46 (8 to 20) | 25 / 7 | +3 (-3 to +9) | +40 (39) | 36 of 743 (0.048) | 13 of 27 | 0.030 of 472 / 0.081 of 271 |
| results/week2/T1_seen_gru | gru_physvla | 14 of 46 (8 to 20) | 28 / 4 | +3 (-3 to +9) | +56 (42) | 28 of 743 (0.038) | 7 of 27 | 0.017 of 472 / 0.074 of 271 |
| results/week2/T1_seen_gru | gru_physvla_cusum | 12 of 46 (7 to 18) | 30 / 4 | +1 (-6 to +7) | +52 (42) | 37 of 743 (0.050) | 9 of 27 | 0.028 of 472 / 0.089 of 271 |
| results/week2/T1_seen_gru | gru_physall | 14 of 46 (8 to 20) | 28 / 4 | +3 (-5 to +11) | +52 (42) | 33 of 743 (0.044) | 14 of 27 | 0.021 of 472 / 0.085 of 271 |
| results/week2/T1_seen_gru | gru_physall_cusum | 12 of 46 (7 to 18) | 31 / 3 | +1 (-5 to +7) | +64 (43) | 40 of 743 (0.054) | 15 of 27 | 0.032 of 472 / 0.092 of 271 |
| results/week2/T1_seen_conv | progress | 11 of 46 (6 to 17) | 27 / 8 |  | +124 (38) | 34 of 743 (0.046) | 23 of 27 | 0.047 of 472 / 0.044 of 271 |
| results/week2/T1_seen_conv | conv | 10 of 46 (5 to 16) | 30 / 6 | -1 (-9 to +7) | +48 (40) | 37 of 743 (0.050) | 14 of 27 | 0.021 of 472 / 0.100 of 271 |
| results/week2/T1_seen_conv | conv_cusum | 10 of 46 (5 to 16) | 30 / 6 | -1 (-9 to +7) | +48 (40) | 40 of 743 (0.054) | 15 of 27 | 0.025 of 472 / 0.103 of 271 |
| results/week2/T1_seen_conv | conv_phys | 14 of 46 (8 to 20) | 25 / 7 | +3 (-3 to +9) | +40 (39) | 36 of 743 (0.048) | 6 of 27 | 0.025 of 472 / 0.089 of 271 |
| results/week2/T1_seen_conv | conv_phys_cusum | 14 of 46 (8 to 20) | 24 / 8 | +3 (-2 to +8) | +32 (38) | 39 of 743 (0.052) | 13 of 27 | 0.028 of 472 / 0.096 of 271 |
| results/week2/T1_seen_conv | conv_physvla | 17 of 46 (11 to 23) | 25 / 4 | +6 (-1 to +13) | +32 (42) | 34 of 743 (0.046) | 12 of 27 | 0.019 of 472 / 0.092 of 271 |
| results/week2/T1_seen_conv | conv_physvla_cusum | 14 of 46 (8 to 20) | 28 / 4 | +3 (-4 to +10) | +40 (42) | 37 of 743 (0.050) | 17 of 27 | 0.021 of 472 / 0.100 of 271 |
| results/week2/T1_seen_conv | conv_physall | 17 of 46 (11 to 24) | 27 / 2 | +6 (-1 to +14) | +36 (44) | 33 of 743 (0.044) | 16 of 27 | 0.017 of 472 / 0.092 of 271 |
| results/week2/T1_seen_conv | conv_physall_cusum | 15 of 46 (9 to 21) | 30 / 1 | +4 (-3 to +11) | +32 (45) | 40 of 743 (0.054) | 17 of 27 | 0.032 of 472 / 0.092 of 271 |
