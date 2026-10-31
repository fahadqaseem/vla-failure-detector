# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| results/week3/baselines/seen | timer | 0.040 | -248 (81) | 7 of 81 (3 to 12) | 0.019 | -264 (81) | 7 of 81 (3 to 12) |
| results/week3/baselines/seen | progress | 0.046 | -144 (61) | 16 of 81 (9 to 23) | 0.026 | -180 (44) | 11 of 81 (5 to 17) |
| results/week3/baselines/seen | safe | 0.049 | -60 (80) | 22 of 81 (14 to 30) | 0.021 | -80 (79) | 18 of 81 (11 to 26) |
| results/week3/baselines/seen | hideseek | 0.223 | -64 (80) | 26 of 81 (18 to 34) | 0.218 | -80 (79) | 23 of 81 (15 to 31) |
| results/week2/T1all_seen_gru | progress | 0.046 | -144 (61) | 16 of 81 (9 to 23) | 0.026 | -180 (44) | 11 of 81 (5 to 17) |
| results/week2/T1all_seen_gru | gru_phys | 0.053 | -48 (75) | 23 of 81 (15 to 31) | 0.023 | -64 (73) | 19 of 81 (12 to 27) |
| results/week2/T1all_seen_gru | gru_phys_cusum | 0.049 | -56 (61) | 17 of 81 (10 to 25) | 0.021 | -72 (48) | 10 of 81 (5 to 16) |
| results/week2/T1all_seen_gru | gru_physvla | 0.044 | -68 (74) | 19 of 81 (12 to 27) | 0.021 | -96 (69) | 10 of 81 (5 to 16) |
| results/week2/T1all_seen_gru | gru_physvla_cusum | 0.039 | -64 (72) | 16 of 81 (9 to 23) | 0.021 | -88 (68) | 10 of 81 (5 to 16) |
| results/week2/T1all_seen_conv | progress | 0.046 | -144 (61) | 16 of 81 (9 to 23) | 0.026 | -180 (44) | 11 of 81 (5 to 17) |
| results/week2/T1all_seen_conv | conv_phys | 0.049 | -48 (76) | 23 of 81 (15 to 31) | 0.021 | -64 (73) | 18 of 81 (11 to 25) |
| results/week2/T1all_seen_conv | conv_phys_cusum | 0.046 | -40 (68) | 22 of 81 (14 to 30) | 0.026 | -64 (62) | 12 of 81 (6 to 19) |
| results/week2/T1all_seen_conv | conv_physvla | 0.046 | -48 (74) | 25 of 81 (17 to 33) | 0.023 | -72 (72) | 9 of 81 (4 to 15) |
| results/week2/T1all_seen_conv | conv_physvla_cusum | 0.051 | -48 (76) | 22 of 81 (14 to 30) | 0.021 | -72 (71) | 12 of 81 (6 to 19) |
| results/week2/T1all_seen_conv | conv_physall | 0.049 | -48 (76) | 23 of 81 (15 to 31) | 0.020 | -72 (73) | 11 of 81 (5 to 17) |
| results/week2/T1all_seen_conv | conv_physall_cusum | 0.055 | -48 (76) | 22 of 81 (14 to 30) | 0.021 | -64 (70) | 12 of 81 (6 to 18) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week3/baselines/seen | timer | 7 of 81 (3 to 12) | 74 / 0 | -9 (-16 to -2) | +248 (81) | 43 of 1071 (0.040) | 31 of 31 | 0.036 of 472 / 0.043 of 599 |
| results/week3/baselines/seen | progress | 16 of 81 (9 to 23) | 45 / 20 |  | +144 (61) | 49 of 1071 (0.046) | 26 of 31 | 0.049 of 472 / 0.043 of 599 |
| results/week3/baselines/seen | safe | 22 of 81 (15 to 30) | 58 / 1 | +6 (-3 to +14) | +60 (80) | 53 of 1071 (0.049) | 26 of 31 | 0.028 of 472 / 0.067 of 599 |
| results/week3/baselines/seen | hideseek | 26 of 81 (18 to 34) | 54 / 1 | +10 (+2 to +19) | +64 (80) | 239 of 1071 (0.223) | 30 of 31 | 0.225 of 472 / 0.222 of 599 |
| results/week2/T1all_seen_gru | progress | 16 of 81 (9 to 23) | 45 / 20 |  | +144 (61) | 49 of 1071 (0.046) | 26 of 31 | 0.049 of 472 / 0.043 of 599 |
| results/week2/T1all_seen_gru | gru_phys | 23 of 81 (15 to 31) | 52 / 6 | +7 (-2 to +16) | +48 (75) | 57 of 1071 (0.053) | 14 of 31 | 0.032 of 472 / 0.070 of 599 |
| results/week2/T1all_seen_gru | gru_phys_cusum | 17 of 81 (10 to 24) | 44 / 20 | +1 (-7 to +9) | +56 (61) | 53 of 1071 (0.049) | 17 of 31 | 0.038 of 472 / 0.058 of 599 |
| results/week2/T1all_seen_gru | gru_physvla | 19 of 81 (12 to 27) | 55 / 7 | +3 (-5 to +12) | +68 (74) | 47 of 1071 (0.044) | 13 of 31 | 0.021 of 472 / 0.062 of 599 |
| results/week2/T1all_seen_gru | gru_physvla_cusum | 16 of 81 (9 to 23) | 56 / 9 | +0 (-8 to +8) | +64 (72) | 42 of 1071 (0.039) | 13 of 31 | 0.019 of 472 / 0.055 of 599 |
| results/week2/T1all_seen_conv | progress | 16 of 81 (9 to 23) | 45 / 20 |  | +144 (61) | 49 of 1071 (0.046) | 26 of 31 | 0.049 of 472 / 0.043 of 599 |
| results/week2/T1all_seen_conv | conv_phys | 23 of 81 (15 to 31) | 53 / 5 | +7 (-2 to +16) | +48 (76) | 52 of 1071 (0.049) | 14 of 31 | 0.023 of 472 / 0.068 of 599 |
| results/week2/T1all_seen_conv | conv_phys_cusum | 22 of 81 (14 to 30) | 46 / 13 | +6 (-3 to +14) | +40 (68) | 49 of 1071 (0.046) | 14 of 31 | 0.023 of 472 / 0.063 of 599 |
| results/week2/T1all_seen_conv | conv_physvla | 25 of 81 (17 to 33) | 49 / 7 | +9 (-1 to +19) | +48 (74) | 49 of 1071 (0.046) | 19 of 31 | 0.015 of 472 / 0.070 of 599 |
| results/week2/T1all_seen_conv | conv_physvla_cusum | 22 of 81 (14 to 30) | 54 / 5 | +6 (-3 to +15) | +48 (76) | 55 of 1071 (0.051) | 22 of 31 | 0.021 of 472 / 0.075 of 599 |
| results/week2/T1all_seen_conv | conv_physall | 23 of 81 (15 to 31) | 53 / 5 | +7 (-2 to +17) | +48 (76) | 52 of 1071 (0.049) | 18 of 31 | 0.017 of 472 / 0.073 of 599 |
| results/week2/T1all_seen_conv | conv_physall_cusum | 22 of 81 (14 to 30) | 54 / 5 | +6 (-3 to +15) | +48 (76) | 59 of 1071 (0.055) | 21 of 31 | 0.017 of 472 / 0.085 of 599 |
