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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/clock/pi05_thr50 | progress | 4 of 29 (1 to 8) | 22 / 3 |  | +124 (26) | 46 of 928 (0.050) | 3 of 4 | 0.040 of 475 / 0.060 of 453 |
| data/clock/pi05_thr50 | gru_phys_ttp_s0 | 5 of 29 (1 to 9) | 10 / 14 | +1 (-3 to +5) | +40 (15) | 8 of 928 (0.009) | 1 of 4 | 0.006 of 475 / 0.011 of 453 |
| data/clock/pi05_thr50 | gru_phys_ttp_s1 | 6 of 29 (2 to 11) | 9 / 14 | +2 (-3 to +7) | +88 (15) | 17 of 928 (0.018) | 0 of 4 | 0.011 of 475 / 0.026 of 453 |
| data/clock/pi05_thr50 | gru_phys_ttp_s2 | 3 of 29 (0 to 6) | 5 / 21 | -1 (-6 to +3) | +68 (8) | 6 of 928 (0.006) | 0 of 4 | 0.002 of 475 / 0.011 of 453 |
| data/clock/pi05_thr50 | gru_phys_ttp_s3 | 1 of 29 (0 to 3) | 5 / 23 | -3 (-7 to +1) | +84 (6) | 8 of 928 (0.009) | 1 of 4 | 0.002 of 475 / 0.015 of 453 |
| data/clock/pi05_thr50 | gru_phys_ttp_s4 | 4 of 29 (1 to 8) | 7 / 18 | +0 (-4 to +4) | +112 (11) | 5 of 928 (0.005) | 0 of 4 | 0.002 of 475 / 0.009 of 453 |
| data/clock/pi05_thr50 | gru_phys_ttp_ens | 4 of 29 (1 to 8) | 8 / 17 | +0 (-5 to +5) | +68 (12) | 6 of 928 (0.006) | 1 of 4 | 0.002 of 475 / 0.011 of 453 |
| data/clock/pi05_thr50 | or_progress_ttp_s0 | 6 of 29 (2 to 10) | 21 / 2 | +2 (+0 to +5) | +96 (27) | 27 of 928 (0.029) | 4 of 4 | 0.025 of 475 / 0.033 of 453 |
| data/clock/pi05_thr50 | or_progress_ttp_s1 | 7 of 29 (3 to 12) | 20 / 2 | +3 (+0 to +6) | +104 (27) | 36 of 928 (0.039) | 3 of 4 | 0.029 of 475 / 0.049 of 453 |
| data/clock/pi05_thr50 | or_progress_ttp_s2 | 5 of 29 (1 to 9) | 20 / 4 | +1 (-2 to +4) | +128 (25) | 26 of 928 (0.028) | 3 of 4 | 0.021 of 475 / 0.035 of 453 |
| data/clock/pi05_thr50 | or_progress_ttp_s3 | 3 of 29 (0 to 6) | 22 / 4 | -1 (-4 to +2) | +128 (25) | 26 of 928 (0.028) | 4 of 4 | 0.021 of 475 / 0.035 of 453 |
| data/clock/pi05_thr50 | or_progress_ttp_s4 | 4 of 29 (1 to 8) | 21 / 4 | +0 (-3 to +3) | +128 (25) | 24 of 928 (0.026) | 3 of 4 | 0.021 of 475 / 0.031 of 453 |
| data/clock/pi05_thr50 | or_progress_ens | 5 of 29 (1 to 9) | 21 / 3 | +1 (-2 to +4) | +128 (26) | 25 of 928 (0.027) | 3 of 4 | 0.021 of 475 / 0.033 of 453 |
