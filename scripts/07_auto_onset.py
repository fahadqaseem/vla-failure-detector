"""Automatic failure onset from saved sim states (CPU only, no policy, no rendering).

At every chunk boundary (every 8 policy steps) the saved sim state is restored in a LIBERO env without
cameras, and we read finger joint positions and object positions. The gripper command comes from the
recorded actions (last dim: +1 close, -1 open). Events, each stamped with the boundary step where it
is first seen:
  missed_grasp  (a) the gripper was commanded closed during the last chunk, the fingers are fully closed
                (width < --closed_width) and no object is held; or (b) a grasp attempt ends without
                lifting anything: the gripper is commanded closed (last action of a chunk +1) and later
                open again (last action -1), no object was held at any boundary in between, and the
                gripper touched an object during the attempt: at some boundary a finger geom is in
                contact with an object geom, or, after a whole chunk commanded closed, the fingers stopped
                (width changed < --stop_mm since the last boundary) before fully closed while no finger
                touches a fixture (stove knob, drawer or microwave handle: task 2 turns the knob in
                every successful run, so a stop on a fixture is not a grasp of an object). This catches grasps
                that close on a handle and reopen (t08_e06, Oct 18) but not a gripper that opens and closes
                in the air (Fahad, Oct 18 late). (b) is stamped at the reopening; one event per attempt.
  drop          an object held at the previous boundary is no longer held and fell relative to the eef
                (object z down minus eef z down > --drop_dz), while the gripper was commanded closed the
                whole chunk (no open command).
  stuck         the eef has not moved more than --move_m between successive boundaries for stuck_n
                boundaries in a row (RESCUE steps-since-progress); stamped when the count reaches stuck_n.
                stuck_n is chosen automatically (--stuck_n 0): the smallest n >= 5 such that at most
                --stuck_max_success (5%) of successful episodes contain a stuck event.
  wrong_object  a held object is not one of the task's objects of interest (LIBERO obj_of_interest).
"held" = object raised more than --lift_dz above its height at step 0 and within --hold_dist of the eef.
Repeated events: missed_grasp and stuck are counted once per run of consecutive boundaries; wrong_object
once per object.
Three onsets per failed episode: onset_any = first event of any kind; onset_strict = first missed grasp,
drop or wrong object (stuck ignored); onset_after_pnr = first event of any kind at or after t_pnr
(only for failures with a t_pnr). A failure with no event gets onset None and is a "silent failure"
(counted separately for each version). Events in successful episodes are "recovered slips".
If scans are given, the intervention window onset - t_pnr (tau 0.5) is added for all three versions.
Summary: results/auto_onset_summary.md (next to --out).

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
p.add_argument("--stop_mm", type=float, default=1.0, help="fingers stopped = width changed less than this (mm) between boundaries")
p.add_argument("--stuck_n", type=int, default=0, help="0 = choose automatically (see --stuck_max_success)")
p.add_argument("--stuck_max_success", type=float, default=0.05)
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
    g = e.robots[0].gripper.important_geoms
    finger_geoms = {e.sim.model.geom_name2id(n) for n in g["left_finger"] + g["right_finger"]}
    m = e.sim.model
    obj_bodies = {b for b in range(m.nbody) if any((m.body_id2name(b) or "").startswith(o + "_") for o in objs)}
    obj_geoms = {i for i in range(m.ngeom) if m.geom_bodyid[i] in obj_bodies}
    fix_bodies = {b for b in range(m.nbody) if any((m.body_id2name(b) or "").startswith(f + "_") for f in e.fixtures_dict)}
    fix_geoms = {i for i in range(m.ngeom) if m.geom_bodyid[i] in fix_bodies}
    steps = ep["query_steps"].astype(int)
    eef, actions = ep["eef"], ep["actions"]

    events = []  # (step, kind, detail); stuck events are added later, once stuck_n is chosen
    stills = []  # (step, boundaries in a row without a move > move_m)
    z0 = None
    prev_held, prev_z = set(), None
    still, in_miss, wrong_seen = 0, False, set()
    grasp_start, grasp_held, grasp_missed, grasp_touched = None, False, False, False  # current grasp attempt (rule b)
    prev_width = None
    for k, s in enumerate(steps):
        env.set_init_state(ep["query_states"][k])
        pos = {o: e.sim.data.body_xpos[e.obj_body_id[o]].copy() for o in objs}
        z = {o: pos[o][2] for o in objs}
        if z0 is None:
            z0 = z
        width = e.sim.data.qpos[finger_addr[0]] - e.sim.data.qpos[finger_addr[1]]
        e.sim.forward()  # contacts are only computed by forward()
        finger_contacts = [{c.geom1, c.geom2} for c in e.sim.data.contact[:e.sim.data.ncon]
                           if {c.geom1, c.geom2} & finger_geoms]
        touching = any(gs & obj_geoms for gs in finger_contacts)
        on_fixture = any(gs & fix_geoms for gs in finger_contacts)
        held = {o for o in objs if z[o] - z0[o] > args.lift_dz and np.linalg.norm(pos[o] - eef[s]) < args.hold_dist}
        prev_cmd = actions[steps[k - 1]:s, -1] if k > 0 else np.zeros(0)
        closed_cmd = len(prev_cmd) > 0 and (prev_cmd > 0).all()

        last_cmd = prev_cmd[-1] if len(prev_cmd) else 0.0
        if grasp_start is None and last_cmd > 0:
            grasp_start, grasp_held, grasp_missed, grasp_touched = int(steps[k - 1]), False, False, False
        miss = closed_cmd and width < args.closed_width and not held
        if miss and not in_miss:
            events.append((int(s), "missed_grasp", f"finger width {width * 1000:.1f} mm"))
            grasp_missed = True  # (a) already fired for this attempt; do not count it again under (b)
        in_miss = miss
        if grasp_start is not None:
            grasp_held = grasp_held or bool(held)
            stopped = (closed_cmd and prev_width is not None and width >= args.closed_width
                       and abs(width - prev_width) * 1000 < args.stop_mm and not on_fixture)
            grasp_touched = grasp_touched or touching or stopped
            if last_cmd < 0:
                if not grasp_held and not grasp_missed and grasp_touched:
                    events.append((int(s), "missed_grasp", f"closed at {grasp_start}, reopened, nothing lifted"))
                grasp_start = None
        for o in prev_held - held:
            fall = (prev_z[o] - z[o]) - (eef[steps[k - 1]][2] - eef[s][2])  # relative to the gripper
            if closed_cmd and fall > args.drop_dz:
                events.append((int(s), "drop", f"{o} fell {fall * 100:.1f} cm below the gripper"))
        for o in held - set(e.obj_of_interest) - wrong_seen:
            events.append((int(s), "wrong_object", o))
            wrong_seen.add(o)
        if k > 0:
            still = still + 1 if np.linalg.norm(eef[s] - eef[steps[k - 1]]) <= args.move_m else 0
        stills.append((int(s), still))
        if args.verbose:
            print(f"  step {s:3d} width {width * 1000:5.1f} mm  cmd {prev_cmd.mean() if len(prev_cmd) else 0:+.2f}  "
                  f"held {sorted(held)}  still {still}")
        prev_held, prev_z, prev_width = held, z, width
    return events, stills


scans = {}
for f in glob.glob(args.scans):
    s = json.load(open(f))
    scans[s["episode_id"]] = s

kinds = ["missed_grasp", "drop", "stuck", "wrong_object"]
strict_kinds = ["missed_grasp", "drop", "wrong_object"]
eps = []
for f in sorted(glob.glob(args.episodes)):
    ep = np.load(f, allow_pickle=True)
    if bool(ep["induced"]):
        continue
    eid = os.path.splitext(os.path.basename(f))[0]
    if args.verbose:
        print(eid, str(ep["description"]))
    events, stills = detect(ep)
    eps.append(dict(eid=eid, task=int(ep["task_id"]), success=bool(ep["success"]), t_end=int(ep["t_end"]),
                    events=events, stills=stills))

# Choose stuck_n: smallest n >= 5 with a stuck event in at most stuck_max_success of successful episodes.
longest = [max(c for _, c in e["stills"]) for e in eps if e["success"]]
stuck_n = args.stuck_n
if stuck_n == 0:
    stuck_n = 5
    while np.mean([L >= stuck_n for L in longest]) > args.stuck_max_success:
        stuck_n += 1
stuck_rate = {n: np.mean([L >= n for L in longest]) for n in range(5, stuck_n + 1)}
for e in eps:
    for s, c in e["stills"]:
        if c == stuck_n:
            e["events"].append((s, "stuck", f"no move > {args.move_m} m for {stuck_n} boundaries"))
    e["events"].sort(key=lambda ev: ev[0])

rows = []
for e in eps:
    scan = scans.get(e["eid"])
    t_pnr = t_pnr_from_scan(scan) if scan and not e["success"] else None
    first_any = e["events"][0] if e["events"] else None
    first_strict = next((ev for ev in e["events"] if ev[1] in strict_kinds), None)
    onset_any = first_any[0] if first_any and not e["success"] else None
    onset_strict = first_strict[0] if first_strict and not e["success"] else None
    first_after = next((ev for ev in e["events"] if t_pnr is not None and ev[0] >= t_pnr), None)
    onset_after = first_after[0] if first_after else None
    row = dict(episode_id=e["eid"], task_id=e["task"], success=int(e["success"]), t_end=e["t_end"],
               **{f"n_{k}": sum(ev[1] == k for ev in e["events"]) for k in kinds},
               onset_any=onset_any, onset_any_event=first_any[1] if onset_any is not None else "",
               onset_strict=onset_strict, onset_strict_event=first_strict[1] if onset_strict is not None else "",
               scanned=int(scan is not None), t_pnr=t_pnr,
               window_any=(onset_any - t_pnr) if onset_any is not None and t_pnr is not None else None,
               window_strict=(onset_strict - t_pnr) if onset_strict is not None and t_pnr is not None else None,
               onset_after_pnr=onset_after, onset_after_pnr_event=first_after[1] if first_after else "",
               window_after_pnr=(onset_after - t_pnr) if onset_after is not None else None,
               events="; ".join(f"{s} {k} ({d})" for s, k, d in e["events"]))
    rows.append(row)
    print(f"{e['eid']} success={e['success']} onset_any={onset_any} onset_strict={onset_strict} t_pnr={t_pnr} | {row['events']}", flush=True)

os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
with open(args.out, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)

fails = [r for r in rows if not r["success"]]
succ = [r for r in rows if r["success"]]
lines = ["# Automatic onset (07_auto_onset.py)", "",
         f"{len(rows)} natural episodes: {len(fails)} failures, {len(succ)} successes.",
         f"stuck_n = {stuck_n} boundaries ({stuck_n * 8} policy steps) without an eef move > {args.move_m} m. "
         "Share of successes with a stuck event per n: " + ", ".join(f"{n}: {v:.3f}" for n, v in stuck_rate.items()) + ".",
         f"Thresholds: fully closed < {args.closed_width * 1000:.0f} mm, lifted > {args.lift_dz * 100:.0f} cm, "
         f"held within {args.hold_dist * 100:.0f} cm, drop > {args.drop_dz * 100:.0f} cm relative to the eef.", "",
         "| version | failures with onset | silent failures (no event) |", "|---|---|---|"]
for v in ["any", "strict"]:
    n_on = sum(r[f"onset_{v}"] is not None for r in fails)
    silent = [r["episode_id"] for r in fails if r[f"onset_{v}"] is None]
    lines.append(f"| onset_{v} | {n_on} of {len(fails)} | {len(silent)}: {', '.join(silent)} |")
lines += ["", "| event | failures with it | first event in failures (onset_any) | successes with it (recovered slips) |",
          "|---|---|---|---|"]
for k in kinds:
    lines.append(f"| {k} | {sum(r[f'n_{k}'] > 0 for r in fails)} | {sum(r['onset_any_event'] == k for r in fails)} | "
                 f"{sum(r[f'n_{k}'] > 0 for r in succ)} |")
lines.append("")
lines.append(f"Successes with at least one event: {sum(any(r[f'n_{k}'] for k in kinds) for r in succ)} of {len(succ)}; "
             f"with a strict event: {sum(any(r[f'n_{k}'] for k in strict_kinds) for r in succ)} of {len(succ)}.")
win = [r for r in fails if r["scanned"]]
if win:
    lines += ["", "Intervention window onset - t_pnr (steps; tau 0.5; t_pnr 0 = doomed from start):", "",
              "| episode | t_pnr | onset_any | window_any | onset_strict | window_strict | onset_after_pnr (event) | window_after_pnr |",
              "|---|---|---|---|---|---|---|---|"]
    for r in win:
        lines.append(f"| {r['episode_id']} | {r['t_pnr']} | {r['onset_any']} | {r['window_any']} | "
                     f"{r['onset_strict']} | {r['window_strict']} | {r['onset_after_pnr']} ({r['onset_after_pnr_event']}) | "
                     f"{r['window_after_pnr']} |")
    timed = [r for r in win if r["t_pnr"] is not None]
    lines += ["", f"Failures with a t_pnr: {len(timed)} of {len(win)} scanned ({sum(r['t_pnr'] == 0 for r in timed)} doomed from start). "
              f"With an event at or after t_pnr: {sum(r['onset_after_pnr'] is not None for r in timed)}. "
              f"Onset before t_pnr (window < 0): onset_any {sum(r['window_any'] is not None and r['window_any'] < 0 for r in timed)}, "
              f"onset_strict {sum(r['window_strict'] is not None and r['window_strict'] < 0 for r in timed)}."]
text = "\n".join(lines) + "\n"
open(os.path.join(os.path.dirname(args.out) or ".", "auto_onset_summary.md"), "w").write(text)
print(text)
