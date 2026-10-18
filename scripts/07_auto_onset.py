"""Automatic failure onset from saved sim states (CPU only, no policy, no rendering).

At every chunk boundary (every 8 policy steps) the saved sim state is restored in a LIBERO env without
cameras, and we read finger joint positions and object positions. The gripper command comes from the
recorded actions (last dim: +1 close, -1 open). Events, each stamped with the boundary step where it
is first seen:
  missed_grasp  the gripper was commanded closed during the last chunk, the fingers are fully closed
                (width < --closed_width) and no object is held.
  drop          an object held at the previous boundary is no longer held and fell relative to the eef
                (object z down minus eef z down > --drop_dz), while the gripper was commanded closed the
                whole chunk (no open command).
  stuck         the eef has not moved more than --move_m between successive boundaries for --stuck_n
                boundaries in a row (RESCUE steps-since-progress); stamped when the count reaches stuck_n.
  wrong_object  a held object is not one of the task's objects of interest (LIBERO obj_of_interest).
"held" = object raised more than --lift_dz above its height at step 0 and within --hold_dist of the eef.
Repeated events: missed_grasp and stuck are counted once per run of consecutive boundaries; wrong_object
once per object.
t_onset (automatic) = step of the first event in a failed episode. Events in successful episodes are
"recovered slips". If scans are given, the intervention window t_onset - t_pnr (tau 0.5) is added.

python scripts/07_auto_onset.py --episodes "data/natural/*/*.npz" --scans "data/full_scans/*.json" --out results/auto_onset.csv
python scripts/07_auto_onset.py --episodes data/natural/task02/t02_e10_n0.npz --verbose   # per-boundary trace
"""

import argparse
import csv
import glob
import json
import os

import numpy as np
from libero.libero import benchmark, get_libero_path
from libero.libero.envs.env_wrapper import ControlEnv

p = argparse.ArgumentParser()
p.add_argument("--episodes", default="data/natural/*/*.npz")
p.add_argument("--scans", default="data/full_scans/*.json")
p.add_argument("--out", default="results/auto_onset.csv")
p.add_argument("--closed_width", type=float, default=0.005, help="finger opening (m) below which the gripper is fully closed")
p.add_argument("--lift_dz", type=float, default=0.03, help="rise (m) above the step-0 height that counts as lifted")
p.add_argument("--hold_dist", type=float, default=0.10, help="max object-eef distance (m) for a held object (moka pots are held by the handle, about 8 cm from their origin)")
p.add_argument("--drop_dz", type=float, default=0.02, help="fall (m) between boundaries that counts as a drop")
p.add_argument("--move_m", type=float, default=0.01)
p.add_argument("--stuck_n", type=int, default=5)
p.add_argument("--tau_min_success", type=int, default=3, help="t_pnr rule, as in 06_train_predictor.py (tau 0.5, K 4)")
p.add_argument("--verbose", action="store_true")
args = p.parse_args()

suite = benchmark.get_benchmark_dict()["libero_10"]()
_envs = {}


def get_env(task_id):
    if task_id not in _envs:  # keep one env open at a time (episodes come sorted by task)
        for old in _envs.values():
            old.close()
        _envs.clear()
        task = suite.get_task(task_id)
        bddl = os.path.join(get_libero_path("bddl_files"), task.problem_folder, task.bddl_file)
        env = ControlEnv(bddl_file_name=bddl, has_renderer=False, has_offscreen_renderer=False, use_camera_obs=False)
        env.reset()
        _envs[task_id] = env
    return _envs[task_id]


def t_pnr_from_scan(scan):  # same rule as 06_train_predictor.py
    ok = [sum(s) >= args.tau_min_success for s in scan["successes"]]
    if ok[-1]:
        return None
    i = len(ok) - 1
    while i > 0 and not ok[i - 1]:
        i -= 1
    return scan["checkpoints"][i]


