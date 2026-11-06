# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/combo/oft/thr80/merged | 0.05 | gru_phys_ttp | 8 vs 35 of 39 | -27 (-32 to -21) | 27 vs 51 of 1071 | -24 (-40 to -8) |
| data/combo/oft/thr80/merged | 0.05 | or_progress_ttp | 33 vs 35 of 39 | -2 (-5 to +0) | 41 vs 51 of 1071 | -10 (-22 to +1) |
| data/combo/oft/thr80/merged | 0.025 | gru_phys_ttp | 7 vs 28 of 39 | -21 (-28 to -13) | 13 vs 27 of 1071 | -14 (-25 to -3) |
| data/combo/oft/thr80/merged | 0.025 | or_progress_ttp | 28 vs 28 of 39 | +0 (-4 to +4) | 20 vs 27 of 1071 | -7 (-15 to +0) |
