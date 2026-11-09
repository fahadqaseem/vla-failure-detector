# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/clock/oft_thr70 | 0.05 | gru_phys_ttp_s0 | 4 vs 18 of 19 | -14 (-17 to -10) | 19 vs 51 of 1071 | -32 (-46 to -18) |
| data/clock/oft_thr70 | 0.05 | gru_phys_ttp_s1 | 4 vs 18 of 19 | -14 (-17 to -10) | 31 vs 51 of 1071 | -20 (-35 to -5) |
| data/clock/oft_thr70 | 0.05 | gru_phys_ttp_s2 | 3 vs 18 of 19 | -15 (-18 to -11) | 26 vs 51 of 1071 | -25 (-40 to -10) |
| data/clock/oft_thr70 | 0.05 | gru_phys_ttp_s3 | 5 vs 18 of 19 | -13 (-17 to -9) | 58 vs 51 of 1071 | +7 (-12 to +27) |
| data/clock/oft_thr70 | 0.05 | gru_phys_ttp_s4 | 4 vs 18 of 19 | -14 (-17 to -10) | 26 vs 51 of 1071 | -25 (-40 to -10) |
| data/clock/oft_thr70 | 0.05 | gru_phys_ttp_ens | 4 vs 18 of 19 | -14 (-17 to -10) | 26 vs 51 of 1071 | -25 (-40 to -11) |
| data/clock/oft_thr70 | 0.05 | or_progress_ttp_s0 | 17 vs 18 of 19 | -1 (-3 to +0) | 36 vs 51 of 1071 | -15 (-25 to -5) |
| data/clock/oft_thr70 | 0.05 | or_progress_ttp_s1 | 18 vs 18 of 19 | +0 (+0 to +0) | 45 vs 51 of 1071 | -6 (-17 to +4) |
| data/clock/oft_thr70 | 0.05 | or_progress_ttp_s2 | 17 vs 18 of 19 | -1 (-3 to +0) | 43 vs 51 of 1071 | -8 (-18 to +2) |
| data/clock/oft_thr70 | 0.05 | or_progress_ttp_s3 | 18 vs 18 of 19 | +0 (+0 to +0) | 67 vs 51 of 1071 | +16 (+1 to +31) |
| data/clock/oft_thr70 | 0.05 | or_progress_ttp_s4 | 17 vs 18 of 19 | -1 (-3 to +0) | 43 vs 51 of 1071 | -8 (-19 to +3) |
| data/clock/oft_thr70 | 0.05 | or_progress_ens | 17 vs 18 of 19 | -1 (-3 to +0) | 41 vs 51 of 1071 | -10 (-21 to +1) |
| data/clock/oft_thr70 | 0.025 | gru_phys_ttp_s0 | 1 vs 15 of 19 | -14 (-18 to -9) | 8 vs 27 of 1071 | -19 (-30 to -8) |
| data/clock/oft_thr70 | 0.025 | gru_phys_ttp_s1 | 2 vs 15 of 19 | -13 (-17 to -8) | 15 vs 27 of 1071 | -12 (-23 to -1) |
| data/clock/oft_thr70 | 0.025 | gru_phys_ttp_s2 | 2 vs 15 of 19 | -13 (-17 to -8) | 16 vs 27 of 1071 | -11 (-22 to +0) |
| data/clock/oft_thr70 | 0.025 | gru_phys_ttp_s3 | 5 vs 15 of 19 | -10 (-15 to -4) | 30 vs 27 of 1071 | +3 (-11 to +17) |
| data/clock/oft_thr70 | 0.025 | gru_phys_ttp_s4 | 1 vs 15 of 19 | -14 (-18 to -9) | 16 vs 27 of 1071 | -11 (-22 to +0) |
| data/clock/oft_thr70 | 0.025 | gru_phys_ttp_ens | 2 vs 15 of 19 | -13 (-17 to -8) | 15 vs 27 of 1071 | -12 (-23 to -1) |
| data/clock/oft_thr70 | 0.025 | or_progress_ttp_s0 | 15 vs 15 of 19 | +0 (-3 to +3) | 20 vs 27 of 1071 | -7 (-14 to +0) |
| data/clock/oft_thr70 | 0.025 | or_progress_ttp_s1 | 15 vs 15 of 19 | +0 (-3 to +3) | 27 vs 27 of 1071 | +0 (-8 to +9) |
| data/clock/oft_thr70 | 0.025 | or_progress_ttp_s2 | 15 vs 15 of 19 | +0 (-3 to +3) | 27 vs 27 of 1071 | +0 (-8 to +8) |
| data/clock/oft_thr70 | 0.025 | or_progress_ttp_s3 | 15 vs 15 of 19 | +0 (-3 to +3) | 35 vs 27 of 1071 | +8 (-3 to +19) |
| data/clock/oft_thr70 | 0.025 | or_progress_ttp_s4 | 15 vs 15 of 19 | +0 (-3 to +3) | 23 vs 27 of 1071 | -4 (-12 to +4) |
| data/clock/oft_thr70 | 0.025 | or_progress_ens | 15 vs 15 of 19 | +0 (-3 to +3) | 25 vs 27 of 1071 | -2 (-10 to +6) |
