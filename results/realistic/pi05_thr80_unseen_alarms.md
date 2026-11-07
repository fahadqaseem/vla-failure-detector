# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/realistic/pi05/thr80/unseen/merged | 0.05 | gru_phys_ttp | 1 vs 7 of 8 | -6 (-8 to -3) | 5 vs 46 of 928 | -41 (-55 to -28) |
| data/realistic/pi05/thr80/unseen/merged | 0.05 | gru_robot_ttp | 0 vs 7 of 8 | -7 (-8 to -5) | 63 vs 46 of 928 | +17 (-3 to +36) |
| data/realistic/pi05/thr80/unseen/merged | 0.05 | gru_robotcontact_ttp | 0 vs 7 of 8 | -7 (-8 to -5) | 17 vs 46 of 928 | -29 (-44 to -15) |
| data/realistic/pi05/thr80/unseen/merged | 0.025 | gru_phys_ttp | 1 vs 7 of 8 | -6 (-8 to -3) | 2 vs 23 of 928 | -21 (-31 to -12) |
| data/realistic/pi05/thr80/unseen/merged | 0.025 | gru_robot_ttp | 0 vs 7 of 8 | -7 (-8 to -5) | 46 vs 23 of 928 | +23 (+7 to +39) |
| data/realistic/pi05/thr80/unseen/merged | 0.025 | gru_robotcontact_ttp | 0 vs 7 of 8 | -7 (-8 to -5) | 8 vs 23 of 928 | -15 (-26 to -5) |
