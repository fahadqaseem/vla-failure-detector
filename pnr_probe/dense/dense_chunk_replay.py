"""Dense per-chunk replay (pnr_probe, Oct 28 2026; replaces the open-loop replay from step 0, whose pass rate was biased:
timed failures 67% vs successes 95%). For every checkpoint k of a recorded episode: restore the saved state with
pnr.sim.restore_query (the method the scans use: restore query k - 1, replay its 8 actions, put the exact saved state at
q_k back; query 0 = reset + 10 no-op steps), then replay only the next recorded chunk (steps q_k .. q_{k+1} - 1) open
loop in MuJoCo (no policy, CPU, no rendering). The env is a ControlEnv without cameras (physics as in the recording).

Fidelity (same 3 rules as dense_replay.py, checked at the END of each chunk; the episode passes if every chunk does):
  1. eef drift <= --tol_mm (10 mm): replayed obs robot0_eef_pos after the chunk's last step against the recorded eef;
  2. same outcome: the task is reached inside the chunk exactly when the recording ended there with success;
  3. goal-object position drift <= --tol_mm (positions only, mm): against the Track 1 physical file at query k + 1
     (computed from the recorded query_states). Not checked for the last chunk (no saved state after it).

Saved per step (same fields as dense_replay.py, so dense_features.py reads both): qfrc_actuator, qfrc_constraint, qvel,
qpos (robot dofs), finger_force (pad normal force), contacts (step, body1, body2, normal force), eef; plus passed,
pass_eef, pass_outcome, pass_obj, drift_mm and obj_drift_mm per chunk end, chunk_pass.

python pnr_probe/dense/dense_chunk_replay.py --episodes "$D/natural/task00/*.npz" --out pnr_probe/data/dense_chunk
"""

import argparse
import glob
import os
import sys

import mujoco
import numpy as np
from libero.libero import benchmark, get_libero_path
from libero.libero.envs.env_wrapper import ControlEnv

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from pnr.sim import restore_query  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--episodes", nargs="+", required=True)
p.add_argument("--out", required=True)
p.add_argument("--tol_mm", type=float, default=10.0)
p.add_argument("--phys", default=os.path.expanduser("~/vla-failure-detector/data/physical"))
args = p.parse_args()

