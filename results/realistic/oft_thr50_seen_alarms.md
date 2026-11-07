# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/realistic/oft/thr50/seen/merged | 0.05 | gru_phys_ttp | 18 vs 26 of 31 | -8 (-15 to -1) | 52 vs 49 of 1071 | +3 (-12 to +18) |
| data/realistic/oft/thr50/seen/merged | 0.05 | gru_robot_ttp | 14 vs 26 of 31 | -12 (-18 to -6) | 53 vs 49 of 1071 | +4 (-13 to +21) |
| data/realistic/oft/thr50/seen/merged | 0.05 | gru_robotcontact_ttp | 21 vs 26 of 31 | -5 (-12 to +2) | 52 vs 49 of 1071 | +3 (-13 to +19) |
| data/realistic/oft/thr50/seen/merged | 0.025 | gru_phys_ttp | 10 vs 22 of 31 | -12 (-19 to -4) | 27 vs 28 of 1071 | -1 (-13 to +11) |
| data/realistic/oft/thr50/seen/merged | 0.025 | gru_robot_ttp | 12 vs 22 of 31 | -10 (-17 to -3) | 24 vs 28 of 1071 | -4 (-16 to +8) |
| data/realistic/oft/thr50/seen/merged | 0.025 | gru_robotcontact_ttp | 11 vs 22 of 31 | -11 (-18 to -3) | 24 vs 28 of 1071 | -4 (-16 to +8) |
