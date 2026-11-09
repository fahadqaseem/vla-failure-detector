# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/pi05_fresh/thr80/seen/merged | progress | 0.033 | -48 (22) | 8 of 24 (4 to 13) | 0.014 | -80 (21) | 8 of 24 (4 to 13) |
| data/pi05_fresh/thr80/seen/merged | gru_phys_ttp_s0 | 0.002 | +112 (1) | 1 of 24 (0 to 3) | 0.002 | +24 (1) | 1 of 24 (0 to 3) |
| data/pi05_fresh/thr80/seen/merged | gru_phys_ttp_s1 | 0.005 | +40 (4) | 3 of 24 (0 to 6) | 0.005 | +136 (1) | 1 of 24 (0 to 3) |
| data/pi05_fresh/thr80/seen/merged | gru_phys_ttp_s2 | 0.002 | +56 (3) | 2 of 24 (0 to 5) | 0.002 | +72 (2) | 2 of 24 (0 to 5) |
| data/pi05_fresh/thr80/seen/merged | gru_phys_ttp_s3 | 0.002 | +72 (3) | 2 of 24 (0 to 5) | 0.002 | +40 (1) | 1 of 24 (0 to 3) |
| data/pi05_fresh/thr80/seen/merged | gru_phys_ttp_s4 | 0.002 | +8 (2) | 1 of 24 (0 to 3) | 0.002 | +24 (1) | 1 of 24 (0 to 3) |
| data/pi05_fresh/thr80/seen/merged | gru_phys_ttp_ens | 0.002 | +72 (3) | 3 of 24 (0 to 6) | 0.002 | +32 (1) | 1 of 24 (0 to 3) |
| data/pi05_fresh/thr80/seen/merged | or_progress_ens | 0.016 | -48 (21) | 9 of 24 (5 to 14) | 0.008 | -96 (18) | 8 of 24 (4 to 13) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/pi05_fresh/thr80/seen/merged | progress | 8 of 24 (4 to 13) | 13 / 3 |  | +80 (21) | 9 of 633 (0.014) | 7 of 10 | none / 0.014 of 633 |
| data/pi05_fresh/thr80/seen/merged | gru_phys_ttp_s0 | 1 of 24 (0 to 3) | 0 / 23 | -7 (-12 to -2) | -24 (1) | 1 of 633 (0.002) | 0 of 10 | none / 0.002 of 633 |
| data/pi05_fresh/thr80/seen/merged | gru_phys_ttp_s1 | 1 of 24 (0 to 3) | 0 / 23 | -7 (-12 to -2) | -136 (1) | 3 of 633 (0.005) | 0 of 10 | none / 0.005 of 633 |
| data/pi05_fresh/thr80/seen/merged | gru_phys_ttp_s2 | 2 of 24 (0 to 5) | 0 / 22 | -6 (-11 to -1) | -72 (2) | 1 of 633 (0.002) | 0 of 10 | none / 0.002 of 633 |
| data/pi05_fresh/thr80/seen/merged | gru_phys_ttp_s3 | 1 of 24 (0 to 3) | 0 / 23 | -7 (-12 to -2) | -40 (1) | 1 of 633 (0.002) | 0 of 10 | none / 0.002 of 633 |
| data/pi05_fresh/thr80/seen/merged | gru_phys_ttp_s4 | 1 of 24 (0 to 3) | 0 / 23 | -7 (-12 to -2) | -24 (1) | 1 of 633 (0.002) | 0 of 10 | none / 0.002 of 633 |
| data/pi05_fresh/thr80/seen/merged | gru_phys_ttp_ens | 1 of 24 (0 to 3) | 0 / 23 | -7 (-12 to -2) | -32 (1) | 1 of 633 (0.002) | 0 of 10 | none / 0.002 of 633 |
| data/pi05_fresh/thr80/seen/merged | or_progress_ens | 8 of 24 (4 to 13) | 10 / 6 | +0 (-3 to +3) | +96 (18) | 5 of 633 (0.008) | 5 of 10 | none / 0.008 of 633 |
