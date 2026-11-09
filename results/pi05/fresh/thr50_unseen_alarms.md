# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/pi05_fresh/thr50/unseen/merged | 0.05 | gru_phys_ttp_s0 | 1 vs 4 of 5 | -3 (-5 to +1) | 7 vs 25 of 633 | -18 (-29 to -7) |
| data/pi05_fresh/thr50/unseen/merged | 0.05 | gru_phys_ttp_s1 | 1 vs 4 of 5 | -3 (-5 to -1) | 24 vs 25 of 633 | -1 (-14 to +12) |
| data/pi05_fresh/thr50/unseen/merged | 0.05 | gru_phys_ttp_s2 | 1 vs 4 of 5 | -3 (-5 to -1) | 5 vs 25 of 633 | -20 (-31 to -9) |
| data/pi05_fresh/thr50/unseen/merged | 0.05 | gru_phys_ttp_s3 | 2 vs 4 of 5 | -2 (-5 to +2) | 5 vs 25 of 633 | -20 (-31 to -9) |
| data/pi05_fresh/thr50/unseen/merged | 0.05 | gru_phys_ttp_s4 | 0 vs 4 of 5 | -4 (-5 to -2) | 5 vs 25 of 633 | -20 (-31 to -10) |
| data/pi05_fresh/thr50/unseen/merged | 0.05 | gru_phys_ttp_ens | 0 vs 4 of 5 | -4 (-5 to -2) | 4 vs 25 of 633 | -21 (-32 to -11) |
| data/pi05_fresh/thr50/unseen/merged | 0.05 | or_progress_ens | 4 vs 4 of 5 | +0 (+0 to +0) | 13 vs 25 of 633 | -12 (-20 to -5) |
| data/pi05_fresh/thr50/unseen/merged | 0.025 | gru_phys_ttp_s0 | 1 vs 4 of 5 | -3 (-5 to +1) | 5 vs 10 of 633 | -5 (-12 to +2) |
| data/pi05_fresh/thr50/unseen/merged | 0.025 | gru_phys_ttp_s1 | 1 vs 4 of 5 | -3 (-5 to -1) | 14 vs 10 of 633 | +4 (-5 to +13) |
| data/pi05_fresh/thr50/unseen/merged | 0.025 | gru_phys_ttp_s2 | 0 vs 4 of 5 | -4 (-5 to -2) | 3 vs 10 of 633 | -7 (-14 to +0) |
| data/pi05_fresh/thr50/unseen/merged | 0.025 | gru_phys_ttp_s3 | 2 vs 4 of 5 | -2 (-5 to +2) | 3 vs 10 of 633 | -7 (-14 to +0) |
| data/pi05_fresh/thr50/unseen/merged | 0.025 | gru_phys_ttp_s4 | 0 vs 4 of 5 | -4 (-5 to -2) | 1 vs 10 of 633 | -9 (-16 to -3) |
| data/pi05_fresh/thr50/unseen/merged | 0.025 | gru_phys_ttp_ens | 0 vs 4 of 5 | -4 (-5 to -2) | 1 vs 10 of 633 | -9 (-16 to -3) |
| data/pi05_fresh/thr50/unseen/merged | 0.025 | or_progress_ens | 2 vs 4 of 5 | -2 (-4 to +0) | 6 vs 10 of 633 | -4 (-9 to +0) |
