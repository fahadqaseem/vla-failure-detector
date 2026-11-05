# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/pi05_reg/thr80/unseen | progress | 0.050 | +28 (30) | 17 of 33 (11 to 23) | 0.025 | -40 (27) | 12 of 33 (7 to 18) |
| data/pi05_reg/thr80/unseen | gru_phys | 0.001 | -144 (2) | 0 of 33 (0 to 0) | 0.000 | -156 (2) | 0 of 33 (0 to 0) |
| data/pi05_reg/thr80/unseen | gru_phys_frac | 0.003 | +208 (6) | 5 of 33 (1 to 9) | 0.001 | +240 (5) | 4 of 33 (1 to 8) |
| data/pi05_reg/thr80/unseen | gru_phys_ttp | 0.005 | +192 (9) | 7 of 33 (3 to 12) | 0.002 | +136 (8) | 6 of 33 (2 to 11) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/pi05_reg/thr80/unseen | progress | 17 of 33 (11 to 22) | 13 / 3 |  | -28 (30) | 46 of 928 (0.050) | 7 of 8 | 0.040 of 475 / 0.060 of 453 |
| data/pi05_reg/thr80/unseen | gru_phys | 0 of 33 (0 to 0) | 2 / 31 | -17 (-22 to -11) | +144 (2) | 1 of 928 (0.001) | 0 of 8 | 0.000 of 475 / 0.002 of 453 |
| data/pi05_reg/thr80/unseen | gru_phys_frac | 5 of 33 (1 to 9) | 1 / 27 | -12 (-18 to -6) | -208 (6) | 3 of 928 (0.003) | 0 of 8 | 0.000 of 475 / 0.007 of 453 |
| data/pi05_reg/thr80/unseen | gru_phys_ttp | 7 of 33 (3 to 12) | 2 / 24 | -10 (-16 to -3) | -192 (9) | 5 of 928 (0.005) | 1 of 8 | 0.002 of 475 / 0.009 of 453 |
