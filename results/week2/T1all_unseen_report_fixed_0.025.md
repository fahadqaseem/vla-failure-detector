# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| results/week2/T1all_unseen_gru | progress | 0.048 | -144 (61) | 17 of 81 (10 to 24) | 0.025 | -200 (43) | 11 of 81 (5 to 17) |
| results/week2/T1all_unseen_gru | gru_phys | 0.014 | -112 (44) | 12 of 81 (6 to 18) | 0.013 | -136 (43) | 10 of 81 (5 to 16) |
| results/week2/T1all_unseen_gru | gru_phys_cusum | 0.118 | -128 (28) | 4 of 81 (1 to 8) | 0.044 | -136 (24) | 3 of 81 (0 to 7) |
| results/week2/T1all_unseen_gru | gru_physvla | 0.164 | -104 (51) | 10 of 81 (5 to 16) | 0.162 | -104 (48) | 10 of 81 (5 to 16) |
| results/week2/T1all_unseen_gru | gru_physvla_cusum | 0.162 | -100 (42) | 6 of 81 (2 to 11) | 0.161 | -112 (39) | 4 of 81 (1 to 8) |
| results/week2/T1all_unseen_conv | progress | 0.048 | -144 (61) | 17 of 81 (10 to 24) | 0.025 | -200 (43) | 11 of 81 (5 to 17) |
| results/week2/T1all_unseen_conv | conv_phys | 0.000 | -104 (3) | 0 of 81 (0 to 0) | 0.000 | -112 (3) | 0 of 81 (0 to 0) |
| results/week2/T1all_unseen_conv | conv_phys_cusum | 0.000 | -168 (3) | 0 of 81 (0 to 0) | 0.000 | -176 (3) | 0 of 81 (0 to 0) |
| results/week2/T1all_unseen_conv | conv_physvla | 0.147 | -96 (61) | 12 of 81 (6 to 18) | 0.106 | -128 (53) | 7 of 81 (3 to 12) |
| results/week2/T1all_unseen_conv | conv_physvla_cusum | 0.169 | -84 (48) | 8 of 81 (3 to 14) | 0.153 | -104 (45) | 8 of 81 (3 to 14) |
| results/week2/T1all_unseen_conv | conv_physall | 0.043 | -100 (66) | 12 of 81 (6 to 18) | 0.023 | -112 (59) | 7 of 81 (2 to 12) |
| results/week2/T1all_unseen_conv | conv_physall_cusum | 0.147 | -80 (55) | 13 of 81 (7 to 20) | 0.104 | -88 (49) | 10 of 81 (5 to 16) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week2/T1all_unseen_gru | progress | 11 of 81 (5 to 17) | 32 / 38 |  | +200 (43) | 27 of 1071 (0.025) | 22 of 31 | 0.030 of 472 / 0.022 of 599 |
| results/week2/T1all_unseen_gru | gru_phys | 10 of 81 (5 to 16) | 33 / 38 | -1 (-9 to +7) | +136 (43) | 14 of 1071 (0.013) | 2 of 31 | 0.000 of 472 / 0.023 of 599 |
| results/week2/T1all_unseen_gru | gru_phys_cusum | 3 of 81 (0 to 7) | 21 / 57 | -8 (-15 to -1) | +136 (24) | 47 of 1071 (0.044) | 2 of 31 | 0.089 of 472 / 0.008 of 599 |
| results/week2/T1all_unseen_gru | gru_physvla | 10 of 81 (5 to 16) | 38 / 33 | -1 (-8 to +6) | +104 (48) | 173 of 1071 (0.162) | 0 of 31 | 0.104 of 472 / 0.207 of 599 |
| results/week2/T1all_unseen_gru | gru_physvla_cusum | 4 of 81 (1 to 8) | 35 / 42 | -7 (-13 to -1) | +112 (39) | 172 of 1071 (0.161) | 0 of 31 | 0.106 of 472 / 0.204 of 599 |
| results/week2/T1all_unseen_conv | progress | 11 of 81 (5 to 17) | 32 / 38 |  | +200 (43) | 27 of 1071 (0.025) | 22 of 31 | 0.030 of 472 / 0.022 of 599 |
| results/week2/T1all_unseen_conv | conv_phys | 0 of 81 (0 to 0) | 3 / 78 | -11 (-17 to -5) | +112 (3) | 0 of 1071 (0.000) | 0 of 31 | 0.000 of 472 / 0.000 of 599 |
| results/week2/T1all_unseen_conv | conv_phys_cusum | 0 of 81 (0 to 0) | 3 / 78 | -11 (-17 to -5) | +176 (3) | 0 of 1071 (0.000) | 0 of 31 | 0.000 of 472 / 0.000 of 599 |
| results/week2/T1all_unseen_conv | conv_physvla | 7 of 81 (3 to 12) | 46 / 28 | -4 (-12 to +4) | +128 (53) | 113 of 1071 (0.106) | 4 of 31 | 0.055 of 472 / 0.145 of 599 |
| results/week2/T1all_unseen_conv | conv_physvla_cusum | 8 of 81 (3 to 14) | 37 / 36 | -3 (-10 to +5) | +104 (45) | 164 of 1071 (0.153) | 9 of 31 | 0.102 of 472 / 0.194 of 599 |
| results/week2/T1all_unseen_conv | conv_physall | 7 of 81 (3 to 12) | 52 / 22 | -4 (-10 to +2) | +112 (59) | 25 of 1071 (0.023) | 7 of 31 | 0.002 of 472 / 0.040 of 599 |
| results/week2/T1all_unseen_conv | conv_physall_cusum | 10 of 81 (5 to 16) | 39 / 32 | -1 (-7 to +5) | +88 (49) | 111 of 1071 (0.104) | 7 of 31 | 0.055 of 472 / 0.142 of 599 |
