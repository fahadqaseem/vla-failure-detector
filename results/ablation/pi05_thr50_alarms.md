# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/ablation/pi05/thr50/merged | 0.05 | gru_phys_ttp | 1 vs 6 of 7 | -5 (-7 to -1) | 8 vs 46 of 928 | -38 (-52 to -25) |
| data/ablation/pi05/thr50/merged | 0.05 | gru_phys_ttp_no_goal | 0 vs 6 of 7 | -6 (-7 to -4) | 1 vs 46 of 928 | -45 (-59 to -33) |
| data/ablation/pi05/thr50/merged | 0.05 | gru_phys_ttp_no_pose | 1 vs 6 of 7 | -5 (-7 to -1) | 11 vs 46 of 928 | -35 (-49 to -22) |
| data/ablation/pi05/thr50/merged | 0.05 | gru_phys_ttp_no_contact | 1 vs 6 of 7 | -5 (-7 to -1) | 11 vs 46 of 928 | -35 (-49 to -22) |
| data/ablation/pi05/thr50/merged | 0.025 | gru_phys_ttp | 1 vs 6 of 7 | -5 (-7 to -1) | 5 vs 23 of 928 | -18 (-28 to -8) |
| data/ablation/pi05/thr50/merged | 0.025 | gru_phys_ttp_no_goal | 0 vs 6 of 7 | -6 (-7 to -4) | 1 vs 23 of 928 | -22 (-32 to -13) |
| data/ablation/pi05/thr50/merged | 0.025 | gru_phys_ttp_no_pose | 0 vs 6 of 7 | -6 (-7 to -4) | 6 vs 23 of 928 | -17 (-27 to -8) |
| data/ablation/pi05/thr50/merged | 0.025 | gru_phys_ttp_no_contact | 1 vs 6 of 7 | -5 (-7 to -1) | 10 vs 23 of 928 | -13 (-23 to -3) |
