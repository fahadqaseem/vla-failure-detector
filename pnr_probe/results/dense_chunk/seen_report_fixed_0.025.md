# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 |
|---|---|---|---|---|---|---|---|
| pnr_probe/results/dense_chunk/seen_a | progress | 0.025 | -176 (43) | 11 of 78 (5 to 17) | 0.043 | -144 (64) | 19 of 78 (12 to 27) |
| pnr_probe/results/dense_chunk/seen_a | gru_phys | 0.024 | -72 (69) | 16 of 78 (9 to 23) | 0.045 | -56 (74) | 22 of 78 (14 to 30) |
| pnr_probe/results/dense_chunk/seen_a | gru_phys_cusum | 0.018 | -72 (51) | 12 of 78 (6 to 19) | 0.045 | -56 (61) | 15 of 78 (9 to 22) |
| pnr_probe/results/dense_chunk/seen_b | progress | 0.025 | -176 (43) | 11 of 78 (5 to 17) | 0.043 | -144 (64) | 19 of 78 (12 to 27) |
| pnr_probe/results/dense_chunk/seen_b | gru_phys | 0.020 | -72 (69) | 14 of 78 (8 to 21) | 0.038 | -64 (71) | 19 of 78 (12 to 27) |
| pnr_probe/results/dense_chunk/seen_b | gru_phys_cusum | 0.022 | -84 (54) | 10 of 78 (5 to 16) | 0.048 | -56 (65) | 14 of 78 (8 to 21) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| pnr_probe/results/dense_chunk/seen_a | progress | 11 of 78 (5 to 17) | 32 / 35 |  | +176 (43) | 23 of 912 (0.025) | 19 of 28 | 0.029 of 344 / 0.023 of 568 |
| pnr_probe/results/dense_chunk/seen_a | gru_phys | 16 of 78 (9 to 23) | 53 / 9 | +5 (-3 to +13) | +72 (69) | 22 of 912 (0.024) | 10 of 28 | 0.012 of 344 / 0.032 of 568 |
| pnr_probe/results/dense_chunk/seen_a | gru_phys_cusum | 12 of 78 (6 to 18) | 39 / 27 | +1 (-7 to +9) | +72 (51) | 16 of 912 (0.018) | 10 of 28 | 0.015 of 344 / 0.019 of 568 |
| pnr_probe/results/dense_chunk/seen_b | progress | 11 of 78 (5 to 17) | 32 / 35 |  | +176 (43) | 23 of 912 (0.025) | 19 of 28 | 0.029 of 344 / 0.023 of 568 |
| pnr_probe/results/dense_chunk/seen_b | gru_phys | 14 of 78 (8 to 21) | 55 / 9 | +3 (-5 to +11) | +72 (69) | 18 of 912 (0.020) | 11 of 28 | 0.015 of 344 / 0.023 of 568 |
| pnr_probe/results/dense_chunk/seen_b | gru_phys_cusum | 10 of 78 (5 to 16) | 44 / 24 | -1 (-9 to +7) | +84 (54) | 20 of 912 (0.022) | 9 of 28 | 0.015 of 344 / 0.026 of 568 |
