# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/pi05_fresh/thr70/unseen/merged | progress | 0.039 | -88 (26) | 7 of 28 (3 to 12) | 0.016 | -120 (24) | 7 of 28 (3 to 12) |
| data/pi05_fresh/thr70/unseen/merged | gru_phys_ttp_s0 | 0.025 | +32 (6) | 4 of 28 (1 to 8) | 0.016 | +24 (6) | 4 of 28 (1 to 8) |
| data/pi05_fresh/thr70/unseen/merged | gru_phys_ttp_s1 | 0.030 | +40 (7) | 5 of 28 (1 to 9) | 0.017 | +36 (6) | 4 of 28 (1 to 8) |
| data/pi05_fresh/thr70/unseen/merged | gru_phys_ttp_s2 | 0.014 | +88 (3) | 3 of 28 (0 to 7) | 0.006 | +24 (3) | 3 of 28 (0 to 7) |
| data/pi05_fresh/thr70/unseen/merged | gru_phys_ttp_s3 | 0.008 | +64 (2) | 2 of 28 (0 to 5) | 0.005 | +56 (2) | 2 of 28 (0 to 5) |
| data/pi05_fresh/thr70/unseen/merged | gru_phys_ttp_s4 | 0.016 | +16 (5) | 3 of 28 (0 to 7) | 0.008 | +0 (5) | 3 of 28 (0 to 7) |
| data/pi05_fresh/thr70/unseen/merged | gru_phys_ttp_ens | 0.013 | +24 (5) | 3 of 28 (0 to 7) | 0.006 | +16 (5) | 3 of 28 (0 to 7) |
| data/pi05_fresh/thr70/unseen/merged | or_progress_ens | 0.024 | -84 (24) | 10 of 28 (5 to 15) | 0.011 | -128 (22) | 8 of 28 (4 to 13) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/pi05_fresh/thr70/unseen/merged | progress | 7 of 28 (3 to 12) | 19 / 2 |  | +88 (26) | 25 of 633 (0.039) | 4 of 5 | none / 0.039 of 633 |
| data/pi05_fresh/thr70/unseen/merged | gru_phys_ttp_s0 | 4 of 28 (1 to 8) | 2 / 22 | -3 (-9 to +3) | -32 (6) | 16 of 633 (0.025) | 0 of 5 | none / 0.025 of 633 |
| data/pi05_fresh/thr70/unseen/merged | gru_phys_ttp_s1 | 5 of 28 (1 to 9) | 2 / 21 | -2 (-8 to +4) | -40 (7) | 19 of 633 (0.030) | 2 of 5 | none / 0.030 of 633 |
| data/pi05_fresh/thr70/unseen/merged | gru_phys_ttp_s2 | 3 of 28 (0 to 6) | 0 / 25 | -4 (-10 to +2) | -88 (3) | 9 of 633 (0.014) | 0 of 5 | none / 0.014 of 633 |
| data/pi05_fresh/thr70/unseen/merged | gru_phys_ttp_s3 | 2 of 28 (0 to 5) | 0 / 26 | -5 (-10 to +0) | -64 (2) | 5 of 633 (0.008) | 1 of 5 | none / 0.008 of 633 |
| data/pi05_fresh/thr70/unseen/merged | gru_phys_ttp_s4 | 3 of 28 (0 to 6) | 2 / 23 | -4 (-10 to +2) | -16 (5) | 10 of 633 (0.016) | 0 of 5 | none / 0.016 of 633 |
| data/pi05_fresh/thr70/unseen/merged | gru_phys_ttp_ens | 3 of 28 (0 to 6) | 2 / 23 | -4 (-10 to +2) | -24 (5) | 8 of 633 (0.013) | 0 of 5 | none / 0.013 of 633 |
| data/pi05_fresh/thr70/unseen/merged | or_progress_ens | 10 of 28 (5 to 15) | 14 / 4 | +3 (+0 to +6) | +84 (24) | 15 of 633 (0.024) | 4 of 5 | none / 0.024 of 633 |
