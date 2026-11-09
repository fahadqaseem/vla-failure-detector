# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/pi05_fresh/thr70/unseen/merged | 0.05 | gru_phys_ttp_s0 | 0 vs 4 of 5 | -4 (-5 to -2) | 16 vs 25 of 633 | -9 (-21 to +3) |
| data/pi05_fresh/thr70/unseen/merged | 0.05 | gru_phys_ttp_s1 | 2 vs 4 of 5 | -2 (-5 to +2) | 19 vs 25 of 633 | -6 (-18 to +6) |
| data/pi05_fresh/thr70/unseen/merged | 0.05 | gru_phys_ttp_s2 | 0 vs 4 of 5 | -4 (-5 to -2) | 9 vs 25 of 633 | -16 (-27 to -5) |
| data/pi05_fresh/thr70/unseen/merged | 0.05 | gru_phys_ttp_s3 | 1 vs 4 of 5 | -3 (-5 to +1) | 5 vs 25 of 633 | -20 (-31 to -10) |
| data/pi05_fresh/thr70/unseen/merged | 0.05 | gru_phys_ttp_s4 | 0 vs 4 of 5 | -4 (-5 to -2) | 10 vs 25 of 633 | -15 (-26 to -4) |
| data/pi05_fresh/thr70/unseen/merged | 0.05 | gru_phys_ttp_ens | 0 vs 4 of 5 | -4 (-5 to -2) | 8 vs 25 of 633 | -17 (-28 to -6) |
| data/pi05_fresh/thr70/unseen/merged | 0.05 | or_progress_ens | 4 vs 4 of 5 | +0 (+0 to +0) | 15 vs 25 of 633 | -10 (-18 to -2) |
| data/pi05_fresh/thr70/unseen/merged | 0.025 | gru_phys_ttp_s0 | 0 vs 4 of 5 | -4 (-5 to -2) | 10 vs 10 of 633 | +0 (-8 to +8) |
| data/pi05_fresh/thr70/unseen/merged | 0.025 | gru_phys_ttp_s1 | 2 vs 4 of 5 | -2 (-5 to +2) | 11 vs 10 of 633 | +1 (-7 to +10) |
| data/pi05_fresh/thr70/unseen/merged | 0.025 | gru_phys_ttp_s2 | 0 vs 4 of 5 | -4 (-5 to -2) | 4 vs 10 of 633 | -6 (-13 to +1) |
| data/pi05_fresh/thr70/unseen/merged | 0.025 | gru_phys_ttp_s3 | 1 vs 4 of 5 | -3 (-5 to +1) | 3 vs 10 of 633 | -7 (-14 to -1) |
| data/pi05_fresh/thr70/unseen/merged | 0.025 | gru_phys_ttp_s4 | 0 vs 4 of 5 | -4 (-5 to -2) | 5 vs 10 of 633 | -5 (-12 to +2) |
| data/pi05_fresh/thr70/unseen/merged | 0.025 | gru_phys_ttp_ens | 0 vs 4 of 5 | -4 (-5 to -2) | 4 vs 10 of 633 | -6 (-13 to +1) |
| data/pi05_fresh/thr70/unseen/merged | 0.025 | or_progress_ens | 2 vs 4 of 5 | -2 (-4 to +0) | 7 vs 10 of 633 | -3 (-8 to +1) |
