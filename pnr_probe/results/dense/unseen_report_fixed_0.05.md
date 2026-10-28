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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| pnr_probe/results/dense/unseen_a | progress | 14 of 54 (8 to 20) | 32 / 8 |  | +124 (46) | 46 of 1022 (0.045) | 25 of 29 | 0.050 of 463 / 0.041 of 559 |
| pnr_probe/results/dense/unseen_a | gru_phys | 8 of 54 (3 to 13) | 19 / 27 | -6 (-13 to +1) | +168 (27) | 8 of 1022 (0.008) | 3 of 29 | 0.004 of 463 / 0.011 of 559 |
| pnr_probe/results/dense/unseen_a | gru_phys_cusum | 14 of 54 (8 to 20) | 22 / 18 | +0 (-7 to +7) | +40 (36) | 88 of 1022 (0.086) | 13 of 29 | 0.097 of 463 / 0.077 of 559 |
| pnr_probe/results/dense/unseen_b | progress | 14 of 54 (8 to 20) | 32 / 8 |  | +124 (46) | 46 of 1022 (0.045) | 25 of 29 | 0.050 of 463 / 0.041 of 559 |
| pnr_probe/results/dense/unseen_b | gru_phys | 9 of 54 (4 to 15) | 21 / 24 | -5 (-12 to +2) | +88 (30) | 63 of 1022 (0.062) | 5 of 29 | 0.063 of 463 / 0.061 of 559 |
| pnr_probe/results/dense/unseen_b | gru_phys_cusum | 6 of 54 (2 to 11) | 15 / 33 | -8 (-15 to -1) | +128 (21) | 117 of 1022 (0.114) | 4 of 29 | 0.099 of 463 / 0.127 of 559 |
