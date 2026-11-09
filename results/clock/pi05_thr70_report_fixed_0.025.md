# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/clock/pi05_thr70 | progress | 0.050 | -72 (29) | 6 of 32 (2 to 10) | 0.025 | -112 (26) | 3 of 32 (0 to 6) |
| data/clock/pi05_thr70 | gru_phys_ttp_s0 | 0.014 | -16 (14) | 7 of 32 (3 to 12) | 0.008 | +24 (13) | 7 of 32 (3 to 12) |
| data/clock/pi05_thr70 | gru_phys_ttp_s1 | 0.017 | -32 (15) | 7 of 32 (3 to 12) | 0.013 | -32 (15) | 7 of 32 (3 to 12) |
| data/clock/pi05_thr70 | gru_phys_ttp_s2 | 0.008 | +88 (5) | 4 of 32 (1 to 8) | 0.006 | -40 (4) | 2 of 32 (0 to 5) |
| data/clock/pi05_thr70 | gru_phys_ttp_s3 | 0.005 | -128 (6) | 1 of 32 (0 to 3) | 0.003 | -144 (5) | 1 of 32 (0 to 3) |
| data/clock/pi05_thr70 | gru_phys_ttp_s4 | 0.008 | -24 (10) | 4 of 32 (1 to 8) | 0.003 | +32 (6) | 3 of 32 (0 to 7) |
| data/clock/pi05_thr70 | gru_phys_ttp_ens | 0.006 | -68 (12) | 4 of 32 (1 to 8) | 0.003 | +24 (8) | 4 of 32 (1 to 8) |
| data/clock/pi05_thr70 | or_progress_ttp_s0 | 0.032 | -84 (30) | 9 of 32 (4 to 14) | 0.017 | -96 (27) | 8 of 32 (3 to 13) |
| data/clock/pi05_thr70 | or_progress_ttp_s1 | 0.033 | -84 (30) | 10 of 32 (5 to 15) | 0.024 | -128 (29) | 8 of 32 (3 to 13) |
| data/clock/pi05_thr70 | or_progress_ttp_s2 | 0.032 | -96 (29) | 5 of 32 (1 to 9) | 0.016 | -164 (24) | 3 of 32 (0 to 7) |
| data/clock/pi05_thr70 | or_progress_ttp_s3 | 0.028 | -112 (28) | 4 of 32 (1 to 8) | 0.013 | -160 (23) | 3 of 32 (0 to 7) |
| data/clock/pi05_thr70 | or_progress_ttp_s4 | 0.029 | -112 (28) | 6 of 32 (2 to 10) | 0.015 | -160 (24) | 5 of 32 (1 to 9) |
| data/clock/pi05_thr70 | or_progress_ens | 0.028 | -96 (30) | 7 of 32 (3 to 12) | 0.014 | -148 (24) | 5 of 32 (1 to 9) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/clock/pi05_thr70 | progress | 3 of 32 (0 to 7) | 23 / 6 |  | +112 (26) | 23 of 928 (0.025) | 3 of 4 | 0.021 of 475 / 0.029 of 453 |
| data/clock/pi05_thr70 | gru_phys_ttp_s0 | 7 of 32 (3 to 12) | 6 / 19 | +4 (-2 to +10) | -24 (13) | 7 of 928 (0.008) | 0 of 4 | 0.004 of 475 / 0.011 of 453 |
| data/clock/pi05_thr70 | gru_phys_ttp_s1 | 7 of 32 (3 to 12) | 8 / 17 | +4 (-2 to +10) | +32 (15) | 12 of 928 (0.013) | 1 of 4 | 0.004 of 475 / 0.022 of 453 |
| data/clock/pi05_thr70 | gru_phys_ttp_s2 | 2 of 32 (0 to 5) | 2 / 28 | -1 (-5 to +3) | +40 (4) | 6 of 928 (0.006) | 0 of 4 | 0.000 of 475 / 0.013 of 453 |
| data/clock/pi05_thr70 | gru_phys_ttp_s3 | 1 of 32 (0 to 3) | 4 / 27 | -2 (-6 to +2) | +144 (5) | 3 of 928 (0.003) | 1 of 4 | 0.000 of 475 / 0.007 of 453 |
| data/clock/pi05_thr70 | gru_phys_ttp_s4 | 3 of 32 (0 to 7) | 3 / 26 | +0 (-5 to +5) | -32 (6) | 3 of 928 (0.003) | 0 of 4 | 0.000 of 475 / 0.007 of 453 |
| data/clock/pi05_thr70 | gru_phys_ttp_ens | 4 of 32 (1 to 8) | 4 / 24 | +1 (-4 to +6) | -24 (8) | 3 of 928 (0.003) | 0 of 4 | 0.000 of 475 / 0.007 of 453 |
| data/clock/pi05_thr70 | or_progress_ttp_s0 | 8 of 32 (4 to 13) | 19 / 5 | +5 (+0 to +10) | +96 (27) | 16 of 928 (0.017) | 2 of 4 | 0.013 of 475 / 0.022 of 453 |
| data/clock/pi05_thr70 | or_progress_ttp_s1 | 8 of 32 (4 to 13) | 21 / 3 | +5 (+0 to +10) | +128 (29) | 22 of 928 (0.024) | 3 of 4 | 0.013 of 475 / 0.035 of 453 |
| data/clock/pi05_thr70 | or_progress_ttp_s2 | 3 of 32 (0 to 7) | 21 / 8 | +0 (-3 to +3) | +164 (24) | 15 of 928 (0.016) | 2 of 4 | 0.011 of 475 / 0.022 of 453 |
| data/clock/pi05_thr70 | or_progress_ttp_s3 | 3 of 32 (0 to 7) | 20 / 9 | +0 (-3 to +3) | +160 (23) | 12 of 928 (0.013) | 3 of 4 | 0.011 of 475 / 0.015 of 453 |
| data/clock/pi05_thr70 | or_progress_ttp_s4 | 5 of 32 (1 to 9) | 19 / 8 | +2 (-2 to +6) | +160 (24) | 14 of 928 (0.015) | 2 of 4 | 0.011 of 475 / 0.020 of 453 |
| data/clock/pi05_thr70 | or_progress_ens | 5 of 32 (1 to 9) | 19 / 8 | +2 (-2 to +6) | +148 (24) | 13 of 928 (0.014) | 2 of 4 | 0.011 of 475 / 0.018 of 453 |
