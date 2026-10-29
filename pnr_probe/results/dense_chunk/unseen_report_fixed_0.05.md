# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 |
|---|---|---|---|---|---|---|---|
| pnr_probe/results/dense_chunk/unseen_a | progress | 0.034 | -200 (47) | 14 of 78 (8 to 21) | 0.049 | -136 (63) | 19 of 78 (12 to 27) |
| pnr_probe/results/dense_chunk/unseen_a | gru_phys | 0.003 | -128 (43) | 7 of 78 (3 to 12) | 0.092 | -120 (45) | 7 of 78 (3 to 12) |
| pnr_probe/results/dense_chunk/unseen_a | gru_phys_cusum | 0.185 | -72 (33) | 9 of 78 (4 to 15) | 0.209 | -56 (38) | 13 of 78 (7 to 20) |
| pnr_probe/results/dense_chunk/unseen_b | progress | 0.034 | -200 (47) | 14 of 78 (8 to 21) | 0.049 | -136 (63) | 19 of 78 (12 to 27) |
| pnr_probe/results/dense_chunk/unseen_b | gru_phys | 0.015 | -136 (47) | 8 of 78 (3 to 14) | 0.101 | -120 (47) | 11 of 78 (5 to 17) |
| pnr_probe/results/dense_chunk/unseen_b | gru_phys_cusum | 0.167 | -132 (32) | 4 of 78 (1 to 8) | 0.191 | -112 (35) | 6 of 78 (2 to 11) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| pnr_probe/results/dense_chunk/unseen_a | progress | 19 of 78 (12 to 27) | 44 / 15 |  | +136 (63) | 45 of 912 (0.049) | 25 of 28 | 0.052 of 344 / 0.048 of 568 |
| pnr_probe/results/dense_chunk/unseen_a | gru_phys | 7 of 78 (3 to 12) | 38 / 33 | -12 (-20 to -4) | +120 (45) | 84 of 912 (0.092) | 3 of 28 | 0.093 of 344 / 0.092 of 568 |
| pnr_probe/results/dense_chunk/unseen_a | gru_phys_cusum | 13 of 78 (7 to 20) | 25 / 40 | -6 (-13 to +1) | +56 (38) | 191 of 912 (0.209) | 3 of 28 | 0.183 of 344 / 0.225 of 568 |
| pnr_probe/results/dense_chunk/unseen_b | progress | 19 of 78 (12 to 27) | 44 / 15 |  | +136 (63) | 45 of 912 (0.049) | 25 of 28 | 0.052 of 344 / 0.048 of 568 |
| pnr_probe/results/dense_chunk/unseen_b | gru_phys | 11 of 78 (5 to 17) | 36 / 31 | -8 (-16 to -1) | +120 (47) | 92 of 912 (0.101) | 3 of 28 | 0.073 of 344 / 0.118 of 568 |
| pnr_probe/results/dense_chunk/unseen_b | gru_phys_cusum | 6 of 78 (2 to 11) | 29 / 43 | -13 (-22 to -4) | +112 (35) | 174 of 912 (0.191) | 4 of 28 | 0.160 of 344 / 0.210 of 568 |
