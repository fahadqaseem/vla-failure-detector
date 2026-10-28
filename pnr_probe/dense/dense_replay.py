"""Dense open-loop replay (pnr_probe, Oct 28 2026): restore the initial state of a recorded episode, do the same
reset + 10 no-op steps as the recording, then replay the saved actions in MuJoCo (no policy, CPU, no rendering).

Fidelity (Fahad, Oct 28 2026): a replay counts (passed = True) only if all three hold, else it is left out downstream:
  1. eef drift <= --tol_mm (10 mm) at every saved checkpoint (query k >= 1, step q_k): replayed obs robot0_eef_pos after
     step q_k - 1 (sampled as in the recording) against the recorded eef;
  2. same outcome as the recording (task success reached or not);
  3. goal-object position drift <= --tol_mm at every checkpoint: positions only (mm, no quaternion parts) of the
     placement goal objects of the BDDL goal (the obj1 / obj2 slots of 20_physical_signals.py), replayed against the
     recorded ones (pos columns of the Track 1 physical file, computed from the recorded query_states).

Saved per step t (after env.step of action t), in --out/<eid>.npz:
  qfrc_actuator, qfrc_constraint, qvel, qpos   robot joints (7 arm + 2 finger dofs)
  finger_force (2)     summed contact normal force on the left / right finger pads (N, mj_contactForce)
  contacts             one row per active contact: (step, body1, body2, normal force), body names in body_names
  eef                  replayed eef position
plus passed, pass_eef, pass_outcome, pass_obj, drift_mm and obj_drift_mm per checkpoint, success_replay.

python pnr_probe/dense/dense_replay.py --episodes "$D/natural/task00/*.npz" --out pnr_probe/data/dense
"""

import argparse
import glob
import os

import mujoco
import numpy as np
from libero.libero import benchmark, get_libero_path
from libero.libero.envs.env_wrapper import ControlEnv

p = argparse.ArgumentParser()
p.add_argument("--episodes", nargs="+", required=True)
p.add_argument("--out", required=True)
p.add_argument("--tol_mm", type=float, default=10.0)
p.add_argument("--wait_steps", type=int, default=10)
p.add_argument("--phys", default=os.path.expanduser("~/vla-failure-detector/data/physical"))
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
    if task_id != env_task:
        if env is not None:
            env.close()
        task = suite.get_task(task_id)
        env = ControlEnv(bddl_file_name=os.path.join(get_libero_path("bddl_files"), task.problem_folder, task.bddl_file),
                         has_renderer=False, has_offscreen_renderer=False, use_camera_obs=False)
        env.seed(0)  # as get_libero_env in the recording
        env_task = task_id
    # Same start as pnr.sim.rollout: reset, set the initial state, 10 no-op steps.
    env.reset()
    env.set_init_state(ep["init_state"])
    for _ in range(args.wait_steps):
        obs, _, _, _ = env.step([0, 0, 0, 0, 0, 0, -1])
    e = env.env
    m, d = e.sim.model._model, e.sim.data._data
    robot = e.robots[0]
    dofs = list(robot._ref_joint_vel_indexes) + list(robot._ref_gripper_joint_vel_indexes)
    qps = list(robot._ref_joint_pos_indexes) + list(robot._ref_gripper_joint_pos_indexes)
    pads = [set(e.sim.model.geom_name2id(g) for g in robot.gripper.important_geoms[k]) for k in ("left_fingerpad", "right_fingerpad")]
    body_names = np.array([m.body(i).name for i in range(m.nbody)])
    q = ep["query_steps"].astype(int)
    actions, rec_eef = ep["actions"], ep["eef"]
    T = len(actions)
    qa, qc, qv, qp, ff, eef = (np.zeros((T, 9)), np.zeros((T, 9)), np.zeros((T, 9)), np.zeros((T, 9)), np.zeros((T, 2)),
                               np.zeros((T, 3)))
    contacts, done_at = [], None
    force6 = np.zeros(6)
    goal_objs = [g[1] for g in e.parsed_problem["goal_state"] if len(g) == 3][:2]  # same slots as 20_physical_signals
    rec_pos = np.load(os.path.join(args.phys, eid + ".npz"))["x"][:, [[0 + 12 * i + 2, 12 * i + 3, 12 * i + 4] for i in range(2)]]
    obj_pos, check = {}, set(int(s) for s in q[1:])
    for t in range(T):
        obs, _, done, _ = env.step(actions[t].tolist())
        eef[t] = obs["robot0_eef_pos"]
        qa[t], qc[t], qv[t], qp[t] = d.qfrc_actuator[dofs], d.qfrc_constraint[dofs], d.qvel[dofs], d.qpos[qps]
        for i in range(d.ncon):
            c = d.contact[i]
            mujoco.mj_contactForce(m, d, i, force6)
            b1, b2 = m.geom_bodyid[c.geom1], m.geom_bodyid[c.geom2]
            contacts.append((t, b1, b2, force6[0]))
            for k in range(2):
                if c.geom1 in pads[k] or c.geom2 in pads[k]:
                    ff[t, k] += force6[0]
        if t + 1 in check:  # state at the next checkpoint: goal-object positions
            k = int(np.searchsorted(q, t + 1))
            obj_pos[k] = [np.array(e.object_states_dict[o].get_geom_state()["pos"]) for o in goal_objs]
        if done and done_at is None:
            done_at = t + 1
    ks = [k for k in range(1, len(q)) if q[k] - 1 < T]
    drift = np.array([np.linalg.norm(eef[q[k] - 1] - rec_eef[q[k] - 1]) * 1000 for k in ks])
    obj = np.array([max([np.linalg.norm(obj_pos[k][i] - rec_pos[k, i]) * 1000 for i in range(len(goal_objs))], default=0.0)
                    for k in ks])
    pass_eef = bool(len(drift) == 0 or drift.max() <= args.tol_mm)
    pass_outcome = (done_at is not None) == bool(ep["success"])
    pass_obj = bool(len(obj) == 0 or obj.max() <= args.tol_mm)
    ok = pass_eef and pass_outcome and pass_obj
    np.savez_compressed(out_path, qfrc_actuator=qa.astype(np.float32), qfrc_constraint=qc.astype(np.float32),
                        qvel=qv.astype(np.float32), qpos=qp.astype(np.float32), finger_force=ff.astype(np.float32), eef=eef.astype(np.float32),
                        contacts=np.array(contacts, np.float32).reshape(-1, 4), body_names=body_names,
                        query_steps=q, drift_mm=drift, obj_drift_mm=obj, max_drift_mm=drift.max() if len(drift) else 0.0,
                        passed=ok, pass_eef=pass_eef, pass_outcome=pass_outcome, pass_obj=pass_obj, success_replay=done_at is not None, success=bool(ep["success"]), tol_mm=args.tol_mm)
    print(f"{n + 1}/{len(files)} {eid}: pass {ok} (eef {pass_eef}, outcome {pass_outcome}, objects {pass_obj}), max eef "
          f"drift {drift.max() if len(drift) else 0:.2f} mm, max goal-object drift {obj.max() if len(obj) else 0:.2f} mm, "
          f"success rec {bool(ep['success'])} replay {done_at is not None}", flush=True)
print(f"done: {len(files)} episodes -> {args.out}")
