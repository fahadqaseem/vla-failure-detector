# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/pi05_fresh/thr80/seen/merged | 0.05 | gru_phys_ttp_s0 | 0 vs 9 of 10 | -9 (-10 to -7) | 1 vs 21 of 633 | -20 (-29 to -11) |
| data/pi05_fresh/thr80/seen/merged | 0.05 | gru_phys_ttp_s1 | 0 vs 9 of 10 | -9 (-10 to -7) | 3 vs 21 of 633 | -18 (-28 to -9) |
| data/pi05_fresh/thr80/seen/merged | 0.05 | gru_phys_ttp_s2 | 0 vs 9 of 10 | -9 (-10 to -7) | 1 vs 21 of 633 | -20 (-29 to -11) |
| data/pi05_fresh/thr80/seen/merged | 0.05 | gru_phys_ttp_s3 | 1 vs 9 of 10 | -8 (-10 to -5) | 1 vs 21 of 633 | -20 (-29 to -11) |
| data/pi05_fresh/thr80/seen/merged | 0.05 | gru_phys_ttp_s4 | 0 vs 9 of 10 | -9 (-10 to -7) | 1 vs 21 of 633 | -20 (-29 to -11) |
| data/pi05_fresh/thr80/seen/merged | 0.05 | gru_phys_ttp_ens | 0 vs 9 of 10 | -9 (-10 to -7) | 1 vs 21 of 633 | -20 (-29 to -11) |
| data/pi05_fresh/thr80/seen/merged | 0.05 | or_progress_ens | 7 vs 9 of 10 | -2 (-5 to +0) | 10 vs 21 of 633 | -11 (-18 to -4) |
| data/pi05_fresh/thr80/seen/merged | 0.025 | gru_phys_ttp_s0 | 0 vs 7 of 10 | -7 (-10 to -4) | 1 vs 9 of 633 | -8 (-15 to -2) |
| data/pi05_fresh/thr80/seen/merged | 0.025 | gru_phys_ttp_s1 | 0 vs 7 of 10 | -7 (-10 to -4) | 3 vs 9 of 633 | -6 (-13 to +1) |
| data/pi05_fresh/thr80/seen/merged | 0.025 | gru_phys_ttp_s2 | 0 vs 7 of 10 | -7 (-10 to -4) | 1 vs 9 of 633 | -8 (-15 to -2) |
| data/pi05_fresh/thr80/seen/merged | 0.025 | gru_phys_ttp_s3 | 0 vs 7 of 10 | -7 (-10 to -4) | 1 vs 9 of 633 | -8 (-15 to -2) |
| data/pi05_fresh/thr80/seen/merged | 0.025 | gru_phys_ttp_s4 | 0 vs 7 of 10 | -7 (-10 to -4) | 1 vs 9 of 633 | -8 (-15 to -2) |
| data/pi05_fresh/thr80/seen/merged | 0.025 | gru_phys_ttp_ens | 0 vs 7 of 10 | -7 (-10 to -4) | 1 vs 9 of 633 | -8 (-15 to -2) |
| data/pi05_fresh/thr80/seen/merged | 0.025 | or_progress_ens | 5 vs 7 of 10 | -2 (-5 to +0) | 5 vs 9 of 633 | -4 (-9 to +0) |
