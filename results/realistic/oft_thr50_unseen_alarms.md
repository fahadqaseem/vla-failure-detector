# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/realistic/oft/thr50/unseen/merged | 0.05 | gru_phys_ttp | 2 vs 27 of 31 | -25 (-29 to -20) | 58 vs 51 of 1071 | +7 (-13 to +28) |
| data/realistic/oft/thr50/unseen/merged | 0.05 | gru_robot_ttp | 2 vs 27 of 31 | -25 (-29 to -20) | 18 vs 51 of 1071 | -33 (-48 to -18) |
| data/realistic/oft/thr50/unseen/merged | 0.05 | gru_robotcontact_ttp | 5 vs 27 of 31 | -22 (-27 to -17) | 12 vs 51 of 1071 | -39 (-53 to -26) |
| data/realistic/oft/thr50/unseen/merged | 0.025 | gru_phys_ttp | 2 vs 22 of 31 | -20 (-26 to -14) | 8 vs 27 of 1071 | -19 (-31 to -8) |
| data/realistic/oft/thr50/unseen/merged | 0.025 | gru_robot_ttp | 1 vs 22 of 31 | -21 (-26 to -16) | 3 vs 27 of 1071 | -24 (-35 to -14) |
| data/realistic/oft/thr50/unseen/merged | 0.025 | gru_robotcontact_ttp | 2 vs 22 of 31 | -20 (-26 to -13) | 8 vs 27 of 1071 | -19 (-30 to -8) |
