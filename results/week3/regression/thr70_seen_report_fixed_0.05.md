# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/week3_reg/thr70/seen | progress | 0.046 | -112 (69) | 22 of 91 (14 to 30) | 0.026 | -136 (51) | 15 of 91 (8 to 22) |
| data/week3_reg/thr70/seen | gru_phys | 0.046 | -16 (85) | 36 of 91 (27 to 45) | 0.017 | -32 (84) | 27 of 91 (19 to 36) |
| data/week3_reg/thr70/seen | gru_phys_frac | 0.049 | -24 (88) | 35 of 91 (26 to 44) | 0.025 | -48 (78) | 28 of 91 (20 to 37) |
| data/week3_reg/thr70/seen | gru_phys_ttp | 0.047 | -24 (86) | 34 of 91 (25 to 43) | 0.025 | -48 (79) | 28 of 91 (20 to 37) |
| data/week3_reg/thr70/seen | gru_robot | 0.044 | -56 (87) | 29 of 91 (20 to 38) | 0.021 | -80 (74) | 19 of 91 (12 to 27) |
| data/week3_reg/thr70/seen | gru_robotobj1 | 0.049 | -40 (83) | 31 of 91 (22 to 40) | 0.022 | -72 (80) | 22 of 91 (14 to 30) |
| data/week3_reg/thr70/seen | gru_robotobj2 | 0.052 | -24 (83) | 31 of 91 (22 to 40) | 0.022 | -72 (81) | 21 of 91 (13 to 29) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/week3_reg/thr70/seen | progress | 22 of 91 (14 to 30) | 47 / 22 |  | +112 (69) | 49 of 1071 (0.046) | 29 of 35 | 0.049 of 472 / 0.043 of 599 |
| data/week3_reg/thr70/seen | gru_phys | 36 of 91 (27 to 45) | 49 / 6 | +14 (+5 to +24) | +16 (85) | 49 of 1071 (0.046) | 20 of 35 | 0.025 of 472 / 0.062 of 599 |
| data/week3_reg/thr70/seen | gru_phys_frac | 35 of 91 (26 to 44) | 53 / 3 | +13 (+3 to +23) | +24 (88) | 52 of 1071 (0.049) | 26 of 35 | 0.030 of 472 / 0.063 of 599 |
| data/week3_reg/thr70/seen | gru_phys_ttp | 34 of 91 (25 to 43) | 52 / 5 | +12 (+3 to +22) | +24 (86) | 50 of 1071 (0.047) | 20 of 35 | 0.030 of 472 / 0.060 of 599 |
| data/week3_reg/thr70/seen | gru_robot | 29 of 91 (21 to 38) | 58 / 4 | +7 (-3 to +17) | +56 (87) | 47 of 1071 (0.044) | 15 of 35 | 0.025 of 472 / 0.058 of 599 |
| data/week3_reg/thr70/seen | gru_robotobj1 | 31 of 91 (22 to 40) | 52 / 8 | +9 (-1 to +19) | +40 (83) | 53 of 1071 (0.049) | 18 of 35 | 0.021 of 472 / 0.072 of 599 |
| data/week3_reg/thr70/seen | gru_robotobj2 | 31 of 91 (22 to 40) | 52 / 8 | +9 (-1 to +19) | +24 (83) | 56 of 1071 (0.052) | 17 of 35 | 0.023 of 472 / 0.075 of 599 |
