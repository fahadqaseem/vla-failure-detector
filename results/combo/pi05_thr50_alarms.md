# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/combo/pi05/thr50/merged | 0.05 | gru_phys_ttp | 1 vs 6 of 7 | -5 (-7 to -1) | 8 vs 46 of 928 | -38 (-52 to -25) |
| data/combo/pi05/thr50/merged | 0.05 | or_progress_ttp | 7 vs 6 of 7 | +1 (+0 to +3) | 27 vs 46 of 928 | -19 (-29 to -9) |
| data/combo/pi05/thr50/merged | 0.025 | gru_phys_ttp | 1 vs 6 of 7 | -5 (-7 to -1) | 5 vs 23 of 928 | -18 (-28 to -8) |
| data/combo/pi05/thr50/merged | 0.025 | or_progress_ttp | 6 vs 6 of 7 | +0 (-3 to +3) | 16 vs 23 of 928 | -7 (-14 to +0) |
