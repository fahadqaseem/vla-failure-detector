# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/realistic/oft/thr80/seen/merged | 0.05 | gru_phys_ttp | 18 vs 33 of 39 | -15 (-22 to -7) | 58 vs 49 of 1071 | +9 (-7 to +25) |
| data/realistic/oft/thr80/seen/merged | 0.05 | gru_robot_ttp | 17 vs 33 of 39 | -16 (-23 to -9) | 50 vs 49 of 1071 | +1 (-17 to +19) |
| data/realistic/oft/thr80/seen/merged | 0.05 | gru_robotcontact_ttp | 16 vs 33 of 39 | -17 (-24 to -9) | 50 vs 49 of 1071 | +1 (-15 to +18) |
| data/realistic/oft/thr80/seen/merged | 0.025 | gru_phys_ttp | 14 vs 28 of 39 | -14 (-22 to -5) | 25 vs 28 of 1071 | -3 (-15 to +9) |
| data/realistic/oft/thr80/seen/merged | 0.025 | gru_robot_ttp | 13 vs 28 of 39 | -15 (-23 to -6) | 24 vs 28 of 1071 | -4 (-17 to +9) |
| data/realistic/oft/thr80/seen/merged | 0.025 | gru_robotcontact_ttp | 14 vs 28 of 39 | -14 (-23 to -5) | 23 vs 28 of 1071 | -5 (-18 to +8) |
