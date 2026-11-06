# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/combo/oft/thr50/merged | 0.05 | gru_phys_ttp | 2 vs 27 of 31 | -25 (-29 to -20) | 58 vs 51 of 1071 | +7 (-13 to +28) |
| data/combo/oft/thr50/merged | 0.05 | or_progress_ttp | 23 vs 27 of 31 | -4 (-8 to -1) | 45 vs 51 of 1071 | -6 (-18 to +6) |
| data/combo/oft/thr50/merged | 0.025 | gru_phys_ttp | 2 vs 22 of 31 | -20 (-26 to -14) | 8 vs 27 of 1071 | -19 (-31 to -8) |
| data/combo/oft/thr50/merged | 0.025 | or_progress_ttp | 21 vs 22 of 31 | -1 (-4 to +2) | 19 vs 27 of 1071 | -8 (-16 to +0) |
