# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/combo/oft/thr70/merged | 0.05 | gru_phys_ttp | 6 vs 31 of 35 | -25 (-30 to -20) | 18 vs 51 of 1071 | -33 (-47 to -19) |
| data/combo/oft/thr70/merged | 0.05 | or_progress_ttp | 28 vs 31 of 35 | -3 (-7 to +0) | 36 vs 51 of 1071 | -15 (-25 to -5) |
| data/combo/oft/thr70/merged | 0.025 | gru_phys_ttp | 4 vs 25 of 35 | -21 (-28 to -14) | 7 vs 27 of 1071 | -20 (-31 to -10) |
| data/combo/oft/thr70/merged | 0.025 | or_progress_ttp | 24 vs 25 of 35 | -1 (-4 to +2) | 20 vs 27 of 1071 | -7 (-14 to +0) |
