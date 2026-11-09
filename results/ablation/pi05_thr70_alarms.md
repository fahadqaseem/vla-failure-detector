# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/ablation/pi05/thr70/merged | 0.05 | gru_phys_ttp | 0 vs 6 of 7 | -6 (-7 to -4) | 13 vs 46 of 928 | -33 (-47 to -19) |
| data/ablation/pi05/thr70/merged | 0.05 | gru_phys_ttp_no_goal | 0 vs 6 of 7 | -6 (-7 to -4) | 8 vs 46 of 928 | -38 (-52 to -25) |
| data/ablation/pi05/thr70/merged | 0.05 | gru_phys_ttp_no_pose | 0 vs 6 of 7 | -6 (-7 to -4) | 5 vs 46 of 928 | -41 (-55 to -28) |
| data/ablation/pi05/thr70/merged | 0.05 | gru_phys_ttp_no_contact | 0 vs 6 of 7 | -6 (-7 to -4) | 12 vs 46 of 928 | -34 (-48 to -21) |
| data/ablation/pi05/thr70/merged | 0.025 | gru_phys_ttp | 0 vs 6 of 7 | -6 (-7 to -4) | 7 vs 23 of 928 | -16 (-26 to -6) |
| data/ablation/pi05/thr70/merged | 0.025 | gru_phys_ttp_no_goal | 0 vs 6 of 7 | -6 (-7 to -4) | 1 vs 23 of 928 | -22 (-32 to -13) |
| data/ablation/pi05/thr70/merged | 0.025 | gru_phys_ttp_no_pose | 0 vs 6 of 7 | -6 (-7 to -4) | 3 vs 23 of 928 | -20 (-30 to -11) |
| data/ablation/pi05/thr70/merged | 0.025 | gru_phys_ttp_no_contact | 0 vs 6 of 7 | -6 (-7 to -4) | 8 vs 23 of 928 | -15 (-25 to -5) |
