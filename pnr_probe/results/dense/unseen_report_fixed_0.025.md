# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 |
|---|---|---|---|---|---|---|---|
| pnr_probe/results/dense/unseen_a | progress | 0.024 | -152 (32) | 10 of 54 (5 to 16) | 0.045 | -124 (46) | 14 of 54 (8 to 20) |
| pnr_probe/results/dense/unseen_a | gru_phys | 0.004 | -184 (19) | 4 of 54 (1 to 8) | 0.008 | -168 (27) | 8 of 54 (3 to 13) |
| pnr_probe/results/dense/unseen_a | gru_phys_cusum | 0.049 | -116 (30) | 7 of 54 (3 to 12) | 0.086 | -40 (36) | 14 of 54 (8 to 20) |
| pnr_probe/results/dense/unseen_b | progress | 0.024 | -152 (32) | 10 of 54 (5 to 16) | 0.045 | -124 (46) | 14 of 54 (8 to 20) |
| pnr_probe/results/dense/unseen_b | gru_phys | 0.034 | -96 (27) | 8 of 54 (3 to 13) | 0.062 | -88 (30) | 9 of 54 (4 to 15) |
| pnr_probe/results/dense/unseen_b | gru_phys_cusum | 0.069 | -152 (17) | 2 of 54 (0 to 5) | 0.114 | -128 (21) | 6 of 54 (2 to 11) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| pnr_probe/results/dense/unseen_a | progress | 10 of 54 (5 to 16) | 22 / 22 |  | +152 (32) | 25 of 1022 (0.024) | 20 of 29 | 0.028 of 463 / 0.021 of 559 |
| pnr_probe/results/dense/unseen_a | gru_phys | 4 of 54 (1 to 8) | 15 / 35 | -6 (-12 to -1) | +184 (19) | 4 of 1022 (0.004) | 2 of 29 | 0.002 of 463 / 0.005 of 559 |
| pnr_probe/results/dense/unseen_a | gru_phys_cusum | 7 of 54 (3 to 12) | 23 / 24 | -3 (-10 to +4) | +116 (30) | 50 of 1022 (0.049) | 7 of 29 | 0.045 of 463 / 0.052 of 559 |
| pnr_probe/results/dense/unseen_b | progress | 10 of 54 (5 to 16) | 22 / 22 |  | +152 (32) | 25 of 1022 (0.024) | 20 of 29 | 0.028 of 463 / 0.021 of 559 |
| pnr_probe/results/dense/unseen_b | gru_phys | 8 of 54 (3 to 13) | 19 / 27 | -2 (-8 to +4) | +96 (27) | 35 of 1022 (0.034) | 2 of 29 | 0.039 of 463 / 0.030 of 559 |
| pnr_probe/results/dense/unseen_b | gru_phys_cusum | 2 of 54 (0 to 5) | 15 / 37 | -8 (-14 to -2) | +152 (17) | 71 of 1022 (0.069) | 2 of 29 | 0.054 of 463 / 0.082 of 559 |
