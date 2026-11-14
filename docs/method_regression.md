# Method: pure regression of the point of no return score (Nov 13, 2026)

Plan: results/plan_nov13.md. Code: scripts/60_regression.py (one run = policy, model, held-out task, seed), scripts/61_regression_report.py
(metrics), scripts/62_regression_plots.py (plots), slurm/n13_submit.sh, n13_reg.sbatch, n13_report.sbatch. Results: results/regression_v2/. CPU only.

## Episodes and exclusions

- Episode sets per policy: `scripts/60_regression.py:53-63` (`data_sets`), the same pre-registered globs as slurm/n6_train.sbatch.
  OFT: data/natural, data/perturbed tasks 0, 1, 4 to 8, data/perturbed_v2 folders with GATE_PASS; scans data/full_scans,
  data/perturbed_scans, data/perturbed_v2_scans; refined K 12 counts from data/week2_refine added at `60_regression.py:102-108`.
  Pi0.5: data/pi05/natural, data/pi05/perturbed seeds 0 and 1 with GATE_PASS; scans data/pi05/full_scans, data/pi05/perturbed_scans;
  no refined counts (K 4 everywhere).
- Excluded (`60_regression.py:118-130`): induced episodes; failures recoverable by pre-check (verdict in 09_precheck.py files,
  `:109-113`); unscanned failures (no target); scanned failures whose last checkpoint is recoverable under the 50% rule
  (`recoverable_50`, `:66-68`: Jeffreys lower 0.25 quantile of the success rate >= 0.5; `t_pnr` returns None, `:76-84`).
  Doomed-from-start failures (t_pnr = 0) stay in.
- Hidden states must be present in every kept episode (`:131`, assertion), physical signals too (`:142-143`).

## Target

- Per query k (policy step `query_steps[k]`, every 8 steps): failure fraction = 1 - successful replays / K at the scan checkpoint with that
  step (`60_regression.py:134-139`); K = number of replays there (4, or 16 where refined). Queries without a checkpoint: NaN (masked).
- Successes without a scan: 0 at every query, K = 0 (`:140-141`). This is an assumption (a run that succeeded is treated as safe
  throughout); the noise floor there is 0. Scanned successes (OFT, 20) use their scan values.
- The 50% and 70% t_pnr values are stored per episode for the backup alarms only (`:146`, `recoverable_70` at `:71-73`: raw failure
  fraction >= 0.7 is not recoverable, as 32_relabel.py); they are never used in training.

## Inputs (never the step index)

- Physical signals, 33 columns per query from scripts/20_physical_signals.py (`NAMES`, `20_physical_signals.py:33-35`; computed
  `:90-104`), loaded at `60_regression.py:142`. Per placement slot (obj1, obj2): dist (gripper to object, m), ddist (change since the
  previous query), pos_x, pos_y, pos_z (object position), dz (height above its first-query position), lifted (dz > 0.02 m), tilt (rad,
  up axis now vs first query), contact (robosuite check_contact), goal_dist (object to goal region or target), in_goal (goal predicate
  true), used (slot used by this task). Articulation slot: art_dist, art_ddist, art_contact, art_true, art_used. Gripper: grip_open
  (finger distance), eef_x, eef_y, eef_z.
- Hidden states: `features_mean` of the episode file (`60_regression.py:148`): last-layer hidden states at the action tokens, mean over
  the tokens; OFT 4096, Pi0.5 1024.
- PCA 128 of features_mean, fitted on the training rows of the fold only (`:204-206`), for safe_lstm and gru_physvla_frac.
- Standardisation with the mean and std of the training rows (`:207-210`).
- Baseline inputs: steps-since-progress (`steps_since_progress`, `:87-93`: queries since the eef last moved more than 0.01 m between
  successive queries, RESCUE) and the policy step (timer_iso only, a check).

## Models (`per_query_input` `60_regression.py:191-198`, `train` `:201-247`)