def detect(ep):
    env = get_env(int(ep["task_id"]))
    e = env.env
    objs = list(e.objects_dict)
    finger_addr = [e.sim.model.get_joint_qpos_addr(j) for j in e.robots[0].gripper.joints]
    steps = ep["query_steps"].astype(int)
    eef, actions = ep["eef"], ep["actions"]

    events = []  # (step, kind, detail)
    z0 = None
    prev_held, prev_z = set(), None
    still, in_miss, wrong_seen = 0, False, set()
    for k, s in enumerate(steps):
        env.set_init_state(ep["query_states"][k])
        pos = {o: e.sim.data.body_xpos[e.obj_body_id[o]].copy() for o in objs}
        z = {o: pos[o][2] for o in objs}
        if z0 is None:
            z0 = z
        width = e.sim.data.qpos[finger_addr[0]] - e.sim.data.qpos[finger_addr[1]]
        held = {o for o in objs if z[o] - z0[o] > args.lift_dz and np.linalg.norm(pos[o] - eef[s]) < args.hold_dist}
        prev_cmd = actions[steps[k - 1]:s, -1] if k > 0 else np.zeros(0)
        closed_cmd = len(prev_cmd) > 0 and (prev_cmd > 0).all()

        miss = closed_cmd and width < args.closed_width and not held
        if miss and not in_miss:
            events.append((int(s), "missed_grasp", f"finger width {width * 1000:.1f} mm"))
        in_miss = miss
        for o in prev_held - held:
            fall = (prev_z[o] - z[o]) - (eef[steps[k - 1]][2] - eef[s][2])  # relative to the gripper
            if closed_cmd and fall > args.drop_dz:
                events.append((int(s), "drop", f"{o} fell {fall * 100:.1f} cm below the gripper"))
        for o in held - set(e.obj_of_interest) - wrong_seen:
            events.append((int(s), "wrong_object", o))
            wrong_seen.add(o)
        if k > 0:
            still = still + 1 if np.linalg.norm(eef[s] - eef[steps[k - 1]]) <= args.move_m else 0
            if still == args.stuck_n:
                events.append((int(s), "stuck", f"no move > {args.move_m} m for {args.stuck_n} boundaries"))
        if args.verbose:
            print(f"  step {s:3d} width {width * 1000:5.1f} mm  cmd {prev_cmd.mean() if len(prev_cmd) else 0:+.2f}  "
                  f"held {sorted(held)}  still {still}")
        prev_held, prev_z = held, z
    return events


scans = {}
for f in glob.glob(args.scans):
    s = json.load(open(f))
    scans[s["episode_id"]] = s

kinds = ["missed_grasp", "drop", "stuck", "wrong_object"]
rows = []
for f in sorted(glob.glob(args.episodes)):
    ep = np.load(f, allow_pickle=True)
    if bool(ep["induced"]):
        continue
    eid = os.path.splitext(os.path.basename(f))[0]
    if args.verbose:
        print(eid, str(ep["description"]))
    events = detect(ep)
    success = bool(ep["success"])
    t_onset = events[0][0] if events and not success else None
    scan = scans.get(eid)
    t_pnr = t_pnr_from_scan(scan) if scan and not success else None
    row = dict(episode_id=eid, task_id=int(ep["task_id"]), success=int(success), t_end=int(ep["t_end"]),
               **{f"n_{k}": sum(ev[1] == k for ev in events) for k in kinds},
               t_onset=t_onset, onset_event=events[0][1] if t_onset is not None else "",
               scanned=int(scan is not None), t_pnr=t_pnr,
               window=(t_onset - t_pnr) if t_onset is not None and t_pnr is not None else None,
               events="; ".join(f"{s} {k} ({d})" for s, k, d in events))
    rows.append(row)
    print(f"{eid} success={success} t_onset={t_onset} t_pnr={t_pnr} | {row['events']}", flush=True)

os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
with open(args.out, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)

fails = [r for r in rows if not r["success"]]
succ = [r for r in rows if r["success"]]
print(f"\n{len(rows)} episodes. Failures: {len(fails)}, with an automatic onset: {sum(r['t_onset'] is not None for r in fails)}. "
      f"Successes with at least one event (recovered slips): {sum(any(r[f'n_{k}'] for k in kinds) for r in succ)} of {len(succ)}.")
for k in kinds:
    print(f"  {k}: in failures {sum(r[f'n_{k}'] > 0 for r in fails)}/{len(fails)}, "
          f"in successes {sum(r[f'n_{k}'] > 0 for r in succ)}/{len(succ)}; first event in failures: "
          f"{sum(r['onset_event'] == k for r in fails)}")
win = [r for r in fails if r["window"] is not None]
if win:
    print("Intervention window t_onset - t_pnr (steps): " + ", ".join(f"{r['episode_id']} {r['window']}" for r in win))
