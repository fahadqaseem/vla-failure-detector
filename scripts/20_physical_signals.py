"""Physical state signals per query (Track 1, Prof. Zhu meeting Oct 23 2026), from the saved sim states (CPU, no
policy, no rendering). Same loading as 10_privileged_features.py.

Objects = the goal objects of the task (BDDL goal): up to 2 placement slots (In / On: object and its goal region or
target) and 1 articulation slot (Turnon / Close / Open: the fixture). Distractors are left out, so every task has the
same 33 numbers. Per placement slot (12):
  dist      gripper (eef site) to object distance (m)          ddist   its change since the previous query
  pos       object position (3)                                 dz      height above its position at the first query
  lifted    dz > 0.02 m                                         tilt    angle (rad) between the object's up axis now
                                                                         and at the first query
  contact   gripper touches the object (robosuite check_contact) goal_dist  object to goal region / target distance
  in_goal   the goal predicate is true now                      used    slot used by this task
Articulation slot (5): dist, ddist, contact, predicate true, used. Gripper (4): opening (finger distance) and eef position.
Never the step index. One file per episode in --out: x (n_queries, 33), names, query_steps.

python scripts/20_physical_signals.py --episodes "data/natural/*/*.npz" "data/perturbed/task0[0145678]/*.npz" --out data/physical
"""

import argparse
import glob
import os

import numpy as np
from libero.libero import benchmark, get_libero_path
from libero.libero.envs.env_wrapper import ControlEnv

p = argparse.ArgumentParser()
p.add_argument("--episodes", nargs="+", default=["data/natural/*/*.npz"])
p.add_argument("--out", default="data/physical")
p.add_argument("--lift_m", type=float, default=0.02)
args = p.parse_args()

SLOT = ["dist", "ddist", "pos_x", "pos_y", "pos_z", "dz", "lifted", "tilt", "contact", "goal_dist", "in_goal", "used"]
NAMES = ([f"obj{i}_{n}" for i in (1, 2) for n in SLOT] + [f"art_{n}" for n in ["dist", "ddist", "contact", "true", "used"]]
         + ["grip_open", "eef_x", "eef_y", "eef_z"])


def up_axis(quat_wxyz):
    """Third column of the rotation matrix of a MuJoCo (w, x, y, z) quaternion: the object's up axis in the world."""
    w, x, y, z = quat_wxyz
    return np.array([2 * (x * z + w * y), 2 * (y * z - w * x), 1 - 2 * (x * x + y * y)])


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
    rows, start, prev = [], {}, {}
    for k, state in enumerate(ep["query_states"]):
        env.set_init_state(state)
        eef = e.sim.data.site_xpos[robot.eef_site_id].copy()
        fingers = e.sim.data.qpos[robot._ref_gripper_joint_pos_indexes].copy()
        x = []
        for slot in range(2):
            if slot >= len(placements):
                x += [0.0] * len(SLOT)
                continue
            _, obj, target = placements[slot]
            gs = e.object_states_dict[obj].get_geom_state()
            pos, up = np.array(gs["pos"]), up_axis(gs["quat"])
            start.setdefault(obj, (pos, up))
            dist = float(np.linalg.norm(pos - eef))
            dz = float(pos[2] - start[obj][0][2])
            tilt = float(np.arccos(np.clip(up @ start[obj][1], -1, 1)))
            goal_dist = float(np.linalg.norm(pos - np.array(e.object_states_dict[target].get_geom_state()["pos"])))
            x += [dist, dist - prev.get(obj, dist), *pos, dz, float(dz > args.lift_m), tilt,
                  float(e.check_contact(robot.gripper, e.get_object(obj))), goal_dist,
                  float(e._eval_predicate(placements[slot])), 1.0]
            prev[obj] = dist
        if unary:
            obj = unary[0][1]
            pos = np.array(e.object_states_dict[obj].get_geom_state()["pos"])
            dist = float(np.linalg.norm(pos - eef))
            x += [dist, dist - prev.get(obj, dist), float(e.check_contact(robot.gripper, e.get_object(obj))),
                  float(e._eval_predicate(unary[0])), 1.0]
            prev[obj] = dist
        else:
            x += [0.0] * 5
        x += [float(abs(fingers[0] - fingers[1])), *eef]
        rows.append(np.array(x, dtype=np.float32))
    np.savez(out_path, x=np.stack(rows), names=np.array(NAMES), query_steps=ep["query_steps"])
    if n % 50 == 0:
        print(f"{n + 1}/{len(files)} {eid}: goal {goal}, {len(rows)} queries", flush=True)
print(f"done: {len(files)} episodes -> {args.out}")
