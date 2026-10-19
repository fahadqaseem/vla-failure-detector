"""Perturbed initial states for extra natural failures (rule in CLAUDE.md, Fahad Oct 18 2026).

Start from one of the 50 fixed LIBERO initial states and move every movable object (env.objects_dict; all
have a free joint in LIBERO-10, fixtures such as the stove or cabinet are not moved):
  shift in x, y by a random distance of 2 to 3 cm in a random direction, and
  rotate about the vertical axis by a random angle of up to 15 degrees.
The draw is seeded (seed, task, init index, attempt). A start is invalid, and a new attempt is drawn, if
  1. two bodies overlap by more than 5 mm right after the move (penetration),
  2. during the 10 settling no-op steps of the eval any object moves more than 1 cm or tilts more than
     10 degrees (it fell, toppled or was pushed), or
  3. the task is already solved after settling.
After 20 invalid attempts the initial state is skipped.
"""

import numpy as np

from pnr.sim import MODEL_FAMILY, WAIT_STEPS, get_libero_dummy_action

SHIFT_M = (0.02, 0.03)
MAX_YAW_DEG = 15.0
MAX_PENETRATION_M = 0.005
MAX_SETTLE_MOVE_M = 0.01
MAX_SETTLE_TILT_DEG = 10.0
MAX_ATTEMPTS = 20


def _yaw_quat(angle):  # MuJoCo quaternions are (w, x, y, z)
    return np.array([np.cos(angle / 2), 0.0, 0.0, np.sin(angle / 2)])


def _quat_mul(a, b):
    w1, x1, y1, z1 = a
    w2, x2, y2, z2 = b
    return np.array([w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2, w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
                     w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2, w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2])


def _poses(e):
    """Position and up axis (third column of the rotation matrix) of every movable object."""
    out = {}
    for name in e.objects_dict:
        b = e.obj_body_id[name]
        out[name] = (e.sim.data.body_xpos[b].copy(), e.sim.data.body_xmat[b].reshape(3, 3)[:, 2].copy())
    return out


def perturb(env, init_state, rng):
    """Returns (perturbed flat sim state, {object: [dx, dy, yaw_deg]}). Does not check validity."""
    env.reset()
    env.set_init_state(init_state)
    e = env.env
    info = {}
    for name, obj in e.objects_dict.items():
        a, b = e.sim.model.get_joint_qpos_addr(obj.joints[0])  # free joint: x y z qw qx qy qz
        q = e.sim.data.qpos[a:b].copy()
        direction = rng.uniform(0, 2 * np.pi)
        dist = rng.uniform(*SHIFT_M)
        yaw = np.deg2rad(rng.uniform(-MAX_YAW_DEG, MAX_YAW_DEG))
        q[0] += dist * np.cos(direction)
        q[1] += dist * np.sin(direction)
        q[3:7] = _quat_mul(_yaw_quat(yaw), q[3:7])
        e.sim.data.qpos[a:b] = q
        info[name] = [round(float(dist * np.cos(direction)), 4), round(float(dist * np.sin(direction)), 4),
                      round(float(np.rad2deg(yaw)), 2)]
    e.sim.forward()
    return env.get_sim_state().copy(), info


def check_valid(env, state):
    """Returns (ok, reason). Runs the same reset + set_init_state + 10 no-op steps as a real episode."""
    env.reset()
    env.set_init_state(state)
    e = env.env
    for i in range(e.sim.data.ncon):
        c = e.sim.data.contact[i]
        if c.dist < -MAX_PENETRATION_M:
            g1, g2 = e.sim.model.geom_id2name(c.geom1), e.sim.model.geom_id2name(c.geom2)
            return False, f"overlap {-c.dist * 1000:.1f} mm ({g1}, {g2})"
    before = _poses(e)
    for _ in range(WAIT_STEPS):
        env.step(get_libero_dummy_action(MODEL_FAMILY))
    after = _poses(e)
    for name in before:
        move = np.linalg.norm(after[name][0] - before[name][0])
        tilt = np.rad2deg(np.arccos(np.clip(before[name][1] @ after[name][1], -1, 1)))
        if move > MAX_SETTLE_MOVE_M or tilt > MAX_SETTLE_TILT_DEG:
            return False, f"{name} moved {move * 100:.1f} cm, tilted {tilt:.0f} deg while settling"
    if e._check_success():
        return False, "task already solved"
    return True, "ok"


def perturbed_start(env, init_state, seed, task_id, init_idx):
    """First valid perturbed start, or None. Returns (state, info, attempt, rejected reasons)."""
    rejected = []
    for attempt in range(MAX_ATTEMPTS):
        rng = np.random.default_rng([seed, task_id, init_idx, attempt])
        state, info = perturb(env, init_state, rng)
        ok, reason = check_valid(env, state)
        if ok:
            return state, info, attempt, rejected
        rejected.append(reason)
    return None, None, None, rejected
