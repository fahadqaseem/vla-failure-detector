# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/combo/pi05/thr80/merged | progress | 0.050 | +28 (30) | 17 of 33 (11 to 23) | 0.025 | -40 (27) | 12 of 33 (7 to 18) |
| data/combo/pi05/thr80/merged | gru_phys_ttp | 0.005 | +192 (9) | 7 of 33 (3 to 12) | 0.002 | +136 (8) | 6 of 33 (2 to 11) |
| data/combo/pi05/thr80/merged | or_progress_ttp | 0.027 | -8 (31) | 15 of 33 (10 to 21) | 0.014 | -60 (28) | 12 of 33 (7 to 18) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/combo/pi05/thr80/merged | progress | 12 of 33 (7 to 17) | 15 / 6 |  | +40 (27) | 23 of 928 (0.025) | 7 of 8 | 0.021 of 475 / 0.029 of 453 |
| data/combo/pi05/thr80/merged | gru_phys_ttp | 6 of 33 (2 to 11) | 2 / 25 | -6 (-12 to +0) | -136 (8) | 2 of 928 (0.002) | 1 of 8 | 0.002 of 475 / 0.002 of 453 |
| data/combo/pi05/thr80/merged | or_progress_ttp | 12 of 33 (7 to 18) | 16 / 5 | +0 (-4 to +4) | +60 (28) | 13 of 928 (0.014) | 6 of 8 | 0.013 of 475 / 0.015 of 453 |
