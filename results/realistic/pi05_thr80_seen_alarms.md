# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/realistic/pi05/thr80/seen/merged | 0.05 | gru_phys_ttp | 4 vs 7 of 8 | -3 (-7 to +1) | 51 vs 44 of 928 | +7 (-9 to +23) |
| data/realistic/pi05/thr80/seen/merged | 0.05 | gru_robot_ttp | 5 vs 7 of 8 | -2 (-5 to +2) | 41 vs 44 of 928 | -3 (-18 to +12) |
| data/realistic/pi05/thr80/seen/merged | 0.05 | gru_robotcontact_ttp | 6 vs 7 of 8 | -1 (-4 to +2) | 47 vs 44 of 928 | +3 (-13 to +19) |
| data/realistic/pi05/thr80/seen/merged | 0.025 | gru_phys_ttp | 3 vs 7 of 8 | -4 (-7 to +0) | 18 vs 19 of 928 | -1 (-12 to +10) |
| data/realistic/pi05/thr80/seen/merged | 0.025 | gru_robot_ttp | 5 vs 7 of 8 | -2 (-5 to +2) | 24 vs 19 of 928 | +5 (-6 to +16) |
| data/realistic/pi05/thr80/seen/merged | 0.025 | gru_robotcontact_ttp | 3 vs 7 of 8 | -4 (-7 to +0) | 25 vs 19 of 928 | +6 (-5 to +17) |
