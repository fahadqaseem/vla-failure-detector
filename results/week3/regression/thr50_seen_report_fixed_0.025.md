# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/week3_reg/thr50/seen | progress | 0.046 | -144 (61) | 16 of 81 (9 to 23) | 0.026 | -180 (44) | 11 of 81 (5 to 17) |
| data/week3_reg/thr50/seen | gru_phys | 0.051 | -48 (75) | 23 of 81 (15 to 31) | 0.024 | -64 (73) | 19 of 81 (12 to 27) |
| data/week3_reg/thr50/seen | gru_phys_frac | 0.049 | -56 (77) | 19 of 81 (12 to 27) | 0.026 | -64 (70) | 17 of 81 (10 to 24) |
| data/week3_reg/thr50/seen | gru_phys_ttp | 0.049 | -56 (76) | 18 of 81 (11 to 26) | 0.025 | -64 (69) | 17 of 81 (10 to 24) |
| data/week3_reg/thr50/seen | gru_robot | 0.044 | -84 (74) | 17 of 81 (10 to 24) | 0.021 | -120 (66) | 11 of 81 (5 to 17) |
| data/week3_reg/thr50/seen | gru_robotobj1 | 0.042 | -92 (72) | 16 of 81 (9 to 23) | 0.022 | -124 (66) | 9 of 81 (4 to 15) |
| data/week3_reg/thr50/seen | gru_robotobj2 | 0.045 | -80 (73) | 17 of 81 (10 to 24) | 0.023 | -124 (68) | 10 of 81 (5 to 16) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/week3_reg/thr50/seen | progress | 11 of 81 (5 to 17) | 33 / 37 |  | +180 (44) | 28 of 1071 (0.026) | 22 of 31 | 0.032 of 472 / 0.022 of 599 |
| data/week3_reg/thr50/seen | gru_phys | 19 of 81 (12 to 27) | 54 / 8 | +8 (-1 to +16) | +64 (73) | 26 of 1071 (0.024) | 10 of 31 | 0.015 of 472 / 0.032 of 599 |
| data/week3_reg/thr50/seen | gru_phys_frac | 17 of 81 (10 to 24) | 53 / 11 | +6 (-2 to +14) | +64 (70) | 28 of 1071 (0.026) | 12 of 31 | 0.013 of 472 / 0.037 of 599 |
| data/week3_reg/thr50/seen | gru_phys_ttp | 17 of 81 (10 to 24) | 52 / 12 | +6 (-2 to +14) | +64 (69) | 27 of 1071 (0.025) | 10 of 31 | 0.013 of 472 / 0.035 of 599 |
| data/week3_reg/thr50/seen | gru_robot | 11 of 81 (5 to 17) | 55 / 15 | +0 (-7 to +7) | +120 (66) | 22 of 1071 (0.021) | 9 of 31 | 0.015 of 472 / 0.025 of 599 |
| data/week3_reg/thr50/seen | gru_robotobj1 | 9 of 81 (4 to 15) | 57 / 15 | -2 (-9 to +5) | +124 (66) | 24 of 1071 (0.022) | 14 of 31 | 0.006 of 472 / 0.035 of 599 |
| data/week3_reg/thr50/seen | gru_robotobj2 | 10 of 81 (5 to 16) | 58 / 13 | -1 (-9 to +6) | +124 (68) | 25 of 1071 (0.023) | 12 of 31 | 0.008 of 472 / 0.035 of 599 |
