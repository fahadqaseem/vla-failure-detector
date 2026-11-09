# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/pi05_fresh/thr70/seen/merged | 0.05 | gru_phys_ttp_s0 | 0 vs 4 of 5 | -4 (-5 to -2) | 1 vs 21 of 633 | -20 (-29 to -11) |
| data/pi05_fresh/thr70/seen/merged | 0.05 | gru_phys_ttp_s1 | 0 vs 4 of 5 | -4 (-5 to -2) | 4 vs 21 of 633 | -17 (-27 to -8) |
| data/pi05_fresh/thr70/seen/merged | 0.05 | gru_phys_ttp_s2 | 0 vs 4 of 5 | -4 (-5 to -2) | 4 vs 21 of 633 | -17 (-27 to -7) |
| data/pi05_fresh/thr70/seen/merged | 0.05 | gru_phys_ttp_s3 | 0 vs 4 of 5 | -4 (-5 to -2) | 3 vs 21 of 633 | -18 (-28 to -9) |
| data/pi05_fresh/thr70/seen/merged | 0.05 | gru_phys_ttp_s4 | 0 vs 4 of 5 | -4 (-5 to -2) | 4 vs 21 of 633 | -17 (-27 to -7) |
| data/pi05_fresh/thr70/seen/merged | 0.05 | gru_phys_ttp_ens | 0 vs 4 of 5 | -4 (-5 to -2) | 3 vs 21 of 633 | -18 (-28 to -9) |
| data/pi05_fresh/thr70/seen/merged | 0.05 | or_progress_ens | 3 vs 4 of 5 | -1 (-3 to +0) | 12 vs 21 of 633 | -9 (-17 to -2) |
| data/pi05_fresh/thr70/seen/merged | 0.025 | gru_phys_ttp_s0 | 0 vs 3 of 5 | -3 (-5 to -1) | 1 vs 9 of 633 | -8 (-15 to -2) |
| data/pi05_fresh/thr70/seen/merged | 0.025 | gru_phys_ttp_s1 | 0 vs 3 of 5 | -3 (-5 to -1) | 3 vs 9 of 633 | -6 (-13 to +1) |
| data/pi05_fresh/thr70/seen/merged | 0.025 | gru_phys_ttp_s2 | 0 vs 3 of 5 | -3 (-5 to -1) | 4 vs 9 of 633 | -5 (-12 to +2) |
| data/pi05_fresh/thr70/seen/merged | 0.025 | gru_phys_ttp_s3 | 0 vs 3 of 5 | -3 (-5 to -1) | 1 vs 9 of 633 | -8 (-15 to -2) |
| data/pi05_fresh/thr70/seen/merged | 0.025 | gru_phys_ttp_s4 | 0 vs 3 of 5 | -3 (-5 to -1) | 3 vs 9 of 633 | -6 (-13 to +1) |
| data/pi05_fresh/thr70/seen/merged | 0.025 | gru_phys_ttp_ens | 0 vs 3 of 5 | -3 (-5 to -1) | 3 vs 9 of 633 | -6 (-13 to +1) |
| data/pi05_fresh/thr70/seen/merged | 0.025 | or_progress_ens | 1 vs 3 of 5 | -2 (-4 to +0) | 7 vs 9 of 633 | -2 (-8 to +3) |
