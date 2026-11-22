# Plan, Nov 22, 2026: 20-replay ground truth (pilot + cost plan)

Prof. Zhu (Nov 20): the ground truth score (replay failure fraction) is too noisy with K = 4 replays per checkpoint; use at least 20 so
the truth curve is smooth, then rerun all experiments. A full rerun is likely too expensive, so this week is a pilot plus a cost plan.
Written and committed before any job. Replays on GPU (galhp L40S, at most 5 GPU jobs at once across everything), regression on CPU (reqp).
No existing data is overwritten: new folders data/gt20_pilot, data/gt20/pooled, results/gt20/.

## Step 1. Pilot (OpenVLA-OFT, 3 failed runs)

- Runs (fixed rule, not by results): the first three OFT failed runs of the Nov 13 plot rule (`62_regression_plots.py` docstring): kept
  failures with t_pnr (50% rule) > 0, the 4 tasks with the most such failures (tasks 0, 1, 4, 6), lowest episode id per task, tasks in
  order. That gives t00_e06_p0_s1 (the run on the Nov 20 slide), t01_e07_p0_s1 and t04_e00_p0_s2. All three are perturbed_v2 episodes,
  scanned with every 8, K 4, seed 0, noise 0.05, extra_steps 200, restore_query, deterministic kernels.
- Checkpoints: every 16 policy steps over the whole run (0, 16, ..., 512; 33 per run, all are chunk boundaries).
- K 20 per checkpoint. Reuse the existing replays where checkpoint and settings match (noise 0.05, extra_steps 200, restore_query,
  deterministic): the 4 seed-0 replays of the scan, plus the 12 seed-1 replays of data/week2_refine where that checkpoint was refined.
  New replays use seed 20 (the replay rng is `default_rng([seed, task, episode_idx, checkpoint, k])`, as 03_pnr_scan.py); seeds already in
  use: 0 (scans and pre-checks), 1 (refinement), 100 (look-ahead). The script checks that the new (seed, k) pairs are disjoint from the
  reused ones and that the first noise draw of every new replay differs from every reused one at that checkpoint.
- Code: scripts/63_gt20_scan.py (same rollout call as 03_pnr_scan.py), one JSON per checkpoint (resumable), with every replay's seed, k,
  outcome, end step and wall time (new replays). Job: slurm/gt20_pilot.sbatch, array of 3 (one run each). Output data/gt20_pilot/.

## Step 2. Cost (results/gt20/cost.md, scripts/65_gt20_cost.py)

- From the pilot: wall seconds per new replay, successful and failed replays separately, and a fit seconds = a + b x replay steps.
- Projection uses the replay lengths already recorded in the existing K 4 scans (end_steps, every checkpoint of every scanned run), so the
  projected cost follows each run's real mix of early successes and 720-step failures. Pi0.5 seconds per step come from the existing
  Pi0.5 scans (minutes and end_steps in each scan JSON), since no Pi0.5 pilot runs this week; said so in the file.
- Designs: all 136 kept OFT failed runs vs 50 of them (fixed rule: round robin over the tasks in order, lowest
  episode id first within each task, until 50); checkpoints every 8 / 16 / 32;
  K 8 vs 20 (new replays = K minus the reusable ones); adaptive: K 20 only at checkpoints where the 4-replay failure fraction is in
  [0.25, 0.75] or differs from a neighbouring checkpoint (a change), K 4 elsewhere. Pi0.5: its 37 kept failed runs, same designs.
- GPU hours and days at 5 GPUs at once. Recommendation: the largest design that finishes in about 10 days.
- A first cost.md is written by a CPU job about 2 hours after the pilot starts (partial pilot data), and again when the pilot ends.

## Step 3. Pilot analysis (CPU, scripts/64_gt20_analysis.py, results/gt20/)

- Per pilot run: truth (failure fraction) with K 20, and K 8 and K 4 as random subsets of the 20 (10 draws each, fixed rng), on one
  figure. Mean absolute change vs K 20 for K 4 and K 8 (mean over checkpoints and draws), and for the original K 4 (seed 0) truth.
- Nov 20 slide redraw for t00_e06_p0_s1: K 20 truth plus the existing seed 0 model predictions of data/regression_v2 (same models,
  colours and legend as 62_regression_plots.py); the old K 4 truth in light grey for reference.
- Each model's MSE vs the K 4 truth and vs the K 20 truth on the 3 pilot runs, at the checkpoints every 16 steps.

## Step 4. Free interim: pooled target (CPU, all existing data)

- Target at query k = failed replays / all replays over the scan checkpoints k-1, k, k+1 (the neighbours that exist); K in the noise
  floor = pooled replay count. Unscanned successes stay 0. Exclusions and t_pnr values stay as in plan_nov13.md (raw scans).
- 60_regression.py --target pooled (default raw, unchanged); all models, seeds 0 to 4, both policies; output data/gt20/pooled.
  61_regression_report.py writes results/gt20/pooled/ and results/gt20/pooled_main.md (same format as regression_v2/main.md),
  labelled as an interim smoothing, not the 20-replay ground truth.

## Step 5 (only if time allows). Batched replays

- Prototype: the 20 replays of one checkpoint together (one policy forward pass for the batch, separate simulators). Compare outcomes
  with the sequential replays of the same seeds on 2 checkpoints and report the speedup. Not used for the pilot unless outcomes match
  exactly (batched bf16 matmuls can differ numerically from batch 1, so exact match is not expected for free).

## Logging

Every job goes into results/LOG.md; results are committed and pushed, never data files.
