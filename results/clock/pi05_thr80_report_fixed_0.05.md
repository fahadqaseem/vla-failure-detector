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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/clock/pi05_thr80 | progress | 11 of 34 (6 to 16) | 20 / 3 |  | +56 (31) | 46 of 928 (0.050) | 3 of 4 | 0.040 of 475 / 0.060 of 453 |
| data/clock/pi05_thr80 | gru_phys_ttp_s0 | 6 of 34 (2 to 11) | 4 / 24 | -5 (-11 to +1) | -96 (10) | 5 of 928 (0.005) | 0 of 4 | 0.002 of 475 / 0.009 of 453 |
| data/clock/pi05_thr80 | gru_phys_ttp_s1 | 1 of 34 (0 to 3) | 3 / 30 | -10 (-16 to -4) | +168 (4) | 13 of 928 (0.014) | 0 of 4 | 0.004 of 475 / 0.024 of 453 |
| data/clock/pi05_thr80 | gru_phys_ttp_s2 | 5 of 34 (1 to 9) | 4 / 25 | -6 (-13 to +0) | -96 (9) | 4 of 928 (0.004) | 0 of 4 | 0.002 of 475 / 0.007 of 453 |
| data/clock/pi05_thr80 | gru_phys_ttp_s3 | 1 of 34 (0 to 3) | 1 / 32 | -10 (-16 to -4) | -12 (2) | 6 of 928 (0.006) | 0 of 4 | 0.000 of 475 / 0.013 of 453 |
| data/clock/pi05_thr80 | gru_phys_ttp_s4 | 3 of 34 (0 to 6) | 2 / 29 | -8 (-14 to -3) | -56 (5) | 2 of 928 (0.002) | 0 of 4 | 0.000 of 475 / 0.004 of 453 |
| data/clock/pi05_thr80 | gru_phys_ttp_ens | 3 of 34 (0 to 7) | 3 / 28 | -8 (-14 to -2) | -16 (6) | 3 of 928 (0.003) | 0 of 4 | 0.000 of 475 / 0.007 of 453 |
| data/clock/pi05_thr80 | or_progress_ttp_s0 | 12 of 34 (7 to 18) | 20 / 2 | +1 (-3 to +5) | +76 (32) | 25 of 928 (0.027) | 3 of 4 | 0.023 of 475 / 0.031 of 453 |
| data/clock/pi05_thr80 | or_progress_ttp_s1 | 9 of 34 (4 to 14) | 20 / 5 | -2 (-6 to +2) | +88 (29) | 27 of 928 (0.029) | 3 of 4 | 0.021 of 475 / 0.038 of 453 |
| data/clock/pi05_thr80 | or_progress_ttp_s2 | 12 of 34 (7 to 17) | 18 / 4 | +1 (-3 to +5) | +84 (30) | 24 of 928 (0.026) | 3 of 4 | 0.021 of 475 / 0.031 of 453 |
| data/clock/pi05_thr80 | or_progress_ttp_s3 | 9 of 34 (4 to 14) | 20 / 5 | -2 (-6 to +2) | +88 (29) | 25 of 928 (0.027) | 3 of 4 | 0.021 of 475 / 0.033 of 453 |
| data/clock/pi05_thr80 | or_progress_ttp_s4 | 10 of 34 (5 to 15) | 19 / 5 | -1 (-5 to +2) | +104 (29) | 23 of 928 (0.025) | 3 of 4 | 0.021 of 475 / 0.029 of 453 |
| data/clock/pi05_thr80 | or_progress_ens | 10 of 34 (5 to 15) | 19 / 5 | -1 (-5 to +2) | +104 (29) | 24 of 928 (0.026) | 3 of 4 | 0.021 of 475 / 0.031 of 453 |
