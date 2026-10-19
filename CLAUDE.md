# vla-pnr: point of no return for VLA failure detection

> New session? Read docs/HANDOFF.md first: it has the latest status and the next step.

Owner: Fahad Qaseem Khawar (MS CS, Wayne State). Research volunteer in Prof. Yi Zhu's REIL Lab.
Weekly group meeting with Prof. Zhu and Sai. This repo is Fahad's own pipeline, written from scratch.

## The research question

A VLA policy that is going to fail usually passes a point of no return (PNR) well before anyone,
human or detector, notices. We use the lab's shared terms (agreed in the Oct 2, 2026 meeting):

- `t_pnr`   point of no return: first time after which the episode almost surely fails.
- `t_alarm` time a failure detector fires.
- `t_onset` time the failure becomes visible. Since Oct 18 (no human annotations this week) it comes
  from an automatic detector, `scripts/07_auto_onset.py`: first missed grasp, drop, stuck or wrong-object
  event in a failed episode. Events in successful episodes are counted as recovered slips.
- Detection window    = `t_alarm - t_pnr`   (Fahad's focus: make this small).
- Intervention window = `t_onset - t_pnr`.

## Current direction (decided in the Oct 16, 2026 group meeting with Prof. Zhu)

The main goal is now to PREDICT `t_pnr`, not only measure it.

- Train a simple model (logistic regression first, then a small MLP) that reads per-step signals
  (VLA hidden features, action consistency, actions, arm position) and outputs, for every step,
  0 = before `t_pnr`, 1 = after `t_pnr`. Prof. Zhu: keep the method clean and elegant.
- Labels: per step, 0 before `t_pnr` and 1 after. `t_pnr` depends on the episode (not fixed at 120).
  Successful episodes and recoverable failures (no `t_pnr`) are all 0.
- Evaluation: binary classification over the WHOLE trajectory against these labels (not against
  the final failure label, not only the first 120 steps). Also report |predicted t_pnr - true t_pnr|
  in steps and false alarms on successful runs. Test on held-out (unseen) tasks, leave-one-task-out.
- The threshold that defines `t_pnr` is tau = 0.5 (see "Predictor decisions"). tau 0.3, tau 0.7
  and "fails every replay" are reported only as a sensitivity check from the 3 full scans.
- Recovery comes after prediction works, and must happen BEFORE `t_pnr`. Prof. Zhu's idea: if the
  predicted risk is high, roll back to an earlier state with lower risk; if low, simply rerun.
- Timeout trap: OpenVLA-OFT failures are timeouts, so episode length alone separates failures
  from successes (timer AUROC 99.5 on whole runs). Always include a timer baseline and make sure
  the model cannot win by counting steps.

### Predictor decisions (Fahad, Oct 17, 2026)

1. Labels by replay, RESCUE-compatible: K = 4 replays per checkpoint, success estimate = lower 0.25
   quantile of Beta(k + 1/2, K - k + 1/2) (Jeffreys), recoverable if estimate >= tau, tau = 0.5.
   UPDATE Oct 18 (Fahad): labels come from FULL scans (every checkpoint, every 8 steps), not binary
   search, because the 3 test scans showed success probability does not only go down (t01_e41:
   binary search 40 vs full scan 152). Full scans run on all natural failures and 20 successes
   (2 per task). `t_pnr` = first checkpoint from which every later checkpoint is not recoverable.
   Afterwards K = 16 is added at the two checkpoints around the tau 0.5 boundary, only where the
   estimate there is close to tau. The 3 first scans also give the sensitivity check (tau 0.3,
   tau 0.7, "fails every replay").
2. Target: the replay risk score (1 - value) plus the 0/1 label (0 before `t_pnr`, 1 after).
   Loss = BCE on the label + MSE on the risk.
3. Inputs: VLA hidden features (SAFE-style, last layer at the action tokens), the action chunk,
   eef position / proprio. NEVER the step index or anything that counts time.
4. Metrics: timely recall at 5% false alarms on successful runs (threshold set by conformal
   calibration on successes), |predicted t_pnr - true t_pnr| in steps, eta = predicted / true
   `t_pnr`, per-step AUROC over the whole run, and the number of late detections (after `t_pnr`).
   Timely = alarm at or before `t_pnr` (RESCUE-style), always reported together with the 5% false-alarm
   limit on successes. Also report lead time = `t_pnr` - alarm step for every failure (Fahad, Oct 18).
   Training uses ALL natural successes (label 0, MSE masked where not scanned), each episode weighted
   equally and positives/negatives balanced. The threshold is calibrated on all successes of the
   training tasks (cross-fitted scores, so each comes from a model that did not see that task);
   false alarms are counted on all successes of the held-out task. AUROC from scikit-learn.
5. Baselines: timer (step count), SAFE-style probe (success/fail labels), steps-since-progress
   (RESCUE: chunk boundaries since the eef last moved more than 0.01 m between successive boundaries).
   Combined model (Fahad, Oct 18 late): MLP on the inputs of 3. plus eef displacement over the last
   4 chunks, steps-since-progress and averaged deltas over the last 4 queries; no step index.
   Headline columns: unnecessary alarms on recoverable failures, and a time-matched AUROC (label-1 steps
   vs success steps in the same 64-step bin only), next to the whole-run AUROC.
6. Evaluation: leave-one-task-out over the 10 LIBERO-10 tasks (Fahad, Oct 18; replaces the single
   fixed split): train on 9 tasks, test on the 10th, repeat for each task, report per task and pooled.
   Tasks with no labelled failure still give false alarms on their successes.
7. Labelling runs as Slurm array jobs (one array task per episode).
8. Doomed-from-start episodes (`t_pnr` = 0: every replay fails, even from step 0) stay in training
   (label 1 at every step) but are flagged, and excluded from the timing metrics
   (|t_pnr error|, eta, timely recall, late detections). Per-step AUROC still includes them.

### More failures: perturbed-natural episodes (Fahad, Oct 18, 2026)

- Collection (`01_collect.py --perturb`, `pnr/perturb.py`, `slurm/collect_perturbed.sbatch`): for each
  LIBERO-10 task and each initial state 0 to 49, move every movable object (`objects_dict`, not fixtures)
  by a random 2 to 3 cm in a random direction in x, y and rotate it about the vertical axis by up to
  15 degrees. Seeded per (seed, task, init index, attempt). No action noise, features saved.
- Invalid start, judged after the 10 settling steps against the UNPERTURBED start after the same steps
  (LIBERO starts hold objects a few cm above the table and some overlap slightly, so absolute checks reject
  every start): some object more than 1 cm (x, y or z) from its unperturbed settled place plus its shift,
  or tilted more than 10 degrees from its unperturbed settled orientation (yaw ignored), or the task
  already solved. Then a new attempt is drawn; after 20 invalid attempts that initial state is skipped.
- Episodes go to `data/perturbed/taskXX/`, ids `tXX_eYY_p0`, labelled "perturbed-natural" (field
  `perturbed`, with `perturbation` and `base_init_state`). Never pooled with the original 500 natural
  episodes in a statistic without saying so.
- Pre-check (`09_precheck.py`, Fahad Oct 18 late: 3 of 4, checkpoint near the end) for every new failure:
  K = 4 replays (noise 0.05, extra_steps 200) from the last chunk boundary at or before t_end - 32. If 3 or
  more succeed (the tau 0.5 bar): "recoverable (pre-check)", no full scan (label 0 at every step; the last
  checkpoint is recoverable, so `t_pnr` would be None anyway, apart from replay noise). Otherwise full scan
  (every 8 steps, K 4, tau 0.5) as an array job (`slurm/perturbed_submit_scans.sbatch` writes
  `results/perturbed_scans/targets.txt` and submits `scan_array.sbatch`, output `data/perturbed_scans/`).
- The replay gate (`02_replay_test.py --full`) runs on the first perturbed episode of each task before
  its pre-checks.

Cite: RESCUE (arXiv 2610.13516), PREFAIL (arXiv 2607.16921), CheckVLA (arXiv 2607.26789).

The pilot (Oct 2 to Oct 16, Mac) measured `t_pnr` = 33 to 48 on one induced failure and found the
two natural failures recoverable. The Oct 2 numbers (alarm about 90 steps after PNR, onset about
45 after alarm) are still guesses.

Independence: Fahad builds his own data, labels and models on Grid. Do not read, copy or depend on
Sai's code or data. Sai is a collaborator Fahad talks to, not a dependency. All labels come from
Fahad's own replay scans and automatic onset detector (no human annotations this week, Oct 18).

## Plan of work (details and dates in docs/PLAN.md)

1. Move the pipeline to WSU Grid (docs/GRID.md).
2. Collect episodes with per-step hidden features saved, plus sim states at chunk boundaries.
3. Label `t_pnr` by replay on 30 to 50 failures plus successful runs (RESCUE-compatible settings).
4. Automatic `t_onset` from sim-state events (07_auto_onset.py); intervention window = `t_onset - t_pnr`.
5. Train the per-step predictor; evaluate on unseen tasks against timer and SAFE-style baselines.
6. Later: decision value (RESCUE break-even false alarm rate) and recovery by rollback.

## Why replay value is the right lens (Seongheon Park, Hide-and-Seek first author, email Oct 14 2026)

- Their xArm experiments measured detection accuracy and timeliness only, not stop-and-hand-off.
- Their "slightly pre-onset" LIBERO alarms are averages over correctly detected failures only.
- Detector is light, but end-to-end response latency was not evaluated.
- Open problem he named: separate (a) mistakes the robot recovers from on its own, (b) failures
  that need intervention, (c) failures where recovery is no longer possible. A useful warning
  lets someone intervene while it can still change the outcome, without stopping a robot that
  would have recovered. He suggested judging detectors by intervention outcomes (successful
  recovery, unnecessary stops).

Our replay value curve gives exactly that split for each moment of an episode:
value high = (a) self-recoverable; `t_pnr` = the policy can no longer recover by itself, so
from here on the episode needs intervention (b). Separating (b) from (c) would need a stronger
recovery oracle (future work). So an alarm before `t_pnr` risks an unnecessary stop, and every
step after `t_pnr` shrinks the time left to intervene: the ideal alarm sits right at `t_pnr`.
`04_analyze.py` reports the replay value at each alarm and classifies alarms as early
(robot would likely recover, value >= 0.5), in window (after PNR, before onset) or late (after onset).

## PNR estimator (operational definition, always report the parameters)

Pilot rule, still the code default in `03_pnr_scan.py`. Label jobs pass the RESCUE-compatible values
below as flags (`slurm/scan_array.sbatch`); no binary-search labeller is written (dropped Oct 18).
From a recorded failed episode, restore the sim state at checkpoints every `--every` policy steps
(default 40, must be a multiple of the action chunk, 8). From each checkpoint run `K` replays
(default 5) of the same policy with Gaussian action noise on the 6 arm dims
(`--noise_std`, default 0.05, env action units in [-1, 1]; gripper untouched).
value(t) = fraction of replays that succeed. risk(t) = 1 - value(t).
`t_pnr` = first checkpoint where at least `m` of `K` replays fail (default 3 of 5) AND every
later checkpoint also has at least `m` failures. If no such checkpoint exists, `t_pnr = None`.
Replays may run `--extra_steps` (default 200) past the 520-step limit; otherwise late checkpoints
look doomed only because the clock runs out. Most LIBERO failures are timeouts, so this matters.
PNR depends on noise level, K and extra_steps. It is an estimate, not ground truth. Say so on slides.

RESCUE-compatible setting (used for all labels from now on, so numbers compare with RESCUE):
tau = 0.5, K = 4 replays per checkpoint (K = 16 later at the two checkpoints around the boundary
where the estimate is close to tau), success estimate = lower 0.25 quantile of Beta(k + 1/2, K - k + 1/2)
(Jeffreys), from FULL scans (every 8 steps; binary search was dropped Oct 18, see "Predictor
decisions"). With K = 4, tau 0.5 means at least 3 of 4 replays succeed, so `03_pnr_scan.py
--K 4 --min_fail 2` gives the same `t_pnr`. tau 0.3, tau 0.7 and "fails every replay" are a sensitivity
check from the 3 full scans only. RESCUE's horizon is the LAST recoverable checkpoint; our `t_pnr`
is the first checkpoint after it. Noise 0.05 and extra_steps 200 stay as above. Ask Fahad before
any other change to the definition or defaults.

## Setup facts (verified from the openvla-oft source, Oct 2026)

- Policy: OpenVLA-OFT, checkpoint `moojink/openvla-7b-oft-finetuned-libero-10`
  (L1 regression action head, deterministic; 2 images: agentview + wrist; 8-dim proprio).
- Benchmark: LIBERO-10 (`libero_10`), 10 tasks, 50 fixed initial states per task.
- Max policy steps 520. The eval script first takes 10 no-op steps so objects settle.
- Action chunk = 8 (`NUM_ACTIONS_CHUNK`), executed open loop, then the model is re-queried.
  Only restore sim state at a chunk boundary (empty action queue).
- Images are rotated 180 degrees before the policy (`get_libero_image`). Use the repo helpers,
  never re-implement preprocessing.
- Sim state: `env.get_sim_state()` / `env.reset(); env.set_init_state(state)` (LIBERO ControlEnv).
- OFT success on LIBERO-10 is in the mid 90s percent, so natural failures are rare
  (about 1 in 15 to 20). Collect enough episodes or use induced failures and label them.
- Compute NOW: WSU Grid (see docs/GRID.md). The Mac was used only for the Oct 16 pilot.
- Mac notes (pilot only): Fahad's MacBook (Apple Silicon). Policy runs on the Mac GPU via MPS
  (`pnr/sim.py` patches openvla-oft's DEVICE; `PNR_DEVICE=cpu` disables). The Mac has 24 GB unified
  memory: tight, since the 7B model in bf16 is about 15 GB. Close other apps (browsers, Docker, IDE
  extensions) before loading the model, load it once per script run, and watch Activity Monitor >
  Memory: if memory pressure stays red or swap grows past a few GB, stop and say so (move to Grid).
  Only if PyTorch reports "MPS backend out of memory", try PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.0 for one
  run and record it in results/LOG.md (it lifts the MPS memory cap and can make the Mac sluggish).
  macOS 14+ needed for bf16 on MPS. Do not set MUJOCO_GL on
  the Mac: robosuite picks `cgl` itself. Run scripts directly with python, no Slurm. Expect it to be
  several times slower than a datacenter GPU, so use small runs: induced failures, `--every 80 --K 3`.
  If bf16 fails on MPS, try float16 before anything else and record it in results/LOG.md.
- Grid: Slurm, L40S GPUs (H200 available). `slurm/` templates are ready;
  headless rendering there needs `MUJOCO_GL=egl`, `PYOPENGL_PLATFORM=egl`.

## Repo map

- `pnr/sim.py`        policy loading, env creation, the single rollout function (record or replay).
- `pnr/pnr.py`        PNR rule and risk-curve maths (pure numpy, unit tested).
- `scripts/00_check_env.py`      imports, GPU, LIBERO tasks, one short dry run.
- `scripts/01_collect.py`        record episodes (actions, eef, sim states at chunk boundaries).
- `scripts/02_replay_test.py`    restore a checkpoint with no noise; must reproduce the episode.
- `scripts/03_pnr_scan.py`       PNR scan over failed episodes.
- `scripts/04_analyze.py`        table + figures; optional `--onsets` and `--alarms` CSVs.
- `scripts/07_auto_onset.py`     automatic t_onset from saved sim states (CPU); results/auto_onset.csv.
- `scripts/07_figures.py`        t_pnr distribution and predicted vs replay risk plots.
- `pnr/perturb.py`     perturbed initial states (object shift 2-3 cm, yaw up to 15 deg) and validity checks.
- `scripts/09_precheck.py`       4 replays at 75% of a new failure: recoverable (pre-check) or scan.
- `scripts/compare_episodes.py`  two recordings of one episode must be identical (gate after code changes).
- `scripts/pick_failures.py`     fixed rule to pick natural failures from different tasks for scans.
- `scripts/scan_targets.py`      fixed list of episodes to label by full scan (results/full_scans/targets.txt).
- `scripts/check_monotonic.py`   full scan vs binary search t_pnr, sensitivity to tau.
- `scripts/06_train_predictor.py` per-step predictor (logistic regression, small MLP), leave-one-task-out.
- `slurm/*.sbatch`               jobs (L40S on galhp). `feature_check` = gate, `collect_array` = 10 tasks
                                 x 50 init states, `scan_array` = full scans on every line of targets.txt.
- Episode files also hold `features` (n_queries, 56, 4096) float16 = last-layer LLM hidden states at
  the 56 action tokens (input of the action head), and `features_mean` (n_queries, 4096).
  `features[k]` belongs to `query_steps[k]` and produced `actions[8k : 8k+8]`.
- `tests/test_pnr.py`            unit tests for the PNR rule (run: `python -m pytest -q`).
- `data/` rollouts and scans (git-ignored). `results/` tables and figures for meetings.

## Rules for working in this repo

- Never invent or estimate a number for a slide or email. Every number must come from a file
  in `results/` produced by a script in this repo, and the command that made it is logged
  in `results/LOG.md` (date, command, git commit, notes).
- Label induced failures (collected with noise) as induced. Never mix them with natural
  failures in one statistic without saying so.
- Run heavy jobs with `sbatch` on GPU nodes, never on the login node. Check `squeue` before
  resubmitting. Start small (1 task, 2 episodes), then scale.
- Before any PNR scan, `02_replay_test.py` must pass on that setup (restored no-noise replay
  matches the original trajectory and outcome). If it fails, stop and debug determinism first.
- Keep code simple and readable. Fahad must be able to explain every line in a meeting.
- Ask before changing the PNR definition or defaults. Write changes into this file.

## Related work (know how we differ)

- SAFE (Gu et al., NeurIPS 2025): probe on last-layer VLA features, trajectory labels,
  functional conformal thresholds. Labels every step of a failed run as failure.
- FailureSpot (Zhu lab, arXiv 2609.04277): timestamp-level detection, action-derived weak
  supervision plus active learning for human onset labels. Recovered deviations still labelled failure.
- Hide-and-Seek (Park et al., arXiv 2605.30834): learns failure signals from trajectory labels with
  inter/intra-trajectory contrastive losses; alarms land near annotated onset; xArm 6 real robot.
- RESCUE (Ahmedt-Aristizabal et al., CSIRO, arXiv 2610.13516, Oct 9 2026): CLOSEST PRIOR WORK.
  Same replay method as ours (restore at chunk boundaries, sigma 0.05 on 6 arm dims, replay fidelity
  check). Defines the recoverability horizon (last checkpoint with success >= tau), which is our
  `t_pnr`. OpenVLA-OFT and pi0.5 on LIBERO-Spatial / LIBERO-Plus (220-step budget), 1,562 episodes,
  128,340 branches; median horizon step 44 for OFT. Shows most monitors alarm after the horizon and
  that stop-and-reset only pays off below a 2 to 3% false alarm rate. Interventions: CONTINUE and
  one scripted RECOVER.
  What they do NOT do (our gap): no new detector is trained, nothing predicts the horizon; splits are
  not task-disjoint (no unseen-task claim); only short tasks (no LIBERO-10 long horizon); no learned
  or rollback recovery. We must not claim that measuring PNR by replay is new.
- CheckVLA (Liu et al., arXiv 2607.26789): intervention-relative irreversibility time from fixed repairs.
- PREFAIL (Shangguan et al., arXiv 2607.16921): latest actionable intervention time for lift-and-place.
- VLA-FAIL (arXiv 2606.21386): AUCPDT metric for detection accuracy plus timing.
- Also: FIPER, ActProbe (action signals + task embedding), TDQC (value calibration), PFD (perturbation uncertainty).

## How to work with Fahad

- Start every reply with a short summary of at most 5 bullets in plain words. Put details below it
  only if needed (Fahad, Oct 18 2026: long updates are too long to read).

## Style

Plain, short explanations. No double hyphens in prose written for Fahad.
