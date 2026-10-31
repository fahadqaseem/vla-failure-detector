# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/week3_grasp/unseen | gru_grasp | 0.007 | -216 (41) | 5 of 81 (1 to 10) | 0.005 | -172 (22) | 4 of 81 (1 to 8) |
| data/week3_grasp/unseen | gru_graspreal | 0.087 | -140 (28) | 3 of 81 (0 to 7) | 0.038 | -128 (20) | 3 of 81 (0 to 7) |
| data/week3_grasp/unseen | gru_graspphys | 0.063 | -108 (56) | 13 of 81 (7 to 20) | 0.030 | -124 (52) | 12 of 81 (6 to 19) |
| data/week3_grasp/unseen | gru_phys | 0.014 | -112 (44) | 12 of 81 (6 to 18) | 0.014 | -136 (43) | 10 of 81 (5 to 16) |
| data/week3_grasp/unseen | gru_robot | 0.048 | -208 (29) | 6 of 81 (2 to 11) | 0.046 | -232 (15) | 4 of 81 (1 to 8) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/week3_grasp/unseen | gru_grasp | 5 of 81 (1 to 9) | 36 / 40 |  | +216 (41) | 8 of 1071 (0.007) | 9 of 31 | 0.002 of 472 / 0.012 of 599 |
| data/week3_grasp/unseen | gru_graspreal | 3 of 81 (0 to 7) | 25 / 53 |  | +140 (28) | 93 of 1071 (0.087) | 2 of 31 | 0.059 of 472 / 0.109 of 599 |
| data/week3_grasp/unseen | gru_graspphys | 13 of 81 (7 to 20) | 43 / 25 |  | +108 (56) | 67 of 1071 (0.063) | 7 of 31 | 0.038 of 472 / 0.082 of 599 |
| data/week3_grasp/unseen | gru_phys | 12 of 81 (6 to 19) | 32 / 37 |  | +112 (44) | 15 of 1071 (0.014) | 2 of 31 | 0.000 of 472 / 0.025 of 599 |
| data/week3_grasp/unseen | gru_robot | 6 of 81 (2 to 11) | 23 / 52 |  | +208 (29) | 51 of 1071 (0.048) | 0 of 31 | 0.104 of 472 / 0.003 of 599 |
