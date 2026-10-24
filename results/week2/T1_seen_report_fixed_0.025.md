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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week2/T1_seen_mlp | progress | 10 of 46 (5 to 16) | 21 / 15 |  | +160 (31) | 15 of 743 (0.020) | 20 of 27 | 0.028 of 472 / 0.007 of 271 |
| results/week2/T1_seen_mlp | mlp | 3 of 46 (0 to 7) | 31 / 12 | -7 (-13 to -2) | +132 (34) | 8 of 743 (0.011) | 7 of 27 | 0.006 of 472 / 0.018 of 271 |
| results/week2/T1_seen_mlp | combined | 15 of 46 (9 to 21) | 27 / 4 | +5 (-3 to +13) | +24 (42) | 101 of 743 (0.136) | 17 of 27 | 0.091 of 472 / 0.214 of 271 |
| results/week2/T1_seen_mlp | mlp_cusum | 3 of 46 (0 to 7) | 30 / 13 | -7 (-13 to -2) | +112 (33) | 5 of 743 (0.007) | 7 of 27 | 0.004 of 472 / 0.011 of 271 |
| results/week2/T1_seen_mlp | combined_cusum | 14 of 46 (8 to 20) | 28 / 4 | +4 (-4 to +12) | +24 (42) | 101 of 743 (0.136) | 18 of 27 | 0.093 of 472 / 0.210 of 271 |
| results/week2/T1_seen_mlp | mlp_phys | 11 of 46 (6 to 17) | 20 / 15 | +1 (-5 to +7) | +32 (31) | 16 of 743 (0.022) | 4 of 27 | 0.019 of 472 / 0.026 of 271 |
| results/week2/T1_seen_mlp | mlp_phys_cusum | 5 of 46 (1 to 10) | 8 / 33 | -5 (-11 to +1) | +32 (13) | 21 of 743 (0.028) | 8 of 27 | 0.028 of 472 / 0.030 of 271 |
| results/week2/T1_seen_mlp | mlp_physvla | 7 of 46 (3 to 12) | 33 / 6 | -3 (-10 to +3) | +56 (40) | 16 of 743 (0.022) | 10 of 27 | 0.013 of 472 / 0.037 of 271 |
| results/week2/T1_seen_mlp | mlp_physvla_cusum | 7 of 46 (3 to 12) | 33 / 6 | -3 (-10 to +3) | +48 (40) | 17 of 743 (0.023) | 10 of 27 | 0.015 of 472 / 0.037 of 271 |
| results/week2/T1_seen_mlp | mlp_physall | 4 of 46 (1 to 8) | 35 / 7 | -6 (-12 to +0) | +72 (39) | 15 of 743 (0.020) | 5 of 27 | 0.008 of 472 / 0.041 of 271 |
| results/week2/T1_seen_mlp | mlp_physall_cusum | 4 of 46 (1 to 8) | 34 / 8 | -6 (-12 to +0) | +72 (38) | 13 of 743 (0.017) | 5 of 27 | 0.008 of 472 / 0.033 of 271 |
| results/week2/T1_seen_gru | progress | 10 of 46 (5 to 16) | 21 / 15 |  | +160 (31) | 15 of 743 (0.020) | 20 of 27 | 0.028 of 472 / 0.007 of 271 |
| results/week2/T1_seen_gru | gru | 6 of 46 (2 to 11) | 31 / 9 | -4 (-11 to +3) | +96 (37) | 20 of 743 (0.027) | 10 of 27 | 0.017 of 472 / 0.044 of 271 |
| results/week2/T1_seen_gru | gru_cusum | 5 of 46 (1 to 9) | 32 / 9 | -5 (-12 to +1) | +104 (37) | 20 of 743 (0.027) | 11 of 27 | 0.017 of 472 / 0.044 of 271 |
| results/week2/T1_seen_gru | gru_phys | 10 of 46 (5 to 16) | 27 / 9 | +0 (-7 to +7) | +64 (37) | 14 of 743 (0.019) | 7 of 27 | 0.008 of 472 / 0.037 of 271 |
| results/week2/T1_seen_gru | gru_phys_cusum | 3 of 46 (0 to 7) | 18 / 25 | -7 (-13 to -1) | +88 (21) | 17 of 743 (0.023) | 10 of 27 | 0.015 of 472 / 0.037 of 271 |
| results/week2/T1_seen_gru | gru_physvla | 8 of 46 (3 to 13) | 27 / 11 | -2 (-9 to +5) | +80 (35) | 14 of 743 (0.019) | 4 of 27 | 0.004 of 472 / 0.044 of 271 |
| results/week2/T1_seen_gru | gru_physvla_cusum | 8 of 46 (3 to 13) | 27 / 11 | -2 (-8 to +4) | +80 (35) | 17 of 743 (0.023) | 6 of 27 | 0.008 of 472 / 0.048 of 271 |
| results/week2/T1_seen_gru | gru_physall | 9 of 46 (4 to 15) | 32 / 5 | -1 (-8 to +6) | +72 (41) | 11 of 743 (0.015) | 7 of 27 | 0.006 of 472 / 0.030 of 271 |
| results/week2/T1_seen_gru | gru_physall_cusum | 10 of 46 (5 to 16) | 31 / 5 | +0 (-7 to +7) | +64 (41) | 14 of 743 (0.019) | 13 of 27 | 0.008 of 472 / 0.037 of 271 |
| results/week2/T1_seen_conv | progress | 10 of 46 (5 to 16) | 21 / 15 |  | +160 (31) | 15 of 743 (0.020) | 20 of 27 | 0.028 of 472 / 0.007 of 271 |
| results/week2/T1_seen_conv | conv | 6 of 46 (2 to 11) | 33 / 7 | -4 (-10 to +2) | +88 (39) | 16 of 743 (0.022) | 12 of 27 | 0.008 of 472 / 0.044 of 271 |
| results/week2/T1_seen_conv | conv_cusum | 8 of 46 (3 to 13) | 32 / 6 | -2 (-9 to +5) | +76 (40) | 15 of 743 (0.020) | 13 of 27 | 0.011 of 472 / 0.037 of 271 |
| results/week2/T1_seen_conv | conv_phys | 11 of 46 (6 to 17) | 26 / 9 | +1 (-5 to +7) | +48 (37) | 17 of 743 (0.023) | 5 of 27 | 0.015 of 472 / 0.037 of 271 |
| results/week2/T1_seen_conv | conv_phys_cusum | 9 of 46 (4 to 14) | 24 / 13 | -1 (-7 to +5) | +56 (33) | 15 of 743 (0.020) | 7 of 27 | 0.013 of 472 / 0.033 of 271 |
| results/week2/T1_seen_conv | conv_physvla | 9 of 46 (4 to 14) | 31 / 6 | -1 (-8 to +6) | +56 (40) | 15 of 743 (0.020) | 8 of 27 | 0.008 of 472 / 0.041 of 271 |
| results/week2/T1_seen_conv | conv_physvla_cusum | 10 of 46 (5 to 16) | 31 / 5 | +0 (-7 to +7) | +48 (41) | 15 of 743 (0.020) | 12 of 27 | 0.008 of 472 / 0.041 of 271 |
| results/week2/T1_seen_conv | conv_physall | 10 of 46 (5 to 16) | 32 / 4 | +0 (-7 to +7) | +56 (42) | 18 of 743 (0.024) | 10 of 27 | 0.006 of 472 / 0.055 of 271 |
| results/week2/T1_seen_conv | conv_physall_cusum | 10 of 46 (5 to 16) | 32 / 4 | +0 (-7 to +7) | +48 (42) | 16 of 743 (0.022) | 12 of 27 | 0.008 of 472 / 0.044 of 271 |
