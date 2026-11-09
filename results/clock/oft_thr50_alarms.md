# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/clock/oft_thr50 | 0.05 | gru_phys_ttp_s0 | 2 vs 16 of 17 | -14 (-17 to -11) | 58 vs 51 of 1071 | +7 (-13 to +28) |
| data/clock/oft_thr50 | 0.05 | gru_phys_ttp_s1 | 5 vs 16 of 17 | -11 (-15 to -7) | 32 vs 51 of 1071 | -19 (-35 to -3) |
| data/clock/oft_thr50 | 0.05 | gru_phys_ttp_s2 | 4 vs 16 of 17 | -12 (-15 to -8) | 85 vs 51 of 1071 | +34 (+13 to +55) |
| data/clock/oft_thr50 | 0.05 | gru_phys_ttp_s3 | 4 vs 16 of 17 | -12 (-15 to -8) | 74 vs 51 of 1071 | +23 (+2 to +44) |
| data/clock/oft_thr50 | 0.05 | gru_phys_ttp_s4 | 2 vs 16 of 17 | -14 (-17 to -11) | 58 vs 51 of 1071 | +7 (-13 to +27) |
| data/clock/oft_thr50 | 0.05 | gru_phys_ttp_ens | 3 vs 16 of 17 | -13 (-16 to -9) | 59 vs 51 of 1071 | +8 (-11 to +27) |
| data/clock/oft_thr50 | 0.05 | or_progress_ttp_s0 | 14 vs 16 of 17 | -2 (-5 to +0) | 45 vs 51 of 1071 | -6 (-18 to +6) |
| data/clock/oft_thr50 | 0.05 | or_progress_ttp_s1 | 15 vs 16 of 17 | -1 (-3 to +0) | 45 vs 51 of 1071 | -6 (-18 to +6) |
| data/clock/oft_thr50 | 0.05 | or_progress_ttp_s2 | 15 vs 16 of 17 | -1 (-3 to +0) | 55 vs 51 of 1071 | +4 (-9 to +17) |
| data/clock/oft_thr50 | 0.05 | or_progress_ttp_s3 | 16 vs 16 of 17 | +0 (+0 to +0) | 94 vs 51 of 1071 | +43 (+25 to +61) |
| data/clock/oft_thr50 | 0.05 | or_progress_ttp_s4 | 15 vs 16 of 17 | -1 (-3 to +0) | 77 vs 51 of 1071 | +26 (+10 to +43) |
| data/clock/oft_thr50 | 0.05 | or_progress_ens | 15 vs 16 of 17 | -1 (-3 to +0) | 47 vs 51 of 1071 | -4 (-16 to +8) |
| data/clock/oft_thr50 | 0.025 | gru_phys_ttp_s0 | 2 vs 13 of 17 | -11 (-15 to -6) | 8 vs 27 of 1071 | -19 (-31 to -8) |
| data/clock/oft_thr50 | 0.025 | gru_phys_ttp_s1 | 2 vs 13 of 17 | -11 (-15 to -6) | 12 vs 27 of 1071 | -15 (-27 to -4) |
| data/clock/oft_thr50 | 0.025 | gru_phys_ttp_s2 | 2 vs 13 of 17 | -11 (-15 to -6) | 21 vs 27 of 1071 | -6 (-19 to +7) |
| data/clock/oft_thr50 | 0.025 | gru_phys_ttp_s3 | 2 vs 13 of 17 | -11 (-15 to -6) | 49 vs 27 of 1071 | +22 (+5 to +39) |
| data/clock/oft_thr50 | 0.025 | gru_phys_ttp_s4 | 1 vs 13 of 17 | -12 (-16 to -7) | 46 vs 27 of 1071 | +19 (+3 to +36) |
| data/clock/oft_thr50 | 0.025 | gru_phys_ttp_ens | 3 vs 13 of 17 | -10 (-14 to -5) | 17 vs 27 of 1071 | -10 (-23 to +3) |
| data/clock/oft_thr50 | 0.025 | or_progress_ttp_s0 | 13 vs 13 of 17 | +0 (-3 to +3) | 19 vs 27 of 1071 | -8 (-16 to +0) |
| data/clock/oft_thr50 | 0.025 | or_progress_ttp_s1 | 13 vs 13 of 17 | +0 (-3 to +3) | 23 vs 27 of 1071 | -4 (-13 to +5) |
| data/clock/oft_thr50 | 0.025 | or_progress_ttp_s2 | 13 vs 13 of 17 | +0 (-3 to +3) | 20 vs 27 of 1071 | -7 (-15 to +1) |
| data/clock/oft_thr50 | 0.025 | or_progress_ttp_s3 | 13 vs 13 of 17 | +0 (-3 to +3) | 36 vs 27 of 1071 | +9 (-2 to +21) |
| data/clock/oft_thr50 | 0.025 | or_progress_ttp_s4 | 13 vs 13 of 17 | +0 (-3 to +3) | 25 vs 27 of 1071 | -2 (-11 to +8) |
| data/clock/oft_thr50 | 0.025 | or_progress_ens | 13 vs 13 of 17 | +0 (-3 to +3) | 19 vs 27 of 1071 | -8 (-16 to +0) |
