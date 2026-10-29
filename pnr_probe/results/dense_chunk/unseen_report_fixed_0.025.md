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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| pnr_probe/results/dense_chunk/unseen_a | progress | 14 of 78 (8 to 21) | 33 / 31 |  | +200 (47) | 31 of 912 (0.034) | 19 of 28 | 0.035 of 344 / 0.033 of 568 |
| pnr_probe/results/dense_chunk/unseen_a | gru_phys | 7 of 78 (3 to 12) | 36 / 35 | -7 (-15 to +1) | +128 (43) | 3 of 912 (0.003) | 3 of 28 | 0.000 of 344 / 0.005 of 568 |
| pnr_probe/results/dense_chunk/unseen_a | gru_phys_cusum | 9 of 78 (4 to 15) | 24 / 45 | -5 (-12 to +2) | +72 (33) | 169 of 912 (0.185) | 2 of 28 | 0.160 of 344 / 0.201 of 568 |
| pnr_probe/results/dense_chunk/unseen_b | progress | 14 of 78 (8 to 21) | 33 / 31 |  | +200 (47) | 31 of 912 (0.034) | 19 of 28 | 0.035 of 344 / 0.033 of 568 |
| pnr_probe/results/dense_chunk/unseen_b | gru_phys | 8 of 78 (3 to 14) | 39 / 31 | -6 (-13 to +1) | +136 (47) | 14 of 912 (0.015) | 2 of 28 | 0.012 of 344 / 0.018 of 568 |
| pnr_probe/results/dense_chunk/unseen_b | gru_phys_cusum | 4 of 78 (1 to 8) | 28 / 46 | -10 (-18 to -2) | +132 (32) | 152 of 912 (0.167) | 3 of 28 | 0.134 of 344 / 0.187 of 568 |
