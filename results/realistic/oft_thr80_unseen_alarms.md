# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/realistic/oft/thr80/unseen/merged | 0.05 | gru_phys_ttp | 8 vs 35 of 39 | -27 (-32 to -21) | 27 vs 51 of 1071 | -24 (-40 to -8) |
| data/realistic/oft/thr80/unseen/merged | 0.05 | gru_robot_ttp | 4 vs 35 of 39 | -31 (-36 to -26) | 4 vs 51 of 1071 | -47 (-61 to -34) |
| data/realistic/oft/thr80/unseen/merged | 0.05 | gru_robotcontact_ttp | 9 vs 35 of 39 | -26 (-31 to -20) | 11 vs 51 of 1071 | -40 (-54 to -27) |
| data/realistic/oft/thr80/unseen/merged | 0.025 | gru_phys_ttp | 7 vs 28 of 39 | -21 (-28 to -13) | 13 vs 27 of 1071 | -14 (-25 to -3) |
| data/realistic/oft/thr80/unseen/merged | 0.025 | gru_robot_ttp | 3 vs 28 of 39 | -25 (-31 to -18) | 3 vs 27 of 1071 | -24 (-35 to -14) |
| data/realistic/oft/thr80/unseen/merged | 0.025 | gru_robotcontact_ttp | 9 vs 28 of 39 | -19 (-27 to -10) | 6 vs 27 of 1071 | -21 (-32 to -10) |
