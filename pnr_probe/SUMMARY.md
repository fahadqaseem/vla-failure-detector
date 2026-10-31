# pnr_probe summary (branch pnr-probe, Oct 27 to 31, 2026)
Question: can physical precursor signals alarm before `t_pnr` on unseen tasks, better than progress?
All data, 81 timed failures, 1071 successes, 31 recoverable failures, leave-one-task-out. Per-chunk runs keep 78 and 912.

## Primary results (unseen, 2.5% budget; best model within budget; progress: 11 of 81, FPR 0.025, +200)

| tested | timely | FPR | median window | source |
|---|---|---|---|---|
| surprise | 2 of 81 | 0.017 | +112 | `summary.md` |
| critical slowing down | 8 of 81 | 0.016 | +128 | `summary.md` |
| time-to-contact | 2 of 81 | 0.023 | +104 | `summary.md` |
| micro-events alone | 13 of 81 | 0.024 | +164 | `summary.md` |
| Track 1 reference | 10 of 81 | 0.013 | +136 | `summary.md` |
| Track 1 + micro-events | 8 of 81 | 0.011 | +112 | `micro_phys/` |
| dense forces and torques, per-chunk replay | 8 of 78 | 0.015 | +136 | `dense_chunk/summary.md` |

No model beat progress on timely alarms: micro-events alone +2 (-6 to +10); Track 1 + micro-events -3 (-10 to +4), and at 5% -4 (-13 to +5).
Replay from step 0 was dropped as biased (timed failures passed 66.7%, successes 95.4%); per-chunk replay passed 96.3% and 85.2%.
Dense vs progress on per-chunk replay: -6 (-13 to +1); progress here was at 0.034, over budget.

## What worked

- Quieter, not earlier. Unnecessary alarms at 2.5%: progress 22 of 31, micro-events alone 12, Track 1 2, Track 1 + micro-events 1. Most of the quiet comes from Track 1.
- Fumbling rises around `t_pnr`: `grip_reopen8` AUROC is 0.53 early, 0.59 before, 0.71 after. It is weak before `t_pnr`, so this is a reaction more than a warning.

## What did not work

- Surprise and time-to-contact: 2 of 81, both at low AUROC (time-matched 0.600 and 0.511).
- Contact flicker (0.47, 0.40, 0.42) and jerk spikes (0.52, 0.53, 0.53) gave no useful warning.
- Dense features added little: (a) 7 of 78, (b) 8 of 78, and at 5% (b) went over budget (FPR 0.101; 11 of 78 vs 19 of 78).
- CUSUM on unseen tasks broke calibration: 0.126 at 2.5% and 0.149 at 5%, 4 of 81. It stayed within budget on seen tasks.
- Unseen tasks remain the limit: Track 1 + micro-events gets 14 of 81 seen vs 8 of 81 unseen at 2.5%, 21 vs 13 at 5%.

## Worth reusing on main

- `micro_phys/train_fold.py`: one Slurm array task per held-out group, then merge.
- `grip_reopen8` from `precursor_features.py`, as a post-`t_pnr` confirmation signal. Drop the other two counts.
- `dense/dense_chunk_replay.py`, only if per-step contacts or torques are needed. Successes pass 85.2%, so report who was left out.
- `summary.py` (rank within budget) and `micro_phys/plot_micro.py` (signals aligned to `t_pnr`).
