# Week 2 plan (Oct 23 to about Oct 26, 2026)

Goal: more timed failures, a look-ahead upper bound, cheaper models, then one final comparison.
Everything runs as Slurm chains submitted up front (`slurm/week2_submit.sh`), so it finishes without the
VS Code session. New results only in `results/week2/`; report jobs commit and push them. `scripts/status.sh`
prints the state in under 15 lines. Rules from CLAUDE.md hold (numbers only from results/, LOG.md, no pooling
of natural and perturbed without saying so).

GPU budget: at most 4 L40S jobs at once. Phase A arrays use at most 3 at once, Phase B at most 1.
GPU-hour estimates come from this week's jobs (sacct): perturbed collection 0.28 h per 50 episodes
including the replay gate, pre-check about 0.1 h per task, full scan 0.68 h per failure (mean of 159).

## Phase A: more timed failures (GPU, starts first)

- Tasks 0, 1, 4, 5, 6, 7, 8 (tasks 2, 3, 9 stay excluded: replay gate failed Oct 19). 100 new perturbed
  episodes per task = initial states 0 to 49 with seeds 1 and 2 (the old episodes used seed 0; the
  perturbation is drawn from (seed, task, init index, attempt), so the draws do not overlap). Same settings
  (2 to 3 cm, yaw up to 15 deg, validity checks). Ids `tXX_eYY_p0_s1`, `_s2`. Output `data/perturbed_v2/`.
- Chain: collection + replay gate (array of 7, at most 3 at once) -> pre-check (array of 7) -> scan list +
  full-scan array (K 4, every 8 steps, noise 0.05, 200 extra steps; at most 3 at once) -> K 16 refinement ->
  Phase D.
- Replay gate per task (first episode, query 1 and the middle query, 10 mm over 80 steps and same outcome).
  If it fails, the task writes GATE_FAIL, gets no pre-check or scan, and the chain continues with the others.
- K 16 near the boundary (CLAUDE.md decision 1, never run so far): for every failure with t_pnr > 0 (old and
  new), the two checkpoints around the boundary are t_pnr - 8 (last recoverable) and t_pnr. "Close to tau"
  (my rule, decided now): 3 of 4 at t_pnr - 8 or 2 of 4 at t_pnr. Then both get 12 more replays (seed 1,
  so different noise), 16 in total, and recoverable = Jeffreys lower 0.25 quantile >= 0.5. t_pnr is recomputed
  with these counts; how many t_pnr values change is logged. Phase D uses the refined labels for all failures.
- Estimate: collection 4 GPU-h; pre-check 1.5 GPU-h; scans about 85 failures (the old rate was 60 scans per
  493 episodes) x 0.68 = about 58 GPU-h, about 20 h wall at 3 at once; refinement at most 10 GPU-h.

## Phase B: look-ahead upper bound (GPU, in parallel with A)

UPPER BOUND, NOT A DETECTOR: it uses the simulator at test time. Labelled that way in every table.
- Episodes: the 101 labelled failures (28 natural, 73 perturbed) and 150 successes: 10 natural per task
  (lowest initial-state index) and 50 perturbed (7 or 8 per task over the 7 tasks, lowest index).
- At every 16th step (every second query): restore (restore_query), 4 futures of 48 steps, noise 0.05.
- Signals per checkpoint: (a) fraction of futures where the eef moves less than 1 cm from start to end;
  (b) mean mlp risk at the last query of each future (the leave-one-task-out mlp that did not see the task);
  (c) whether any future succeeds (score = 1 if none succeeds).
- Alarm: threshold per signal, conformal 5% on the successes of the other tasks (leave-one-task-out).
- Estimate: about 7 GPU-h, plus model loading, 25 array tasks of 10 episodes, 1 at a time: about 9 h wall.

## Phase C: cheaper models on existing data (CPU, now)

Data: natural + perturbed (7 of 10 tasks), pooled and said so. Variants fixed now, all reported:
1. Rescue-chance regression `mlp_rescue`, `combined_rescue`: same networks, loss = MSE between the sigmoid
   output and the replay risk (1 - rescue fraction) at each query. Scans are every 8 steps, i.e. at every
   query, so no interpolation is needed. Successes that were not scanned get risk 0 (they succeeded);
   pre-check recoverable failures are masked. Alarm on the level and on CUSUM (`_cusum`).
2. Memory over the last 8 queries (PCA 128 of the VLA features fit on training rows, plus action chunk, eef,
   gripper; earlier windows repeat the first query): `gru` (GRU 64, last state -> linear) and `conv`
   (two 1D convolutions, 64 channels, kernel 3, ReLU, mean over time -> linear). Same labels and loss as mlp.
   Level and CUSUM.
3. Threshold drift: seen-task split, thresholds calibrated on natural successes only vs on pooled natural +
   perturbed successes; false alarms reported separately on held-out natural and perturbed successes.
Unseen (leave-one-task-out) and seen splits for 1 and 2. "Best of each family" for Phase D, rule fixed now:
most timely alarms on unseen tasks at fixed 5%, among variants with held-out false alarms <= 6%; ties go to
fewer false alarms. If none qualifies, the one with the fewest false alarms.

## Phase D: final report (after A)

All timed failures (old natural, old perturbed, new perturbed; refined labels). Models: progress, gated_mlp,
gated_combined, mlp_cusum, combined_cusum, the best Phase C variant of each family (rescue, memory), and
the Phase B upper bound as a separate row (on its own 101 failures + 150 successes). Same table as before:
timely / late / missed, false alarms on successes, unnecessary alarms on recoverable failures, median
detection window, bootstrap 95% intervals and difference from progress. Unseen tasks headline, seen secondary.

## Order of jobs

1. Phase C CPU jobs (start now, independent).
2. Phase A collection array (GPU, 3 slots), chained to pre-check, scans, refinement, Phase D.
3. Phase B array (GPU, 1 slot), chained to the CPU scoring and its report.
4. Each report job writes to results/week2/, then commits and pushes.
Expected end: Phase C about Oct 24, B about Oct 24, A and D about Oct 25 to 26.
