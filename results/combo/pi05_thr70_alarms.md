# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/combo/pi05/thr70/merged | 0.05 | gru_phys_ttp | 0 vs 6 of 7 | -6 (-7 to -4) | 13 vs 46 of 928 | -33 (-47 to -19) |
| data/combo/pi05/thr70/merged | 0.05 | or_progress_ttp | 6 vs 6 of 7 | +0 (+0 to +0) | 30 vs 46 of 928 | -16 (-27 to -6) |
| data/combo/pi05/thr70/merged | 0.025 | gru_phys_ttp | 0 vs 6 of 7 | -6 (-7 to -4) | 5 vs 23 of 928 | -18 (-28 to -8) |
| data/combo/pi05/thr70/merged | 0.025 | or_progress_ttp | 5 vs 6 of 7 | -1 (-3 to +0) | 16 vs 23 of 928 | -7 (-14 to +0) |
