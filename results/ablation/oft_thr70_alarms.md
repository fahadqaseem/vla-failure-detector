# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/ablation/oft/thr70/merged | 0.05 | gru_phys_ttp | 7 vs 31 of 35 | -24 (-29 to -18) | 19 vs 51 of 1071 | -32 (-46 to -18) |
| data/ablation/oft/thr70/merged | 0.05 | gru_phys_ttp_no_goal | 0 vs 31 of 35 | -31 (-34 to -27) | 170 vs 51 of 1071 | +119 (+91 to +146) |
| data/ablation/oft/thr70/merged | 0.05 | gru_phys_ttp_no_pose | 4 vs 31 of 35 | -27 (-32 to -22) | 33 vs 51 of 1071 | -18 (-35 to -1) |
| data/ablation/oft/thr70/merged | 0.05 | gru_phys_ttp_no_contact | 5 vs 31 of 35 | -26 (-31 to -21) | 14 vs 51 of 1071 | -37 (-51 to -23) |
| data/ablation/oft/thr70/merged | 0.025 | gru_phys_ttp | 4 vs 25 of 35 | -21 (-28 to -14) | 8 vs 27 of 1071 | -19 (-30 to -8) |
| data/ablation/oft/thr70/merged | 0.025 | gru_phys_ttp_no_goal | 0 vs 25 of 35 | -25 (-30 to -20) | 167 vs 27 of 1071 | +140 (+115 to +166) |
| data/ablation/oft/thr70/merged | 0.025 | gru_phys_ttp_no_pose | 4 vs 25 of 35 | -21 (-27 to -14) | 10 vs 27 of 1071 | -17 (-29 to -6) |
| data/ablation/oft/thr70/merged | 0.025 | gru_phys_ttp_no_contact | 5 vs 25 of 35 | -20 (-27 to -13) | 8 vs 27 of 1071 | -19 (-30 to -8) |
