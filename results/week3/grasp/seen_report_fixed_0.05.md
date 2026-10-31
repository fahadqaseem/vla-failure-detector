# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/week3_grasp/seen | gru_grasp | 0.047 | -72 (77) | 20 of 81 (13 to 28) | 0.024 | -112 (73) | 12 of 81 (6 to 19) |
| data/week3_grasp/seen | gru_graspreal | 0.049 | -68 (72) | 14 of 81 (8 to 21) | 0.026 | -80 (68) | 13 of 81 (7 to 20) |
| data/week3_grasp/seen | gru_graspphys | 0.045 | -48 (75) | 23 of 81 (15 to 31) | 0.021 | -72 (71) | 15 of 81 (9 to 22) |
| data/week3_grasp/seen | gru_phys | 0.051 | -48 (75) | 23 of 81 (15 to 31) | 0.024 | -64 (73) | 19 of 81 (12 to 27) |
| data/week3_grasp/seen | gru_robot | 0.044 | -84 (74) | 17 of 81 (10 to 24) | 0.021 | -120 (66) | 11 of 81 (5 to 17) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/week3_grasp/seen | gru_grasp | 20 of 81 (13 to 28) | 57 / 4 |  | +72 (77) | 50 of 1071 (0.047) | 18 of 31 | 0.030 of 472 / 0.060 of 599 |
| data/week3_grasp/seen | gru_graspreal | 14 of 81 (8 to 21) | 58 / 9 |  | +68 (72) | 52 of 1071 (0.049) | 17 of 31 | 0.032 of 472 / 0.062 of 599 |
| data/week3_grasp/seen | gru_graspphys | 23 of 81 (15 to 31) | 52 / 6 |  | +48 (75) | 48 of 1071 (0.045) | 17 of 31 | 0.025 of 472 / 0.060 of 599 |
| data/week3_grasp/seen | gru_phys | 23 of 81 (15 to 31) | 52 / 6 |  | +48 (75) | 55 of 1071 (0.051) | 15 of 31 | 0.032 of 472 / 0.067 of 599 |
| data/week3_grasp/seen | gru_robot | 17 of 81 (10 to 25) | 57 / 7 |  | +84 (74) | 47 of 1071 (0.044) | 14 of 31 | 0.019 of 472 / 0.063 of 599 |
