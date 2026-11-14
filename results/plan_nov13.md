# Plan, Nov 13, 2026: pure regression of the point of no return score

New direction from Prof. Zhu (Nov 13): no t_pnr threshold in training. Predict, at every policy query, the replay failure fraction
("point of no return score"). Written before any job. CPU Slurm only. Results in results/regression_v2/, method in docs/method_regression.md.
Code: scripts/60_regression.py (new, standalone; 06_train_predictor.py is not used because its gru_phys_frac balances positive and
negative rows by the t_pnr label, which this plan rules out).

## Data (fixed before any result)

- Episodes: the same pre-registered sets as slurm/n6_train.sbatch.
  OpenVLA-OFT: natural (10 tasks), perturbed tasks 0, 1, 4 to 8, perturbed_v2 folders with GATE_PASS. Refined counts (K 16 at boundary
  checkpoints, data/week2_refine) are used.
  Pi0.5: natural (10 tasks), perturbed seeds 0 and 1 with GATE_PASS. No refined counts exist for Pi0.5 (K 4 everywhere).
  The fresh Pi0.5 seeds 2 to 4 are NOT used here.
- Hidden states: both policies have them (`features_mean` per query: OFT 4096, Pi0.5 1024). If any used episode lacks them the job stops
  and says so.
- Target per query: failure fraction = 1 - successful replays / K at that checkpoint (scans are every 8 steps = every query).
  Failed runs: scanned checkpoints only; queries without a checkpoint are masked (no loss, no metric).
  Successes: target 0 at every query (assumption: a run that succeeded is treated as safe throughout); the OFT successes that were
  scanned use their scan values instead.
- Excluded from training AND evaluation: recoverable failures, i.e. failures recoverable by pre-check (3 of 4) and scanned failures
  whose last checkpoint is recoverable under the 50% rule (Jeffreys tau 0.5, the project default). Unscanned failures that are not
  pre-check recoverable have no target and are also left out. Doomed-from-start failures stay in.
- Every job log prints the counts (episodes, failures kept, excluded, points) so they can be checked.

## Training (all learned models)

- Output = sigmoid of the network; loss = MSE between output and target on known points only.
- Every episode has the same total weight: each known point gets 1 / (known points in its episode). No reweighting by label or class.
- Inputs standardised with the training rows. Adam, lr 1e-3, weight decay 1e-3, 300 full-batch epochs (as 06), seed 0 first.
- Unseen tasks: leave one task out (train on 9 tasks, test on the 10th), 10 folds, both policies. Pi0.5 tasks 2, 3, 8, 9 have no
  kept failures; their successes still count in the success and all-point metrics.

## Models

(a) gru_phys_frac: GRU 64 over the last 8 queries of the 33 physical signals (data/physical, 20_physical_signals.py) -> linear.
(b) SAFE-regression, on features_mean (the SAFE-style hidden-state input already used by our `safe` baseline), same target and MSE:
    safe_lin (linear probe, as our `safe`), safe_mlp (linear 256, ReLU, linear), safe_lstm (LSTM 128 over the run so far on the
    PCA 128 of features_mean; PCA fitted on training rows, needed so the LSTM fits CPU time). These follow the SAFE design (probe,
    MLP and LSTM on last-layer features); they are our implementation, not the authors' code.
(c) gru_physvla_frac: GRU 64 over the last 8 queries of [physical signals, PCA 128 of features_mean].
(d) Baselines: const = training mean of the target (episode-weighted as above); progress_iso = steps-since-progress (RESCUE, 0.01 m)
    mapped to a failure fraction by increasing isotonic regression fit on the training tasks (same weights).
    Extra (CLAUDE.md timeout rule, not a candidate): timer_iso = policy step mapped the same way. It shows how much of the target the
    clock alone explains; no model gets the step as input.

## Metrics (held-out tasks, pooled over the 10 folds; also per task)

1. MSE and MAE on (i) scanned checkpoints of failed runs, (ii) successes, (iii) all known points.
2. Spearman correlation between prediction and target on failed runs: pooled over all their points, and the median per episode
   (episodes whose target is not constant).
3. Noise floor from the binomial noise of the retries: for a point with K retries and observed failure fraction f,
   expected squared error of the observed fraction around the true one = f(1 - f) / (K - 1) (unbiased); K = 4, or 16 where refined.
   MAE floor: E|f_hat - f| under Binomial(K, f) with f = observed (plug-in, approximate). Points with an assumed 0 (unscanned
   successes) have floor 0.
4. Seeds: seed 0 for every model first. Best two LEARNED models (a, b variants, c) = lowest mean over both policies of
   (MSE (i) + MSE (ii)) / 2, so a model cannot win by predicting high everywhere or low everywhere. Those two get seeds 0 to 4;
   report mean and standard deviation over seeds. Chosen automatically by the report job from seed 0 only.

## Backup only (not the headline)

From each model's score (baselines included): alarm = first query whose score is above a threshold set for 2.5% false alarms on
successes (conformal quantile of the per-run maximum, from cross-fitted scores of the training-task successes: for each training task a
model trained on the other 8 scores it). Report % of timed failures (t_pnr > 0) caught at or before t_pnr under the 50% rule and the
70% rule (raw failure fraction >= 0.7 = not recoverable, as 32_relabel.py), and the actual false-alarm rate on held-out successes.
Under the 70% rule some kept failures have no t_pnr; they are not timed.

## Jobs

- slurm/n13_reg.sbatch: one array task per (model, held-out task), CPU (8 cores, 48 GB), reqp. Seed 0: 2 policies x 6 jobs
  (gru_phys_frac, safe_lin, safe_mlp, safe_lstm, gru_physvla_frac, baselines) x 10 folds.
- slurm/n13_pick.sbatch (after seed 0): writes the seed-0 report, picks the best two, submits seeds 1 to 4 for them and the final report.
- slurm/n13_report.sbatch: results/regression_v2/ (report.md, per_task.md, seeds.md, backup_alarms.md), logs to results/LOG.md, pushes.

## Amendment (Fahad, Nov 13, 2026, before any result was read)

- Seeds: all 5 seeds (0 to 4) for EVERY learned model (gru_phys_frac, safe_lin, safe_mlp, safe_lstm, gru_physvla_frac), both policies.
  Nothing is picked on test results; the "best two" rule above and n13_pick.sbatch are dropped. seeds.md reports mean and range (min to max).
- Plots: for 4 held-out failed runs and 1 success per policy, the true score and every model's predicted score over time on one chart
  each (PNG), results/regression_v2/plots/ (62_regression_plots.py, seed 0).
- Output layout: results/regression_v2/main.md (main table), seeds.md, backup.md (alarm % at 2.5% false alarms), plots/; per_task.md stays
  as a secondary file.
