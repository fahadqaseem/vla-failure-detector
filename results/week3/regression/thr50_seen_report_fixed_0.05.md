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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/week3_reg/thr50/seen | progress | 16 of 81 (9 to 23) | 45 / 20 |  | +144 (61) | 49 of 1071 (0.046) | 26 of 31 | 0.049 of 472 / 0.043 of 599 |
| data/week3_reg/thr50/seen | gru_phys | 23 of 81 (15 to 31) | 52 / 6 | +7 (-2 to +16) | +48 (75) | 55 of 1071 (0.051) | 15 of 31 | 0.032 of 472 / 0.067 of 599 |
| data/week3_reg/thr50/seen | gru_phys_frac | 19 of 81 (12 to 27) | 58 / 4 | +3 (-5 to +11) | +56 (77) | 52 of 1071 (0.049) | 23 of 31 | 0.030 of 472 / 0.063 of 599 |
| data/week3_reg/thr50/seen | gru_phys_ttp | 18 of 81 (11 to 25) | 58 / 5 | +2 (-6 to +10) | +56 (76) | 52 of 1071 (0.049) | 18 of 31 | 0.034 of 472 / 0.060 of 599 |
| data/week3_reg/thr50/seen | gru_robot | 17 of 81 (10 to 25) | 57 / 7 | +1 (-7 to +9) | +84 (74) | 47 of 1071 (0.044) | 14 of 31 | 0.019 of 472 / 0.063 of 599 |
| data/week3_reg/thr50/seen | gru_robotobj1 | 16 of 81 (9 to 23) | 56 / 9 | +0 (-8 to +8) | +92 (72) | 45 of 1071 (0.042) | 19 of 31 | 0.021 of 472 / 0.058 of 599 |
| data/week3_reg/thr50/seen | gru_robotobj2 | 17 of 81 (10 to 24) | 56 / 8 | +1 (-6 to +8) | +80 (73) | 48 of 1071 (0.045) | 18 of 31 | 0.021 of 472 / 0.063 of 599 |
