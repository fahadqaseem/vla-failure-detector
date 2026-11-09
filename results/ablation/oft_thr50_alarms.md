# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/ablation/oft/thr50/merged | 0.05 | gru_phys_ttp | 2 vs 27 of 31 | -25 (-29 to -20) | 58 vs 51 of 1071 | +7 (-13 to +28) |
| data/ablation/oft/thr50/merged | 0.05 | gru_phys_ttp_no_goal | 0 vs 27 of 31 | -27 (-30 to -23) | 104 vs 51 of 1071 | +53 (+29 to +77) |
| data/ablation/oft/thr50/merged | 0.05 | gru_phys_ttp_no_pose | 1 vs 27 of 31 | -26 (-30 to -22) | 51 vs 51 of 1071 | +0 (-20 to +20) |
| data/ablation/oft/thr50/merged | 0.05 | gru_phys_ttp_no_contact | 3 vs 27 of 31 | -24 (-28 to -19) | 41 vs 51 of 1071 | -10 (-27 to +8) |
| data/ablation/oft/thr50/merged | 0.025 | gru_phys_ttp | 2 vs 22 of 31 | -20 (-26 to -14) | 8 vs 27 of 1071 | -19 (-31 to -8) |
| data/ablation/oft/thr50/merged | 0.025 | gru_phys_ttp_no_goal | 0 vs 22 of 31 | -22 (-27 to -17) | 57 vs 27 of 1071 | +30 (+13 to +48) |
| data/ablation/oft/thr50/merged | 0.025 | gru_phys_ttp_no_pose | 0 vs 22 of 31 | -22 (-27 to -17) | 51 vs 27 of 1071 | +24 (+7 to +41) |
| data/ablation/oft/thr50/merged | 0.025 | gru_phys_ttp_no_contact | 1 vs 22 of 31 | -21 (-26 to -15) | 9 vs 27 of 1071 | -18 (-29 to -7) |
