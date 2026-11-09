# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/pi05_fresh/thr70/seen/merged | progress | 0.033 | -96 (26) | 7 of 28 (3 to 12) | 0.014 | -124 (24) | 7 of 28 (3 to 12) |
| data/pi05_fresh/thr70/seen/merged | gru_phys_ttp_s0 | 0.002 | +24 (1) | 1 of 28 (0 to 3) | 0.002 | +8 (1) | 1 of 28 (0 to 3) |
| data/pi05_fresh/thr70/seen/merged | gru_phys_ttp_s1 | 0.006 | -80 (7) | 2 of 28 (0 to 5) | 0.005 | -92 (6) | 1 of 28 (0 to 3) |
| data/pi05_fresh/thr70/seen/merged | gru_phys_ttp_s2 | 0.006 | -80 (4) | 1 of 28 (0 to 3) | 0.006 | -104 (3) | 1 of 28 (0 to 3) |
| data/pi05_fresh/thr70/seen/merged | gru_phys_ttp_s3 | 0.005 | -72 (4) | 1 of 28 (0 to 3) | 0.002 | -36 (2) | 0 of 28 (0 to 0) |
| data/pi05_fresh/thr70/seen/merged | gru_phys_ttp_s4 | 0.006 | -56 (5) | 1 of 28 (0 to 3) | 0.005 | -72 (5) | 1 of 28 (0 to 3) |
| data/pi05_fresh/thr70/seen/merged | gru_phys_ttp_ens | 0.005 | -64 (3) | 1 of 28 (0 to 3) | 0.005 | -80 (3) | 1 of 28 (0 to 3) |
| data/pi05_fresh/thr70/seen/merged | or_progress_ens | 0.019 | -112 (24) | 8 of 28 (4 to 13) | 0.011 | -160 (22) | 6 of 28 (2 to 10) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/pi05_fresh/thr70/seen/merged | progress | 7 of 28 (3 to 12) | 19 / 2 |  | +96 (26) | 21 of 633 (0.033) | 4 of 5 | none / 0.033 of 633 |
| data/pi05_fresh/thr70/seen/merged | gru_phys_ttp_s0 | 1 of 28 (0 to 3) | 0 / 27 | -6 (-11 to -1) | -24 (1) | 1 of 633 (0.002) | 0 of 5 | none / 0.002 of 633 |
| data/pi05_fresh/thr70/seen/merged | gru_phys_ttp_s1 | 2 of 28 (0 to 5) | 5 / 21 | -5 (-11 to +0) | +80 (7) | 4 of 633 (0.006) | 0 of 5 | none / 0.006 of 633 |
| data/pi05_fresh/thr70/seen/merged | gru_phys_ttp_s2 | 1 of 28 (0 to 3) | 3 / 24 | -6 (-11 to -1) | +80 (4) | 4 of 633 (0.006) | 0 of 5 | none / 0.006 of 633 |
| data/pi05_fresh/thr70/seen/merged | gru_phys_ttp_s3 | 1 of 28 (0 to 3) | 3 / 24 | -6 (-11 to -1) | +72 (4) | 3 of 633 (0.005) | 0 of 5 | none / 0.005 of 633 |
| data/pi05_fresh/thr70/seen/merged | gru_phys_ttp_s4 | 1 of 28 (0 to 3) | 4 / 23 | -6 (-11 to -1) | +56 (5) | 4 of 633 (0.006) | 0 of 5 | none / 0.006 of 633 |
| data/pi05_fresh/thr70/seen/merged | gru_phys_ttp_ens | 1 of 28 (0 to 3) | 2 / 25 | -6 (-11 to -1) | +64 (3) | 3 of 633 (0.005) | 0 of 5 | none / 0.005 of 633 |
| data/pi05_fresh/thr70/seen/merged | or_progress_ens | 8 of 28 (4 to 13) | 16 / 4 | +1 (+0 to +3) | +112 (24) | 12 of 633 (0.019) | 3 of 5 | none / 0.019 of 633 |
