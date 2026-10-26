# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week2/T1all_seen_gru | progress | 11 of 81 (5 to 17) | 33 / 37 |  | +180 (44) | 28 of 1071 (0.026) | 22 of 31 | 0.032 of 472 / 0.022 of 599 |
| results/week2/T1all_seen_gru | gru_phys | 19 of 81 (12 to 27) | 54 / 8 | +8 (-1 to +16) | +64 (73) | 25 of 1071 (0.023) | 10 of 31 | 0.013 of 472 / 0.032 of 599 |
| results/week2/T1all_seen_gru | gru_phys_cusum | 10 of 81 (5 to 16) | 38 / 33 | -1 (-9 to +7) | +72 (48) | 23 of 1071 (0.021) | 12 of 31 | 0.019 of 472 / 0.023 of 599 |
| results/week2/T1all_seen_gru | gru_physvla | 10 of 81 (5 to 16) | 59 / 12 | -1 (-9 to +6) | +96 (69) | 22 of 1071 (0.021) | 9 of 31 | 0.006 of 472 / 0.032 of 599 |
| results/week2/T1all_seen_gru | gru_physvla_cusum | 10 of 81 (5 to 16) | 58 / 13 | -1 (-8 to +6) | +88 (68) | 22 of 1071 (0.021) | 10 of 31 | 0.008 of 472 / 0.030 of 599 |
| results/week2/T1all_seen_conv | progress | 11 of 81 (5 to 17) | 33 / 37 |  | +180 (44) | 28 of 1071 (0.026) | 22 of 31 | 0.032 of 472 / 0.022 of 599 |
| results/week2/T1all_seen_conv | conv_phys | 18 of 81 (11 to 26) | 55 / 8 | +7 (-1 to +15) | +64 (73) | 22 of 1071 (0.021) | 8 of 31 | 0.008 of 472 / 0.030 of 599 |
| results/week2/T1all_seen_conv | conv_phys_cusum | 12 of 81 (6 to 18) | 50 / 19 | +1 (-7 to +9) | +64 (62) | 28 of 1071 (0.026) | 12 of 31 | 0.017 of 472 / 0.033 of 599 |
| results/week2/T1all_seen_conv | conv_physvla | 9 of 81 (4 to 15) | 63 / 9 | -2 (-9 to +5) | +72 (72) | 25 of 1071 (0.023) | 10 of 31 | 0.006 of 472 / 0.037 of 599 |
| results/week2/T1all_seen_conv | conv_physvla_cusum | 12 of 81 (6 to 19) | 59 / 10 | +1 (-6 to +8) | +72 (71) | 22 of 1071 (0.021) | 12 of 31 | 0.006 of 472 / 0.032 of 599 |
| results/week2/T1all_seen_conv | conv_physall | 11 of 81 (5 to 17) | 62 / 8 | +0 (-7 to +7) | +72 (73) | 21 of 1071 (0.020) | 11 of 31 | 0.008 of 472 / 0.028 of 599 |
| results/week2/T1all_seen_conv | conv_physall_cusum | 12 of 81 (6 to 19) | 58 / 11 | +1 (-7 to +9) | +64 (70) | 22 of 1071 (0.021) | 14 of 31 | 0.008 of 472 / 0.030 of 599 |
