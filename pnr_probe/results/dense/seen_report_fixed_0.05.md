# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 |
|---|---|---|---|---|---|---|---|
| pnr_probe/results/dense/seen_a | progress | 0.024 | -140 (32) | 10 of 54 (5 to 16) | 0.044 | -120 (44) | 13 of 54 (7 to 19) |
| pnr_probe/results/dense/seen_a | gru_phys | 0.023 | -72 (48) | 15 of 54 (9 to 22) | 0.038 | -56 (48) | 16 of 54 (10 to 23) |
| pnr_probe/results/dense/seen_a | gru_phys_cusum | 0.021 | -64 (37) | 11 of 54 (6 to 17) | 0.053 | -44 (42) | 16 of 54 (10 to 23) |
| pnr_probe/results/dense/seen_b | progress | 0.024 | -140 (32) | 10 of 54 (5 to 16) | 0.044 | -120 (44) | 13 of 54 (7 to 19) |
| pnr_probe/results/dense/seen_b | gru_phys | 0.021 | -72 (48) | 15 of 54 (9 to 22) | 0.049 | -60 (52) | 19 of 54 (12 to 26) |
| pnr_probe/results/dense/seen_b | gru_phys_cusum | 0.027 | -64 (39) | 12 of 54 (6 to 18) | 0.045 | -64 (46) | 15 of 54 (9 to 22) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| pnr_probe/results/dense/seen_a | progress | 13 of 54 (7 to 19) | 31 / 10 |  | +120 (44) | 45 of 1022 (0.044) | 24 of 29 | 0.050 of 463 / 0.039 of 559 |
| pnr_probe/results/dense/seen_a | gru_phys | 16 of 54 (10 to 23) | 32 / 6 | +3 (-5 to +11) | +56 (48) | 39 of 1022 (0.038) | 15 of 29 | 0.022 of 463 / 0.052 of 559 |
| pnr_probe/results/dense/seen_a | gru_phys_cusum | 16 of 54 (9 to 23) | 26 / 12 | +3 (-4 to +10) | +44 (42) | 54 of 1022 (0.053) | 16 of 29 | 0.030 of 463 / 0.072 of 559 |
| pnr_probe/results/dense/seen_b | progress | 13 of 54 (7 to 19) | 31 / 10 |  | +120 (44) | 45 of 1022 (0.044) | 24 of 29 | 0.050 of 463 / 0.039 of 559 |
| pnr_probe/results/dense/seen_b | gru_phys | 19 of 54 (12 to 26) | 33 / 2 | +6 (-1 to +13) | +60 (52) | 50 of 1022 (0.049) | 14 of 29 | 0.019 of 463 / 0.073 of 559 |
| pnr_probe/results/dense/seen_b | gru_phys_cusum | 15 of 54 (9 to 22) | 31 / 8 | +2 (-5 to +9) | +64 (46) | 46 of 1022 (0.045) | 17 of 29 | 0.028 of 463 / 0.059 of 559 |
