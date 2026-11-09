# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/pi05_fresh/thr80/unseen/merged | progress | 0.039 | -44 (22) | 8 of 24 (4 to 13) | 0.016 | -72 (21) | 8 of 24 (4 to 13) |
| data/pi05_fresh/thr80/unseen/merged | gru_phys_ttp_s0 | 0.008 | +160 (3) | 3 of 24 (0 to 6) | 0.008 | +184 (2) | 2 of 24 (0 to 5) |
| data/pi05_fresh/thr80/unseen/merged | gru_phys_ttp_s1 | 0.019 | +160 (2) | 2 of 24 (0 to 5) | 0.008 | +140 (2) | 2 of 24 (0 to 5) |
| data/pi05_fresh/thr80/unseen/merged | gru_phys_ttp_s2 | 0.005 | +96 (3) | 3 of 24 (0 to 6) | 0.002 | +96 (3) | 3 of 24 (0 to 6) |
| data/pi05_fresh/thr80/unseen/merged | gru_phys_ttp_s3 | 0.003 | +24 (1) | 1 of 24 (0 to 3) | 0.002 | +16 (1) | 1 of 24 (0 to 3) |
| data/pi05_fresh/thr80/unseen/merged | gru_phys_ttp_s4 | 0.002 | +96 (3) | 3 of 24 (0 to 6) | 0.002 | +120 (2) | 2 of 24 (0 to 5) |
| data/pi05_fresh/thr80/unseen/merged | gru_phys_ttp_ens | 0.003 | +88 (3) | 3 of 24 (0 to 6) | 0.002 | +80 (3) | 3 of 24 (0 to 6) |
| data/pi05_fresh/thr80/unseen/merged | or_progress_ens | 0.019 | +24 (21) | 11 of 24 (6 to 16) | 0.008 | -96 (17) | 7 of 24 (3 to 12) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/pi05_fresh/thr80/unseen/merged | progress | 8 of 24 (4 to 13) | 14 / 2 |  | +44 (22) | 25 of 633 (0.039) | 9 of 10 | none / 0.039 of 633 |
| data/pi05_fresh/thr80/unseen/merged | gru_phys_ttp_s0 | 3 of 24 (0 to 6) | 0 / 21 | -5 (-11 to +1) | -160 (3) | 5 of 633 (0.008) | 1 of 10 | none / 0.008 of 633 |
| data/pi05_fresh/thr80/unseen/merged | gru_phys_ttp_s1 | 2 of 24 (0 to 5) | 0 / 22 | -6 (-12 to +0) | -160 (2) | 12 of 633 (0.019) | 2 of 10 | none / 0.019 of 633 |
| data/pi05_fresh/thr80/unseen/merged | gru_phys_ttp_s2 | 3 of 24 (0 to 6) | 0 / 21 | -5 (-11 to +1) | -96 (3) | 3 of 633 (0.005) | 1 of 10 | none / 0.005 of 633 |
| data/pi05_fresh/thr80/unseen/merged | gru_phys_ttp_s3 | 1 of 24 (0 to 3) | 0 / 23 | -7 (-12 to -2) | -24 (1) | 2 of 633 (0.003) | 1 of 10 | none / 0.003 of 633 |
| data/pi05_fresh/thr80/unseen/merged | gru_phys_ttp_s4 | 3 of 24 (0 to 6) | 0 / 21 | -5 (-11 to +1) | -96 (3) | 1 of 633 (0.002) | 1 of 10 | none / 0.002 of 633 |
| data/pi05_fresh/thr80/unseen/merged | gru_phys_ttp_ens | 3 of 24 (0 to 6) | 0 / 21 | -5 (-11 to +1) | -88 (3) | 2 of 633 (0.003) | 1 of 10 | none / 0.003 of 633 |
| data/pi05_fresh/thr80/unseen/merged | or_progress_ens | 11 of 24 (6 to 16) | 10 / 3 | +3 (+0 to +6) | -24 (21) | 12 of 633 (0.019) | 8 of 10 | none / 0.019 of 633 |
