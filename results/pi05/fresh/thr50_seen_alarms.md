# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/pi05_fresh/thr50/seen/merged | 0.05 | gru_phys_ttp_s0 | 0 vs 4 of 5 | -4 (-5 to -2) | 3 vs 21 of 633 | -18 (-27 to -9) |
| data/pi05_fresh/thr50/seen/merged | 0.05 | gru_phys_ttp_s1 | 1 vs 4 of 5 | -3 (-5 to +1) | 6 vs 21 of 633 | -15 (-25 to -5) |
| data/pi05_fresh/thr50/seen/merged | 0.05 | gru_phys_ttp_s2 | 0 vs 4 of 5 | -4 (-5 to -2) | 6 vs 21 of 633 | -15 (-25 to -5) |
| data/pi05_fresh/thr50/seen/merged | 0.05 | gru_phys_ttp_s3 | 0 vs 4 of 5 | -4 (-5 to -2) | 6 vs 21 of 633 | -15 (-25 to -5) |
| data/pi05_fresh/thr50/seen/merged | 0.05 | gru_phys_ttp_s4 | 0 vs 4 of 5 | -4 (-5 to -2) | 8 vs 21 of 633 | -13 (-23 to -3) |
| data/pi05_fresh/thr50/seen/merged | 0.05 | gru_phys_ttp_ens | 0 vs 4 of 5 | -4 (-5 to -2) | 6 vs 21 of 633 | -15 (-25 to -5) |
| data/pi05_fresh/thr50/seen/merged | 0.05 | or_progress_ens | 3 vs 4 of 5 | -1 (-3 to +0) | 13 vs 21 of 633 | -8 (-16 to +0) |
| data/pi05_fresh/thr50/seen/merged | 0.025 | gru_phys_ttp_s0 | 0 vs 3 of 5 | -3 (-5 to -1) | 2 vs 9 of 633 | -7 (-14 to -1) |
| data/pi05_fresh/thr50/seen/merged | 0.025 | gru_phys_ttp_s1 | 0 vs 3 of 5 | -3 (-5 to -1) | 6 vs 9 of 633 | -3 (-10 to +4) |
| data/pi05_fresh/thr50/seen/merged | 0.025 | gru_phys_ttp_s2 | 0 vs 3 of 5 | -3 (-5 to -1) | 5 vs 9 of 633 | -4 (-11 to +3) |
| data/pi05_fresh/thr50/seen/merged | 0.025 | gru_phys_ttp_s3 | 0 vs 3 of 5 | -3 (-5 to -1) | 5 vs 9 of 633 | -4 (-11 to +3) |
| data/pi05_fresh/thr50/seen/merged | 0.025 | gru_phys_ttp_s4 | 0 vs 3 of 5 | -3 (-5 to -1) | 5 vs 9 of 633 | -4 (-11 to +3) |
| data/pi05_fresh/thr50/seen/merged | 0.025 | gru_phys_ttp_ens | 0 vs 3 of 5 | -3 (-5 to -1) | 5 vs 9 of 633 | -4 (-11 to +3) |
| data/pi05_fresh/thr50/seen/merged | 0.025 | or_progress_ens | 1 vs 3 of 5 | -2 (-4 to +0) | 7 vs 9 of 633 | -2 (-8 to +3) |
