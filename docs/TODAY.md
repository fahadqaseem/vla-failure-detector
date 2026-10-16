# Today (Oct 15): first real PNR number on the MacBook before the meeting

Goal: one figure from real rollouts showing replay risk over time for one or two failed episodes, with
t_pnr marked, plus the replay determinism result. Small n is fine if it is honest. If setup blocks you,
bring the definition, the pipeline and the exact blocker.

Everything runs directly on the Mac (no Slurm). Timings below are unknown until step 1 prints the
seconds per policy query; update this file with the real numbers.

| step | command |
|---|---|
| 1. env check | `python scripts/00_check_env.py` (first run downloads the 15 GB checkpoint) |
| 2. one episode | `python scripts/01_collect.py --tasks 0 --episodes 1` |
| 3. determinism | `python scripts/02_replay_test.py --episode data/rollouts/t00_e00_n0.npz --steps 40 --full` |
| 4. failures fast | `python scripts/01_collect.py --tasks 0 1 --episodes 2 --noise_std 0.15` (induced, labelled) |
| 4b. natural failures | `python scripts/01_collect.py --tasks 0 1 2 3 4 5 6 7 8 9 --episodes 2` (only if time allows; failures are rare) |
| 5. PNR scan, 1 episode, full curve | `python scripts/03_pnr_scan.py --episodes "data/rollouts/<failed_id>.npz" --every 80 --K 3 --min_fail 2 --full_curve` |
| 6. analyse | `python scripts/04_analyze.py` |

Budget rule: if step 1 shows more than about 3 s per policy query, or the Mac is swapping heavily, skip 4b and scan only one induced
failure with `--every 80 --K 3`.

## What to say in the meeting

1. The definition (CLAUDE.md, "PNR estimator") and its parameters, including the reduced Mac settings.
2. Replay determinism: PASS or FAIL with the deviation in mm.
3. Per failed episode: t_pnr vs episode end. Induced and natural failures kept separate.
4. Next: line up t_pnr with human onset labels (FailureSpot annotations) and with a detector's first
   alarm, i.e. the detection window `t_alarm - t_pnr`. Then scale on Grid.
5. External check from Seongheon Park (Hide-and-Seek first author, Oct 14 email): their alarms were
   never tested for stop-and-hand-off, and the open problem is telling apart self-recoverable mistakes,
   failures needing intervention, and unrecoverable ones. Replay value answers the first split per
   moment: before PNR the robot would mostly recover by itself, after PNR it needs help. So an alarm
   before PNR is an unnecessary stop, and the ideal alarm sits at PNR. 04_analyze.py already classifies
   alarms as early / in window / late / unnecessary stop.
6. Ask Prof. Zhu: is there access to the 250 annotated rollouts with sim states (or initial state +
   actions so states can be rebuilt)? That would give t_onset on the same episodes.

## First prompt to paste into Claude Code

```
Read CLAUDE.md, docs/SETUP.md and docs/TODAY.md. My lab meeting is today and we are running
everything on this MacBook for now (no Grid). First check the machine: chip, memory, macOS
version, free disk, whether conda exists, and whether ~/openvla-oft, ~/LIBERO and the Hugging Face
cache already exist. This Mac has 24 GB, which is tight for the 7B model: before loading it, list
which big apps are running so I can quit them, and while it runs report memory pressure and swap
(vm_stat / memory_pressure). Show me a plan, then
set up the environment from docs/SETUP.md step 2 and go through TODAY.md one step at a time.
After each step tell me the result in two lines and add a row to results/LOG.md. Never estimate
a number: only report what the scripts print.
```
