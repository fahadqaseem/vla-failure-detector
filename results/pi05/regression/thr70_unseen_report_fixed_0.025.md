# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/pi05_reg/thr70/unseen | progress | 0.050 | -84 (28) | 8 of 31 (3 to 13) | 0.025 | -136 (25) | 6 of 31 (2 to 11) |
| data/pi05_reg/thr70/unseen | gru_phys | 0.004 | -44 (6) | 3 of 31 (0 to 6) | 0.000 | -56 (6) | 3 of 31 (0 to 6) |
| data/pi05_reg/thr70/unseen | gru_phys_frac | 0.012 | +132 (10) | 7 of 31 (3 to 12) | 0.005 | +132 (10) | 6 of 31 (2 to 11) |
| data/pi05_reg/thr70/unseen | gru_phys_ttp | 0.014 | +88 (14) | 10 of 31 (5 to 15) | 0.008 | +72 (13) | 9 of 31 (4 to 14) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/pi05_reg/thr70/unseen | progress | 6 of 31 (2 to 11) | 19 / 6 |  | +136 (25) | 23 of 928 (0.025) | 6 of 7 | 0.021 of 475 / 0.029 of 453 |
| data/pi05_reg/thr70/unseen | gru_phys | 3 of 31 (0 to 6) | 3 / 25 | -3 (-8 to +2) | +56 (6) | 0 of 928 (0.000) | 1 of 7 | 0.000 of 475 / 0.000 of 453 |
| data/pi05_reg/thr70/unseen | gru_phys_frac | 6 of 31 (2 to 11) | 4 / 21 | +0 (-5 to +6) | -132 (10) | 5 of 928 (0.005) | 0 of 7 | 0.002 of 475 / 0.009 of 453 |
| data/pi05_reg/thr70/unseen | gru_phys_ttp | 9 of 31 (4 to 14) | 4 / 18 | +3 (-3 to +9) | -72 (13) | 7 of 928 (0.008) | 0 of 7 | 0.004 of 475 / 0.011 of 453 |
