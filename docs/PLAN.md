# Plan: Oct 17 to Oct 23, 2026 (in-person meeting with Prof. Zhu on Friday Oct 23)

Goal for Friday: a first predictor of `t_pnr` tested on unseen tasks, with honest numbers.

## Friday deliverable (3 slides)

1. RESCUE overlap and our gap (they measure the horizon; nobody predicts it on unseen, long tasks).
2. How the labels were made (replay, RESCUE-compatible settings) and how they compare with
   Fahad's human annotations.
3. One results table: per-step AUROC (whole run), |t_pnr error| in steps, false alarms on successes,
   for timer / SAFE-style probe / our model, on held-out tasks.

## Steps

| day | step | done when |
|---|---|---|
| Sat-Sun | Grid account works; repo cloned; conda env built; `00_check_env.py` passes on a GPU node | log line in results/LOG.md |
| Mon | `02_replay_test.py` passes on Grid (no-noise replay matches) | PASS with drift in mm |
| Mon | `01_collect.py` also saves per-step hidden features (last layer, the same input SAFE uses) | features shape printed |
| Mon-Tue | collect natural runs on all 10 LIBERO-10 tasks, enough to get 30+ natural failures; add induced failures only if needed (labelled) | rollouts.csv |
| Tue-Wed | replay labels: `03_pnr_scan.py` on failures + 20 successes, tau 0.5 (also 0.3/0.7) | pnr_table.csv |
| Wed | load Fahad's own annotations; compare with replay `t_pnr` on shared episodes | small table |
| Wed-Thu | `06_train_predictor.py`: per-step logistic regression, then small MLP; task-held-out split | results table |
| Thu | baselines: timer (step count), SAFE-style probe on success/fail labels | same table |
| Thu night | 3 slides | |

## Rules for this week

- Every number from a logged command (results/LOG.md).
- Held-out tasks are fixed BEFORE training and never looked at while tuning.
- Report the threshold (tau) and replay settings next to every `t_pnr` number.
- Natural and induced failures are reported separately.
