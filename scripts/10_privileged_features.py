"""Privileged inputs for a diagnostic predictor (Fahad, Oct 19 2026): simulator poses instead of VLA features.

For every query of every episode, from the saved sim state (CPU, no policy, no rendering), 25 numbers:
  gripper: eef position (3), finger joint positions (2), gripper command counter (2)
  2 placement slots, one per two-argument goal predicate (in / on) in the order of the BDDL goal:
      object minus target position (3), object minus eef position (3), predicate true now (1), slot used (1)
  1 articulation slot, for a one-argument goal predicate (turnon / close): true now (1), slot used (1)
Targets are objects (plate_1) or regions (basket_1_contain_region); both have a position in LIBERO's
object_states_dict. Unused slots are zero. Never the step index.
One file per episode in --out: x (n_queries, 25), query_steps.

python scripts/10_privileged_features.py --episodes "data/natural/*/*.npz" --out data/privileged
"""

import argparse
import glob
import os

import numpy as np
from libero.libero import benchmark, get_libero_path
from libero.libero.envs.env_wrapper import ControlEnv

p = argparse.ArgumentParser()
p.add_argument("--episodes", nargs="+", default=["data/natural/*/*.npz"])
p.add_argument("--out", default="data/privileged")
args = p.parse_args()

suite = benchmark.get_benchmark_dict()["libero_10"]()
os.makedirs(args.out, exist_ok=True)
env, env_task = None, None
files = sorted(f for pat in args.episodes for f in glob.glob(pat))
for n, f in enumerate(files):
    eid = os.path.splitext(os.path.basename(f))[0]
    out_path = os.path.join(args.out, eid + ".npz")
    if os.path.exists(out_path):
        continue
    ep = np.load(f, allow_pickle=True)
    task_id = int(ep["task_id"])
    if task_id != env_task:  # one env open at a time (files come sorted by task)
        if env is not None:
            env.close()
        task = suite.get_task(task_id)
        env = ControlEnv(bddl_file_name=os.path.join(get_libero_path("bddl_files"), task.problem_folder, task.bddl_file),
                         has_renderer=False, has_offscreen_renderer=False, use_camera_obs=False)
        env.reset()
        env_task = task_id
    e = env.env
    goal = e.parsed_problem["goal_state"]
    placements = [g for g in goal if len(g) == 3][:2]
    unary = [g for g in goal if len(g) == 2][:1]
    robot = e.robots[0]
    rows = []
    for k, state in enumerate(ep["query_states"]):
        env.set_init_state(state)
        eef = e.sim.data.site_xpos[robot.eef_site_id].copy()
        fingers = e.sim.data.qpos[robot._ref_gripper_joint_pos_indexes].copy()
        x = [eef, fingers, ep["query_grippers"][k]]
        for slot in range(2):
            if slot < len(placements):
                _, obj, target = placements[slot]
                po = e.object_states_dict[obj].get_geom_state()["pos"]
                pt = e.object_states_dict[target].get_geom_state()["pos"]
                x += [po - pt, po - eef, [float(e._eval_predicate(placements[slot])), 1.0]]
            else:
                x += [np.zeros(3), np.zeros(3), [0.0, 0.0]]
        x += [[float(e._eval_predicate(unary[0])), 1.0] if unary else [0.0, 0.0]]
        rows.append(np.concatenate([np.asarray(v, dtype=np.float64).ravel() for v in x]))
    np.savez(out_path, x=np.stack(rows).astype(np.float32), query_steps=ep["query_steps"])
    if n % 50 == 0:
        print(f"{n + 1}/{len(files)} {eid}: goal {goal}, {len(rows)} queries", flush=True)
print(f"done: {len(files)} episodes -> {args.out}")
