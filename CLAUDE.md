# vla-pnr: point of no return for VLA failure detection

Owner: Fahad Qaseem Khawar (MS CS, Wayne State). Research volunteer in Prof. Yi Zhu's REIL Lab.
Weekly group meeting with Prof. Zhu and Sai. This repo is Fahad's own pipeline, written from scratch.

## The research question

A VLA policy that is going to fail usually passes a point of no return (PNR) well before anyone,
human or detector, notices. We use the lab's shared terms (agreed in the Oct 2, 2026 meeting):

- `t_pnr`   point of no return: first time after which the episode almost surely fails.
- `t_alarm` time a failure detector fires.
- `t_onset` time a human can see the failure (human annotation, FailureSpot style).
- Detection window    = `t_alarm - t_pnr`   (Fahad's focus: make this small).
- Intervention window = `t_onset - t_pnr`.

Observed so far (rough, from the Oct 2 discussion, not yet measured by this repo): alarm about
90 steps after PNR, onset about 45 steps after alarm. Prof. Zhu: detecting at or before PNR would
beat existing papers; PNR as a concept is not studied in prior work. Keep the focus on
monitoring and detection. Recovery comes later.

Division of labour: Sai owns PACER (pre-PNR anomaly detection over the first 120 steps).
Do not read, copy or depend on Sai's code. Fahad owns the post-PNR side: measuring PNR and
shrinking the detection window.

## Plan of work

1. Measure `t_pnr` per failed rollout with simulator replay (this repo, `scripts/03_pnr_scan.py`).
2. Put `t_pnr`, `t_alarm` (from a detector) and `t_onset` (human labels) on one timeline.
3. Later: train a detector on replay risk labels instead of trajectory or onset labels, and
   compare label types at a matched 5% false alarm rate (median lag, misses, AUROC).
   Fallback result if that fails: the "two clocks" characterisation (PNR vs onset) on its own.

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
- Compute NOW: Fahad's MacBook (Apple Silicon). Policy runs on the Mac GPU via MPS
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
- Compute LATER: WSU Grid, Slurm, L40S GPUs (H200 available). `slurm/` templates are ready;
  headless rendering there needs `MUJOCO_GL=egl`, `PYOPENGL_PLATFORM=egl`.

## Repo map

- `pnr/sim.py`        policy loading, env creation, the single rollout function (record or replay).
- `pnr/pnr.py`        PNR rule and risk-curve maths (pure numpy, unit tested).
- `scripts/00_check_env.py`      imports, GPU, LIBERO tasks, one short dry run.
- `scripts/01_collect.py`        record episodes (actions, eef, sim states at chunk boundaries).
- `scripts/02_replay_test.py`    restore a checkpoint with no noise; must reproduce the episode.
- `scripts/03_pnr_scan.py`       PNR scan over failed episodes.
- `scripts/04_analyze.py`        table + figures; optional `--onsets` and `--alarms` CSVs.
- `slurm/*.sbatch`               job templates (fill in partition and conda env).
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
- PREFAIL: replay-based "t_stop" labels. Closest prior to PNR. Must be read and distinguished.
- Also: FIPER, ActProbe (action signals + task embedding), TDQC (value calibration), PFD (perturbation uncertainty).

## Style

Plain, short explanations. No double hyphens in prose written for Fahad.
