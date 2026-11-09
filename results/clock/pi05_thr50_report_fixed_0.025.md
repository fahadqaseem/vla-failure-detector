# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/clock/pi05_thr50 | progress | 0.050 | -124 (26) | 4 of 29 (1 to 8) | 0.025 | -144 (23) | 2 of 29 (0 to 5) |
| data/clock/pi05_thr50 | gru_phys_ttp_s0 | 0.009 | -40 (15) | 5 of 29 (1 to 9) | 0.005 | -80 (15) | 4 of 29 (1 to 8) |
| data/clock/pi05_thr50 | gru_phys_ttp_s1 | 0.018 | -88 (15) | 6 of 29 (2 to 10) | 0.015 | -100 (14) | 5 of 29 (1 to 9) |
| data/clock/pi05_thr50 | gru_phys_ttp_s2 | 0.006 | -68 (8) | 3 of 29 (0 to 7) | 0.004 | -76 (8) | 3 of 29 (0 to 7) |
| data/clock/pi05_thr50 | gru_phys_ttp_s3 | 0.009 | -84 (6) | 1 of 29 (0 to 3) | 0.004 | -128 (6) | 1 of 29 (0 to 3) |
| data/clock/pi05_thr50 | gru_phys_ttp_s4 | 0.005 | -112 (11) | 4 of 29 (1 to 8) | 0.000 | -56 (8) | 2 of 29 (0 to 5) |
| data/clock/pi05_thr50 | gru_phys_ttp_ens | 0.006 | -68 (12) | 4 of 29 (1 to 8) | 0.000 | -112 (9) | 3 of 29 (0 to 7) |
| data/clock/pi05_thr50 | or_progress_ttp_s0 | 0.029 | -96 (27) | 6 of 29 (2 to 11) | 0.017 | -128 (25) | 6 of 29 (2 to 11) |
| data/clock/pi05_thr50 | or_progress_ttp_s1 | 0.039 | -104 (27) | 7 of 29 (3 to 12) | 0.024 | -148 (24) | 6 of 29 (2 to 11) |
| data/clock/pi05_thr50 | or_progress_ttp_s2 | 0.028 | -128 (25) | 5 of 29 (1 to 9) | 0.015 | -176 (22) | 5 of 29 (1 to 9) |
| data/clock/pi05_thr50 | or_progress_ttp_s3 | 0.028 | -128 (25) | 3 of 29 (0 to 7) | 0.013 | -176 (21) | 3 of 29 (0 to 7) |
| data/clock/pi05_thr50 | or_progress_ttp_s4 | 0.026 | -128 (25) | 4 of 29 (1 to 8) | 0.013 | -168 (22) | 4 of 29 (1 to 8) |
| data/clock/pi05_thr50 | or_progress_ens | 0.027 | -128 (26) | 5 of 29 (1 to 9) | 0.014 | -164 (22) | 4 of 29 (1 to 8) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/clock/pi05_thr50 | progress | 2 of 29 (0 to 5) | 21 / 6 |  | +144 (23) | 23 of 928 (0.025) | 3 of 4 | 0.021 of 475 / 0.029 of 453 |
| data/clock/pi05_thr50 | gru_phys_ttp_s0 | 4 of 29 (1 to 8) | 11 / 14 | +2 (-3 to +7) | +80 (15) | 5 of 928 (0.005) | 1 of 4 | 0.004 of 475 / 0.007 of 453 |
| data/clock/pi05_thr50 | gru_phys_ttp_s1 | 5 of 29 (1 to 9) | 9 / 15 | +3 (-2 to +8) | +100 (14) | 14 of 928 (0.015) | 0 of 4 | 0.008 of 475 / 0.022 of 453 |
| data/clock/pi05_thr50 | gru_phys_ttp_s2 | 3 of 29 (0 to 6) | 5 / 21 | +1 (-3 to +5) | +76 (8) | 4 of 928 (0.004) | 0 of 4 | 0.000 of 475 / 0.009 of 453 |
| data/clock/pi05_thr50 | gru_phys_ttp_s3 | 1 of 29 (0 to 3) | 5 / 23 | -1 (-4 to +2) | +128 (6) | 4 of 928 (0.004) | 1 of 4 | 0.000 of 475 / 0.009 of 453 |
| data/clock/pi05_thr50 | gru_phys_ttp_s4 | 2 of 29 (0 to 5) | 6 / 21 | +0 (-4 to +4) | +56 (8) | 0 of 928 (0.000) | 0 of 4 | 0.000 of 475 / 0.000 of 453 |
| data/clock/pi05_thr50 | gru_phys_ttp_ens | 3 of 29 (0 to 6) | 6 / 20 | +1 (-3 to +5) | +112 (9) | 0 of 928 (0.000) | 0 of 4 | 0.000 of 475 / 0.000 of 453 |
| data/clock/pi05_thr50 | or_progress_ttp_s0 | 6 of 29 (2 to 10) | 19 / 4 | +4 (+1 to +8) | +128 (25) | 16 of 928 (0.017) | 3 of 4 | 0.013 of 475 / 0.022 of 453 |
| data/clock/pi05_thr50 | or_progress_ttp_s1 | 6 of 29 (2 to 10) | 18 / 5 | +4 (+1 to +8) | +148 (24) | 22 of 928 (0.024) | 2 of 4 | 0.013 of 475 / 0.035 of 453 |
| data/clock/pi05_thr50 | or_progress_ttp_s2 | 5 of 29 (1 to 9) | 17 / 7 | +3 (+0 to +6) | +176 (22) | 14 of 928 (0.015) | 2 of 4 | 0.011 of 475 / 0.020 of 453 |
| data/clock/pi05_thr50 | or_progress_ttp_s3 | 3 of 29 (0 to 6) | 18 / 8 | +1 (+0 to +3) | +176 (21) | 12 of 928 (0.013) | 3 of 4 | 0.011 of 475 / 0.015 of 453 |
| data/clock/pi05_thr50 | or_progress_ttp_s4 | 4 of 29 (1 to 8) | 18 / 7 | +2 (+0 to +5) | +168 (22) | 12 of 928 (0.013) | 2 of 4 | 0.011 of 475 / 0.015 of 453 |
| data/clock/pi05_thr50 | or_progress_ens | 4 of 29 (1 to 8) | 18 / 7 | +2 (+0 to +5) | +164 (22) | 13 of 928 (0.014) | 2 of 4 | 0.011 of 475 / 0.018 of 453 |