| model | input per query | window | architecture |
|---|---|---|---|
| gru_phys_frac | physical (33) | last 8 queries (`windows`, `:156-159`; earlier queries repeat the first) | GRU 64, last state -> linear 1 (`GRUNet`, `:173-179`) |
| safe_lin | features_mean | 1 | linear 1 (`:225`) |
| safe_mlp | features_mean | 1 | linear 256 -> ReLU -> linear 1 (`:225-226`) |
| safe_lstm | PCA 128 of features_mean | the whole run so far | LSTM 128 -> linear 1 (`LSTMNet`, `:182-188`; padded batch `:216-219`) |
| gru_physvla_frac | physical (33) + PCA 128 | last 8 queries | GRU 64 -> linear 1 |
| const | none | | training mean of the target, episode-weighted (`train_baseline`, `:249-253`) |
| progress_iso | steps-since-progress | 1 | increasing isotonic regression onto the target, fit on the training tasks with the same weights (`:254-257`) |
| timer_iso | policy step | 1 | same isotonic fit (check for the timeout trap, not a candidate) |

The safe_* models follow the SAFE design (probe, MLP, LSTM on last-layer features) with our target; they are our implementation.
Output of every learned model = sigmoid of the network (`:232`, `:239-245`).

## Loss and training

- MSE between sigmoid output and target on known points only (`60_regression.py:232`).
- Weights (`weights_and_targets`, `:162-170`): each known point gets 1 / (known points in its episode), then normalised to sum 1,
  so every episode has the same total weight. No reweighting by label, class or outcome.
- Adam, lr 1e-3, weight decay 1e-3, 300 full-batch epochs (`:230-235`; defaults `:39-41`), torch seed = `--seed` (`:203`), PCA
  seeded the same.
- Leave one task out: train on the 9 other tasks, predict the held-out task (`:265-268`); 10 folds per policy.

## Metrics (`scripts/61_regression_report.py`)

- Known points of the held-out tasks pooled over the 10 folds (`points`, `61_regression_report.py:45-52`). MSE and MAE on (i) failed runs
  (all their points are scanned checkpoints), (ii) successes, (iii) all (`metrics`, `:65-70`).
- Spearman on failed runs: pooled over points (`:72`), and the median over episodes with a non-constant target and prediction
  (`:73-78`).
- Noise floor (`floors`, `:55-62`): per point with K > 1 retries and observed fraction f, MSE f(1 - f) / (K - 1) (unbiased estimate of
  the variance of the observed fraction), MAE = E|X/K - f| with X ~ Binomial(K, f) (plug-in); K 0 points (assumed 0) have floor 0;
  averaged over the same points as the model errors.
- Seeds (amendment, Nov 13): seeds 0 to 4 for every learned model (torch initialisation and PCA change; data, folds and thresholds do
  not); seeds.md reports mean and range (min to max) (`:178-187`). Nothing is picked on test results.
- Files: main.md (seed 0 table), seeds.md, backup.md, per_task.md (secondary), plots/ (62_regression_plots.py: 4 held-out failed runs
  and 1 success per policy, chosen by the fixed rule in its docstring, true and predicted scores over policy steps).

## Backup alarms (`61_regression_report.py:89-107`)

- Threshold per fold: for each training task u, a model trained on the other 8 tasks scores u's successes (`60_regression.py:272-276`);
  the per-run maximum scores of these cross-fitted successes are the calibration set. Threshold = conformal quantile at alpha 0.025
  (`conformal_threshold`, `61_regression_report.py:89-92`: the ceil((n + 1)(1 - alpha))-th smallest per-run max). Alarm = first query
  whose score is above it (`:97-100`).
- Reported: timely = alarm at or before t_pnr for kept failures with t_pnr > 0, under the 50% rule and the 70% rule (`:102-105`), and the
  false-alarm rate on held-out successes (`:101`). Baselines included. This is a backup, not the headline.