suite = benchmark.get_benchmark_dict()["libero_10"]()
os.makedirs(args.out, exist_ok=True)
env, env_task = None, None
force6 = np.zeros(6)
files = sorted(f for pat in args.episodes for f in glob.glob(pat))
for n, f in enumerate(files):
    eid = os.path.splitext(os.path.basename(f))[0]
    out_path = os.path.join(args.out, eid + ".npz")
    if os.path.exists(out_path):
        continue
    ep = dict(np.load(f, allow_pickle=True))
    task_id = int(ep["task_id"])
    if task_id != env_task:
        if env is not None:
            env.close()
        task = suite.get_task(task_id)
        env = ControlEnv(bddl_file_name=os.path.join(get_libero_path("bddl_files"), task.problem_folder, task.bddl_file),
                         has_renderer=False, has_offscreen_renderer=False, use_camera_obs=False)
        env.seed(0)  # as get_libero_env in the recording
        env_task = task_id
    q = ep["query_steps"].astype(int)
    actions, rec_eef = ep["actions"], ep["eef"]
    T = len(actions)
    rec_pos = np.load(os.path.join(args.phys, eid + ".npz"))["x"][:, [[12 * i + 2, 12 * i + 3, 12 * i + 4] for i in range(2)]]
    qa, qc, qv, qp, ff, eef = (np.zeros((T, 9)), np.zeros((T, 9)), np.zeros((T, 9)), np.zeros((T, 9)), np.zeros((T, 2)),
                               np.zeros((T, 3)))
    contacts, drift, obj, outcome_ok = [], [], [], []
    for k in range(len(q)):
        start, end = q[k], (q[k + 1] if k + 1 < len(q) else T)
        if start >= end:
            continue
        restore_query(env, ep, k)  # env.reset() inside rebuilds the sim: look everything up afterwards
        e = env.env
        m, d = e.sim.model._model, e.sim.data._data
        robot = e.robots[0]
        dofs = list(robot._ref_joint_vel_indexes) + list(robot._ref_gripper_joint_vel_indexes)
        qps = list(robot._ref_joint_pos_indexes) + list(robot._ref_gripper_joint_pos_indexes)
        pads = [set(e.sim.model.geom_name2id(g) for g in robot.gripper.important_geoms[s]) for s in ("left_fingerpad", "right_fingerpad")]
        goal_objs = [g[1] for g in e.parsed_problem["goal_state"] if len(g) == 3][:2]  # slots of 20_physical_signals
        done_in_chunk = False
        for t in range(start, end):
            obs, _, done, _ = env.step(actions[t].tolist())
            done_in_chunk |= bool(done)
            eef[t] = obs["robot0_eef_pos"]
            qa[t], qc[t], qv[t], qp[t] = d.qfrc_actuator[dofs], d.qfrc_constraint[dofs], d.qvel[dofs], d.qpos[qps]
            for i in range(d.ncon):
                c = d.contact[i]
                mujoco.mj_contactForce(m, d, i, force6)
                contacts.append((t, m.geom_bodyid[c.geom1], m.geom_bodyid[c.geom2], force6[0]))
                for s in range(2):
                    if c.geom1 in pads[s] or c.geom2 in pads[s]:
                        ff[t, s] += force6[0]
        drift.append(np.linalg.norm(eef[end - 1] - rec_eef[end - 1]) * 1000)
        if k + 1 < len(q):
            pos = [np.array(e.object_states_dict[o].get_geom_state()["pos"]) for o in goal_objs]
            obj.append(max([np.linalg.norm(pos[i] - rec_pos[k + 1, i]) * 1000 for i in range(len(goal_objs))], default=0.0))
        else:
            obj.append(np.nan)
        outcome_ok.append(done_in_chunk == (bool(ep["success"]) and end == T))
    body_names = np.array([m.body(i).name for i in range(m.nbody)])
    drift, obj, outcome_ok = np.array(drift), np.array(obj), np.array(outcome_ok)
    chunk_eef, chunk_obj = drift <= args.tol_mm, ~(obj > args.tol_mm)  # NaN (last chunk) counts as ok
    chunk_pass = chunk_eef & chunk_obj & outcome_ok
    pass_eef, pass_obj, pass_outcome = bool(chunk_eef.all()), bool(chunk_obj.all()), bool(outcome_ok.all())
    ok = bool(chunk_pass.all())
    np.savez_compressed(out_path, qfrc_actuator=qa.astype(np.float32), qfrc_constraint=qc.astype(np.float32),
                        qvel=qv.astype(np.float32), qpos=qp.astype(np.float32), finger_force=ff.astype(np.float32),
                        eef=eef.astype(np.float32), contacts=np.array(contacts, np.float32).reshape(-1, 4), body_names=body_names,
                        query_steps=q, drift_mm=drift, obj_drift_mm=obj, max_drift_mm=drift.max() if len(drift) else 0.0,
                        chunk_pass=chunk_pass, passed=ok, pass_eef=pass_eef, pass_outcome=pass_outcome, pass_obj=pass_obj,
                        success=bool(ep["success"]), tol_mm=args.tol_mm, method="chunk restore_query")
    print(f"{n + 1}/{len(files)} {eid}: pass {ok} (eef {pass_eef}, outcome {pass_outcome}, objects {pass_obj}), chunks "
          f"passed {int(chunk_pass.sum())}/{len(chunk_pass)}, max eef drift {drift.max() if len(drift) else 0:.3f} mm, "
          f"max goal-object drift {np.nanmax(obj) if np.isfinite(obj).any() else 0:.3f} mm", flush=True)
print(f"done: {len(files)} episodes -> {args.out}")
