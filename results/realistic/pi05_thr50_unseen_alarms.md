# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/realistic/pi05/thr50/unseen/merged | 0.05 | gru_phys_ttp | 1 vs 6 of 7 | -5 (-7 to -1) | 8 vs 46 of 928 | -38 (-52 to -25) |
| data/realistic/pi05/thr50/unseen/merged | 0.05 | gru_robot_ttp | 1 vs 6 of 7 | -5 (-7 to -1) | 46 vs 46 of 928 | +0 (-19 to +19) |
| data/realistic/pi05/thr50/unseen/merged | 0.05 | gru_robotcontact_ttp | 1 vs 6 of 7 | -5 (-7 to -1) | 50 vs 46 of 928 | +4 (-15 to +23) |
| data/realistic/pi05/thr50/unseen/merged | 0.025 | gru_phys_ttp | 1 vs 6 of 7 | -5 (-7 to -1) | 5 vs 23 of 928 | -18 (-28 to -8) |
| data/realistic/pi05/thr50/unseen/merged | 0.025 | gru_robot_ttp | 1 vs 6 of 7 | -5 (-7 to -1) | 18 vs 23 of 928 | -5 (-18 to +8) |
| data/realistic/pi05/thr50/unseen/merged | 0.025 | gru_robotcontact_ttp | 0 vs 6 of 7 | -6 (-7 to -4) | 41 vs 23 of 928 | +18 (+3 to +34) |
