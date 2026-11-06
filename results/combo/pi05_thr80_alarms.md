# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/combo/pi05/thr80/merged | 0.05 | gru_phys_ttp | 1 vs 7 of 8 | -6 (-8 to -3) | 5 vs 46 of 928 | -41 (-55 to -28) |
| data/combo/pi05/thr80/merged | 0.05 | or_progress_ttp | 7 vs 7 of 8 | +0 (+0 to +0) | 25 vs 46 of 928 | -21 (-31 to -12) |
| data/combo/pi05/thr80/merged | 0.025 | gru_phys_ttp | 1 vs 7 of 8 | -6 (-8 to -3) | 2 vs 23 of 928 | -21 (-31 to -12) |
| data/combo/pi05/thr80/merged | 0.025 | or_progress_ttp | 6 vs 7 of 8 | -1 (-3 to +0) | 13 vs 23 of 928 | -10 (-17 to -4) |
