# HANDOFF: start here (written Oct 17, 2026)

Claude Code: read this file, then CLAUDE.md, docs/PLAN.md and docs/GRID.md, and continue the work
with Fahad. This file carries everything decided in the planning chat so far.

## 1. Where things stand

- Pilot on the MacBook (Oct 2 to Oct 16) is done. Results are in results/LOG.md:
  natural success 28/30; replay fidelity PASS (max drift 2.61 mm after restoring the OSC controller
  and gripper counter); MPS slice bug fixed with `hidden.clone()`.
  Induced failure t00_e00_n0.15 (task 0, init state 0): replay successes 3/3, 2/3, 3/3, 1/3, 1/3, 0/3
  at steps 0, 16, 32, 48, 64, 80, so t_pnr in 33 to 48 (a ramp). t00_e01_n0.15: t_pnr by 80.
  Natural failures t06_e00_n0 and t08_e01_n0 had no t_pnr (recoverable timeouts).
- Oct 16 group meeting (Prof. Zhu, Sai, Fahad) changed the goal: PREDICT t_pnr with a simple model.
  Details in CLAUDE.md, section "Current direction".
- RESCUE (arXiv 2610.13516, CSIRO, Oct 9 2026) already measures t_pnr by replay with the same
  settings we use. Our contribution is the predictor, unseen tasks, long-horizon LIBERO-10, and
  later rollback recovery. Fahad emailed RESCUE and this plan to Prof. Zhu on Oct 17.
- Mac is retired for heavy runs. Everything now runs on WSU Grid.
- Fahad works independently: own data, own labels, own code. Sai is a collaborator, not a dependency.
- Next in-person meeting: Friday Oct 23 (Prof. Zhu sends the time and room by Thursday night).

## 2. Immediate task: get Grid working (this is where to start)

Fahad connects VS Code to a Grid COMPUTE NODE (never the login node Warrior) following the official
WSU procedure written in docs/GRID.md. Login host grid.wayne.edu, AccessID password typed by Fahad.
The repo is cloned to ~/vla-failure-detector on Grid.

Step A. Discover the cluster (login node, read-only). Run and read:
```bash
hostname; whoami; echo $HOME
df -h $HOME | tail -1; quota -s 2>/dev/null | tail -3; ls -d /wsu/scratch* /scratch* 2>/dev/null
sinfo -o "%P %G %l %D %a" | head -25
sacctmgr -nP show assoc user=$USER format=account,partition,qos | head
module avail 2>&1 | grep -iE "cuda|conda|anaconda|python|gcc|git" | head -30
which git conda python3; python3 --version
```
Then fill in docs/GRID.md (host, partitions with L40S/H200, GPU request syntax, modules, storage
paths and quotas, time limits) and the TODOs in slurm/*.sbatch and slurm/common.sh.

Step B. Storage. The checkpoint is about 15 GB. If $HOME quota is small, set HF_HOME and the conda
env location on scratch/project storage, and write the choice into docs/GRID.md.

Step C. Environment (do installs in a batch or interactive GPU job if the login node is restricted):
follow docs/SETUP.md step 2 but for Linux + CUDA (not MPS). Pins that worked on the Mac pilot and
probably matter here too: numpy 1.26.4, mujoco 3.3.0, opencv-python 4.10.0.84, protobuf < 5.
torch: use the CUDA build that matches the Grid driver. Set MUJOCO_GL=egl, PYOPENGL_PLATFORM=egl.
Record every deviation in results/LOG.md.

Step D. Checks on a GPU node, in order, each logged in results/LOG.md:
1. `sbatch slurm/check.sbatch` (00_check_env.py)
2. collect 1 episode, then `slurm/replay.sbatch` (02_replay_test.py must PASS with drift in mm)
3. reproduce the pilot: scan t00_e00_n0.15 again on Grid and compare with the Mac result.

## 3. After Grid works (docs/PLAN.md has the day-by-day)

1. Make 01_collect.py also save per-step VLA hidden features (the same input SAFE uses), aligned
   with actions, eef position and sim states at chunk boundaries.
2. Collect natural runs on all 10 LIBERO-10 tasks until about 30+ natural failures. Add a slurm
   array job so tasks run in parallel.
3. Label t_pnr by replay on failures plus about 20 successes, RESCUE-compatible settings
   (tau 0.5, also 0.3 and 0.7; K 4 expanded to 16 near the switch; Jeffreys lower quantile).
   Ask Fahad before changing code defaults.
4. Load Fahad's own episode annotations (he will provide the file) and compare with replay t_pnr.
5. New script 06_train_predictor.py: per-step logistic regression, then a small MLP. Labels 0 before
   t_pnr, 1 after; successes all 0. Task-held-out split fixed BEFORE training.
6. Evaluate over the whole trajectory: per-step AUROC, |predicted t_pnr - true t_pnr| in steps,
   false alarms on successful runs. Baselines: timer (step count) and a SAFE-style probe trained on
   success/fail labels. Watch the timeout trap (episode length alone separates failures).
7. Thursday night: 3 slides (RESCUE gap, labels, results table).

## 4. How to work with Fahad

- Explain plainly and briefly. Fahad must be able to explain every line in a meeting.
- Show a plan before big changes; one step at a time; report each result in two lines.
- Never invent numbers. Every number comes from a script and is logged in results/LOG.md.
- Never type passwords or handle Duo; Fahad does logins himself.
- Never run the model on the login node.
- No double hyphens in prose written for Fahad.
- Keep the GitHub repo private.
