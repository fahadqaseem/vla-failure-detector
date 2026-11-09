# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/pi05_fresh/thr50/seen/merged | progress | 0.033 | -120 (21) | 4 of 23 (1 to 8) | 0.014 | -152 (19) | 3 of 23 (0 to 7) |
| data/pi05_fresh/thr50/seen/merged | gru_phys_ttp_s0 | 0.005 | -128 (4) | 0 of 23 (0 to 0) | 0.003 | -204 (4) | 0 of 23 (0 to 0) |
| data/pi05_fresh/thr50/seen/merged | gru_phys_ttp_s1 | 0.009 | -116 (4) | 0 of 23 (0 to 0) | 0.009 | -152 (4) | 0 of 23 (0 to 0) |
| data/pi05_fresh/thr50/seen/merged | gru_phys_ttp_s2 | 0.009 | -112 (4) | 0 of 23 (0 to 0) | 0.008 | -120 (4) | 0 of 23 (0 to 0) |
| data/pi05_fresh/thr50/seen/merged | gru_phys_ttp_s3 | 0.009 | -128 (3) | 0 of 23 (0 to 0) | 0.008 | -136 (3) | 0 of 23 (0 to 0) |
| data/pi05_fresh/thr50/seen/merged | gru_phys_ttp_s4 | 0.013 | -272 (7) | 0 of 23 (0 to 0) | 0.008 | -92 (4) | 0 of 23 (0 to 0) |
| data/pi05_fresh/thr50/seen/merged | gru_phys_ttp_ens | 0.009 | -120 (4) | 0 of 23 (0 to 0) | 0.008 | -128 (4) | 0 of 23 (0 to 0) |
| data/pi05_fresh/thr50/seen/merged | or_progress_ens | 0.021 | -144 (19) | 3 of 23 (0 to 7) | 0.011 | -192 (19) | 3 of 23 (0 to 7) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/pi05_fresh/thr50/seen/merged | progress | 3 of 23 (0 to 6) | 16 / 4 |  | +152 (19) | 9 of 633 (0.014) | 3 of 5 | none / 0.014 of 633 |
| data/pi05_fresh/thr50/seen/merged | gru_phys_ttp_s0 | 0 of 23 (0 to 0) | 4 / 19 | -3 (-6 to +0) | +204 (4) | 2 of 633 (0.003) | 0 of 5 | none / 0.003 of 633 |
| data/pi05_fresh/thr50/seen/merged | gru_phys_ttp_s1 | 0 of 23 (0 to 0) | 4 / 19 | -3 (-6 to +0) | +152 (4) | 6 of 633 (0.009) | 0 of 5 | none / 0.009 of 633 |
| data/pi05_fresh/thr50/seen/merged | gru_phys_ttp_s2 | 0 of 23 (0 to 0) | 4 / 19 | -3 (-6 to +0) | +120 (4) | 5 of 633 (0.008) | 0 of 5 | none / 0.008 of 633 |
| data/pi05_fresh/thr50/seen/merged | gru_phys_ttp_s3 | 0 of 23 (0 to 0) | 3 / 20 | -3 (-6 to +0) | +136 (3) | 5 of 633 (0.008) | 0 of 5 | none / 0.008 of 633 |
| data/pi05_fresh/thr50/seen/merged | gru_phys_ttp_s4 | 0 of 23 (0 to 0) | 4 / 19 | -3 (-6 to +0) | +92 (4) | 5 of 633 (0.008) | 0 of 5 | none / 0.008 of 633 |
| data/pi05_fresh/thr50/seen/merged | gru_phys_ttp_ens | 0 of 23 (0 to 0) | 4 / 19 | -3 (-6 to +0) | +128 (4) | 5 of 633 (0.008) | 0 of 5 | none / 0.008 of 633 |
| data/pi05_fresh/thr50/seen/merged | or_progress_ens | 3 of 23 (0 to 6) | 16 / 4 | +0 (+0 to +0) | +192 (19) | 7 of 633 (0.011) | 1 of 5 | none / 0.011 of 633 |
