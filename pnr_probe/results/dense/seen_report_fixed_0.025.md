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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| pnr_probe/results/dense/seen_a | progress | 10 of 54 (5 to 16) | 22 / 22 |  | +140 (32) | 25 of 1022 (0.024) | 20 of 29 | 0.030 of 463 / 0.020 of 559 |
| pnr_probe/results/dense/seen_a | gru_phys | 15 of 54 (9 to 22) | 33 / 6 | +5 (-2 to +12) | +72 (48) | 24 of 1022 (0.023) | 13 of 29 | 0.015 of 463 / 0.030 of 559 |
| pnr_probe/results/dense/seen_a | gru_phys_cusum | 11 of 54 (5 to 17) | 26 / 17 | +1 (-6 to +8) | +64 (37) | 21 of 1022 (0.021) | 14 of 29 | 0.013 of 463 / 0.027 of 559 |
| pnr_probe/results/dense/seen_b | progress | 10 of 54 (5 to 16) | 22 / 22 |  | +140 (32) | 25 of 1022 (0.024) | 20 of 29 | 0.030 of 463 / 0.020 of 559 |
| pnr_probe/results/dense/seen_b | gru_phys | 15 of 54 (9 to 22) | 33 / 6 | +5 (-2 to +12) | +72 (48) | 21 of 1022 (0.021) | 13 of 29 | 0.011 of 463 / 0.029 of 559 |
| pnr_probe/results/dense/seen_b | gru_phys_cusum | 12 of 54 (6 to 18) | 27 / 15 | +2 (-5 to +9) | +64 (39) | 28 of 1022 (0.027) | 11 of 29 | 0.011 of 463 / 0.041 of 559 |
