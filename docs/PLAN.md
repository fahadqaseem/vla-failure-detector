# Plan: Oct 17 to Oct 23, 2026 (in-person meeting with Prof. Zhu on Friday Oct 23)

Goal for Friday: a first predictor of `t_pnr` tested on unseen tasks, with honest numbers.

## Friday deliverable (3 slides)

1. RESCUE overlap and our gap (they measure the horizon; nobody predicts it on unseen, long tasks).
2. How the labels were made (replay, RESCUE-compatible settings), the t_pnr distribution, and the
   intervention window against the automatic onset (no human annotations this week).
3. One results table on held-out tasks (leave-one-task-out), for timer / SAFE-style probe / steps-since-progress /
   our model: timely recall at 5% false alarms on successes (conformal threshold),
   |t_pnr error| in steps, eta = predicted / true t_pnr, per-step AUROC (whole run), late detections.
   Cite RESCUE 2610.13516, PREFAIL 2607.16921, CheckVLA 2607.26789.

## Steps

| day | step | done when |
|---|---|---|
| Sat-Sun | Grid account works; repo cloned; conda env built; `00_check_env.py` passes on a GPU node | log line in results/LOG.md |
| Mon | `02_replay_test.py` passes on Grid (no-noise replay matches) | PASS with drift in mm |
| Mon | `01_collect.py` also saves per-step hidden features (last layer, the same input SAFE uses) | features shape printed |
| Mon-Tue | collect natural runs on all 10 LIBERO-10 tasks, enough to get 30+ natural failures; add induced failures only if needed (labelled) | rollouts.csv |
| Tue | 3 full replay scans (every checkpoint, K 4) to confirm success probability only decreases over time; sensitivity check tau 0.3, 0.7, "fails every replay" | monotonic yes/no, logged |
| Tue-Wed | replay labels as Slurm array jobs: FULL scans (every 8 steps; binary search dropped Oct 18 because t01_e41 rebounds), K 4, Jeffreys lower 0.25 quantile, tau 0.5, on all 28 natural failures + 20 successes (2 per task); then K 16 at the two checkpoints around the boundary only where the estimate is close to tau | pnr_table.csv |
| Wed | automatic `t_onset` from sim states (`07_auto_onset.py`: missed grasp, drop, stuck, wrong object); intervention window `t_onset - t_pnr` per failure; recovered slips in successes | results/auto_onset.csv |
| Wed | evaluation is leave-one-task-out over the 10 tasks (Fahad, Oct 18; replaces a fixed split): train on 9, test on 1, repeat; doomed-from-start episodes (t_pnr 0) stay in training, flagged, and are left out of timing metrics | written in CLAUDE.md |
| Wed-Thu | `06_train_predictor.py`: inputs hidden features + action chunk + eef/proprio (no step index); target risk + 0/1 label; loss BCE + MSE; logistic regression, then small MLP | results table |
| Thu | baselines: timer (step count), SAFE-style probe on success/fail labels, steps-since-progress | same table |
| Thu night | 3 slides | |

## Rules for this week

- Every number from a logged command (results/LOG.md).
- Evaluation is leave-one-task-out; the held-out task is never looked at while tuning (no tuning on test results).
- Report the threshold (tau) and replay settings next to every `t_pnr` number.
- Natural and induced failures are reported separately.
