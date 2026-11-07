# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/realistic/pi05/thr50/seen/merged | 0.05 | gru_phys_ttp | 3 vs 6 of 7 | -3 (-6 to +1) | 47 vs 44 of 928 | +3 (-14 to +19) |
| data/realistic/pi05/thr50/seen/merged | 0.05 | gru_robot_ttp | 5 vs 6 of 7 | -1 (-4 to +2) | 38 vs 44 of 928 | -6 (-21 to +8) |
| data/realistic/pi05/thr50/seen/merged | 0.05 | gru_robotcontact_ttp | 5 vs 6 of 7 | -1 (-4 to +2) | 49 vs 44 of 928 | +5 (-10 to +20) |
| data/realistic/pi05/thr50/seen/merged | 0.025 | gru_phys_ttp | 1 vs 6 of 7 | -5 (-7 to -1) | 21 vs 19 of 928 | +2 (-10 to +14) |
| data/realistic/pi05/thr50/seen/merged | 0.025 | gru_robot_ttp | 5 vs 6 of 7 | -1 (-4 to +2) | 23 vs 19 of 928 | +4 (-7 to +15) |
| data/realistic/pi05/thr50/seen/merged | 0.025 | gru_robotcontact_ttp | 1 vs 6 of 7 | -5 (-7 to -1) | 19 vs 19 of 928 | +0 (-11 to +11) |
