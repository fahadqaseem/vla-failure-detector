# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/clock/pi05_thr80 | progress | 0.050 | -56 (31) | 11 of 34 (6 to 16) | 0.025 | -96 (28) | 8 of 34 (3 to 13) |
| data/clock/pi05_thr80 | gru_phys_ttp_s0 | 0.005 | +96 (10) | 6 of 34 (2 to 11) | 0.002 | +96 (9) | 5 of 34 (1 to 9) |
| data/clock/pi05_thr80 | gru_phys_ttp_s1 | 0.014 | -168 (4) | 1 of 34 (0 to 3) | 0.005 | -104 (3) | 1 of 34 (0 to 3) |
| data/clock/pi05_thr80 | gru_phys_ttp_s2 | 0.004 | +96 (9) | 5 of 34 (1 to 9) | 0.002 | +44 (8) | 4 of 34 (1 to 8) |
| data/clock/pi05_thr80 | gru_phys_ttp_s3 | 0.006 | +12 (2) | 1 of 34 (0 to 3) | 0.002 | -56 (2) | 0 of 34 (0 to 0) |
| data/clock/pi05_thr80 | gru_phys_ttp_s4 | 0.002 | +56 (5) | 3 of 34 (0 to 7) | 0.000 | -8 (4) | 2 of 34 (0 to 5) |
| data/clock/pi05_thr80 | gru_phys_ttp_ens | 0.003 | +16 (6) | 3 of 34 (0 to 7) | 0.002 | -8 (4) | 2 of 34 (0 to 5) |
| data/clock/pi05_thr80 | or_progress_ttp_s0 | 0.027 | -76 (32) | 12 of 34 (7 to 18) | 0.014 | -112 (29) | 10 of 34 (5 to 15) |
| data/clock/pi05_thr80 | or_progress_ttp_s1 | 0.029 | -88 (29) | 9 of 34 (4 to 14) | 0.014 | -136 (25) | 5 of 34 (1 to 9) |
| data/clock/pi05_thr80 | or_progress_ttp_s2 | 0.026 | -84 (30) | 12 of 34 (7 to 17) | 0.015 | -104 (27) | 9 of 34 (4 to 14) |
| data/clock/pi05_thr80 | or_progress_ttp_s3 | 0.027 | -88 (29) | 9 of 34 (4 to 14) | 0.014 | -136 (25) | 5 of 34 (1 to 9) |
| data/clock/pi05_thr80 | or_progress_ttp_s4 | 0.025 | -104 (29) | 10 of 34 (5 to 15) | 0.013 | -136 (25) | 6 of 34 (2 to 11) |
| data/clock/pi05_thr80 | or_progress_ens | 0.026 | -104 (29) | 10 of 34 (5 to 15) | 0.014 | -136 (26) | 6 of 34 (2 to 11) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/clock/pi05_thr80 | progress | 8 of 34 (3 to 13) | 20 / 6 |  | +96 (28) | 23 of 928 (0.025) | 3 of 4 | 0.021 of 475 / 0.029 of 453 |
| data/clock/pi05_thr80 | gru_phys_ttp_s0 | 5 of 34 (1 to 9) | 4 / 25 | -3 (-9 to +3) | -96 (9) | 2 of 928 (0.002) | 0 of 4 | 0.002 of 475 / 0.002 of 453 |
| data/clock/pi05_thr80 | gru_phys_ttp_s1 | 1 of 34 (0 to 3) | 2 / 31 | -7 (-12 to -2) | +104 (3) | 5 of 928 (0.005) | 0 of 4 | 0.000 of 475 / 0.011 of 453 |
| data/clock/pi05_thr80 | gru_phys_ttp_s2 | 4 of 34 (1 to 8) | 4 / 26 | -4 (-10 to +2) | -44 (8) | 2 of 928 (0.002) | 0 of 4 | 0.000 of 475 / 0.004 of 453 |
| data/clock/pi05_thr80 | gru_phys_ttp_s3 | 0 of 34 (0 to 0) | 2 / 32 | -8 (-13 to -3) | +56 (2) | 2 of 928 (0.002) | 0 of 4 | 0.000 of 475 / 0.004 of 453 |
| data/clock/pi05_thr80 | gru_phys_ttp_s4 | 2 of 34 (0 to 5) | 2 / 30 | -6 (-12 to +0) | +8 (4) | 0 of 928 (0.000) | 0 of 4 | 0.000 of 475 / 0.000 of 453 |
| data/clock/pi05_thr80 | gru_phys_ttp_ens | 2 of 34 (0 to 5) | 2 / 30 | -6 (-12 to +0) | +8 (4) | 2 of 928 (0.002) | 0 of 4 | 0.000 of 475 / 0.004 of 453 |
| data/clock/pi05_thr80 | or_progress_ttp_s0 | 10 of 34 (5 to 15) | 19 / 5 | +2 (-3 to +7) | +112 (29) | 13 of 928 (0.014) | 2 of 4 | 0.013 of 475 / 0.015 of 453 |
| data/clock/pi05_thr80 | or_progress_ttp_s1 | 5 of 34 (1 to 9) | 20 / 9 | -3 (-6 to +0) | +136 (25) | 13 of 928 (0.014) | 2 of 4 | 0.011 of 475 / 0.018 of 453 |
| data/clock/pi05_thr80 | or_progress_ttp_s2 | 9 of 34 (4 to 14) | 18 / 7 | +1 (-3 to +5) | +104 (27) | 14 of 928 (0.015) | 2 of 4 | 0.011 of 475 / 0.020 of 453 |
| data/clock/pi05_thr80 | or_progress_ttp_s3 | 5 of 34 (1 to 9) | 20 / 9 | -3 (-6 to +0) | +136 (25) | 13 of 928 (0.014) | 2 of 4 | 0.011 of 475 / 0.018 of 453 |
| data/clock/pi05_thr80 | or_progress_ttp_s4 | 6 of 34 (2 to 11) | 19 / 9 | -2 (-6 to +2) | +136 (25) | 12 of 928 (0.013) | 2 of 4 | 0.011 of 475 / 0.015 of 453 |
| data/clock/pi05_thr80 | or_progress_ens | 6 of 34 (2 to 11) | 20 / 8 | -2 (-6 to +2) | +136 (26) | 13 of 928 (0.014) | 2 of 4 | 0.011 of 475 / 0.018 of 453 |
