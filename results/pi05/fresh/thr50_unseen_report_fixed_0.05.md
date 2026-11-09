# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/pi05_fresh/thr50/unseen/merged | progress | 0.039 | -120 (21) | 4 of 23 (1 to 8) | 0.016 | -144 (19) | 4 of 23 (1 to 8) |
| data/pi05_fresh/thr50/unseen/merged | gru_phys_ttp_s0 | 0.011 | -68 (6) | 1 of 23 (0 to 3) | 0.008 | -36 (4) | 1 of 23 (0 to 3) |
| data/pi05_fresh/thr50/unseen/merged | gru_phys_ttp_s1 | 0.038 | -36 (6) | 2 of 23 (0 to 5) | 0.022 | -36 (6) | 2 of 23 (0 to 5) |
| data/pi05_fresh/thr50/unseen/merged | gru_phys_ttp_s2 | 0.008 | -128 (3) | 1 of 23 (0 to 3) | 0.005 | -128 (3) | 1 of 23 (0 to 3) |
| data/pi05_fresh/thr50/unseen/merged | gru_phys_ttp_s3 | 0.008 | +112 (2) | 2 of 23 (0 to 5) | 0.005 | +16 (1) | 1 of 23 (0 to 3) |
| data/pi05_fresh/thr50/unseen/merged | gru_phys_ttp_s4 | 0.008 | -80 (6) | 1 of 23 (0 to 3) | 0.002 | -88 (4) | 1 of 23 (0 to 3) |
| data/pi05_fresh/thr50/unseen/merged | gru_phys_ttp_ens | 0.006 | -100 (4) | 1 of 23 (0 to 3) | 0.002 | -128 (4) | 1 of 23 (0 to 3) |
| data/pi05_fresh/thr50/unseen/merged | or_progress_ens | 0.021 | -136 (19) | 5 of 23 (2 to 9) | 0.009 | -168 (18) | 3 of 23 (0 to 6) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/pi05_fresh/thr50/unseen/merged | progress | 4 of 23 (1 to 8) | 17 / 2 |  | +120 (21) | 25 of 633 (0.039) | 4 of 5 | none / 0.039 of 633 |
| data/pi05_fresh/thr50/unseen/merged | gru_phys_ttp_s0 | 1 of 23 (0 to 3) | 5 / 17 | -3 (-7 to +1) | +68 (6) | 7 of 633 (0.011) | 1 of 5 | none / 0.011 of 633 |
| data/pi05_fresh/thr50/unseen/merged | gru_phys_ttp_s1 | 2 of 23 (0 to 5) | 4 / 17 | -2 (-7 to +3) | +36 (6) | 24 of 633 (0.038) | 1 of 5 | none / 0.038 of 633 |
| data/pi05_fresh/thr50/unseen/merged | gru_phys_ttp_s2 | 1 of 23 (0 to 3) | 2 / 20 | -3 (-7 to +1) | +128 (3) | 5 of 633 (0.008) | 1 of 5 | none / 0.008 of 633 |
| data/pi05_fresh/thr50/unseen/merged | gru_phys_ttp_s3 | 2 of 23 (0 to 5) | 0 / 21 | -2 (-7 to +3) | -112 (2) | 5 of 633 (0.008) | 2 of 5 | none / 0.008 of 633 |
| data/pi05_fresh/thr50/unseen/merged | gru_phys_ttp_s4 | 1 of 23 (0 to 3) | 5 / 17 | -3 (-7 to +1) | +80 (6) | 5 of 633 (0.008) | 0 of 5 | none / 0.008 of 633 |
| data/pi05_fresh/thr50/unseen/merged | gru_phys_ttp_ens | 1 of 23 (0 to 3) | 3 / 19 | -3 (-7 to +1) | +100 (4) | 4 of 633 (0.006) | 0 of 5 | none / 0.006 of 633 |
| data/pi05_fresh/thr50/unseen/merged | or_progress_ens | 5 of 23 (2 to 9) | 14 / 4 | +1 (+0 to +3) | +136 (19) | 13 of 633 (0.021) | 4 of 5 | none / 0.021 of 633 |
