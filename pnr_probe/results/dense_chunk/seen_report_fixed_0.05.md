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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| pnr_probe/results/dense_chunk/seen_a | progress | 19 of 78 (12 to 27) | 45 / 14 |  | +144 (64) | 39 of 912 (0.043) | 24 of 28 | 0.047 of 344 / 0.040 of 568 |
| pnr_probe/results/dense_chunk/seen_a | gru_phys | 22 of 78 (15 to 30) | 52 / 4 | +3 (-5 to +12) | +56 (74) | 41 of 912 (0.045) | 14 of 28 | 0.023 of 344 / 0.058 of 568 |
| pnr_probe/results/dense_chunk/seen_a | gru_phys_cusum | 15 of 78 (9 to 22) | 46 / 17 | -4 (-12 to +4) | +56 (61) | 41 of 912 (0.045) | 12 of 28 | 0.032 of 344 / 0.053 of 568 |
| pnr_probe/results/dense_chunk/seen_b | progress | 19 of 78 (12 to 27) | 45 / 14 |  | +144 (64) | 39 of 912 (0.043) | 24 of 28 | 0.047 of 344 / 0.040 of 568 |
| pnr_probe/results/dense_chunk/seen_b | gru_phys | 19 of 78 (12 to 27) | 52 / 7 | +0 (-9 to +9) | +64 (71) | 35 of 912 (0.038) | 12 of 28 | 0.023 of 344 / 0.048 of 568 |
| pnr_probe/results/dense_chunk/seen_b | gru_phys_cusum | 14 of 78 (8 to 21) | 51 / 13 | -5 (-13 to +3) | +56 (65) | 44 of 912 (0.048) | 12 of 28 | 0.029 of 344 / 0.060 of 568 |
