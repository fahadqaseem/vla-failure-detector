"""Robot state per query from the saved sim states (CPU, no rendering), for the real-world ablation (Oct 30): eef position (3), eef
rotation (first two columns of the rotation matrix, 6, continuous unlike a quaternion), gripper opening (1). Same loading as
20_physical_signals.py. One file per episode in --out: x (n_queries, 10).

python scripts/33_robot_state.py --phys data/physical --out data/robot_state
"""

import argparse
import glob
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from libero.libero import benchmark, get_libero_path  # noqa: E402
from libero.libero.envs.env_wrapper import ControlEnv  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--phys", default="data/physical")
p.add_argument("--out", default="data/robot_state")
args = p.parse_args()

wanted = {os.path.splitext(os.path.basename(f))[0] for f in glob.glob(os.path.join(args.phys, "*.npz"))}
pats = ["data/natural/*/*.npz", "data/perturbed/*/*.npz", "data/perturbed_v2/*/*.npz"]
files = sorted((f for pat in pats for f in glob.glob(pat) if os.path.splitext(os.path.basename(f))[0] in wanted),
               key=lambda f: os.path.basename(f))
suite = benchmark.get_benchmark_dict()["libero_10"]()
os.makedirs(args.out, exist_ok=True)
env, env_task = None, None
for n, f in enumerate(files):
    eid = os.path.splitext(os.path.basename(f))[0]
    path = os.path.join(args.out, eid + ".npz")
    if os.path.exists(path):
        continue
    ep = np.load(f, allow_pickle=True)
    task_id = int(ep["task_id"])
    if task_id != env_task:
        if env is not None:
            env.close()
        task = suite.get_task(task_id)
        env = ControlEnv(bddl_file_name=os.path.join(get_libero_path("bddl_files"), task.problem_folder, task.bddl_file),
                         has_renderer=False, has_offscreen_renderer=False, use_camera_obs=False)
        env.reset()
        env_task = task_id
    e = env.env
    robot = e.robots[0]
    rows = []
    for state in ep["query_states"]:
        env.set_init_state(state)
        mat = e.sim.data.site_xmat[robot.eef_site_id].reshape(3, 3)
        fingers = e.sim.data.qpos[robot._ref_gripper_joint_pos_indexes]
        rows.append(np.r_[e.sim.data.site_xpos[robot.eef_site_id], mat[:, 0], mat[:, 1], abs(fingers[0] - fingers[1])])
    np.savez(path, x=np.stack(rows).astype(np.float32))
    if n % 100 == 0:
        print(f"{n + 1}/{len(files)} {eid}", flush=True)
print("done", len(files))
