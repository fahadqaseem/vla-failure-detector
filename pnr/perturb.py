"""Perturbed initial states for extra natural failures (rule in CLAUDE.md, Fahad Oct 18 2026).

Start from one of the 50 fixed LIBERO initial states and move every movable object (env.objects_dict; all
have a free joint in LIBERO-10, fixtures such as the stove or cabinet are not moved):
  shift in x, y by a random distance of 2 to 3 cm in a random direction, and
  rotate about the vertical axis by a random angle of up to 15 degrees.
The draw is seeded (seed, task, init index, attempt). LIBERO initial states hold objects a few cm above
the table (they fall during the 10 no-op settling steps) and some start slightly overlapping, so validity
is judged against the UNPERTURBED initial state after the same 10 settling steps. A start is invalid, and
a new attempt is drawn, if after settling
  1. some object is more than 1 cm (in x, y or z) away from where it settles in the unperturbed start
     plus its own shift (it was pushed by an overlap, toppled, fell off something or landed on another), or
  2. some object's up axis differs by more than 10 degrees from the unperturbed settled one, or
  3. the task is already solved.
After 20 invalid attempts the initial state is skipped.
"""

import numpy as np

from pnr.sim import MODEL_FAMILY, WAIT_STEPS, get_libero_dummy_action

SHIFT_M = (0.02, 0.03)
MAX_YAW_DEG = 15.0
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
    """Position and the world vertical seen in the object's own frame (third row of its rotation matrix) for
    every movable object. A rotation about the world vertical does not change that vector, a tilt does
    (the object's own z axis is not always vertical, so its z axis itself would move with the yaw)."""
    out = {}
    for name in e.objects_dict:
        b = e.obj_body_id[name]
        out[name] = (e.sim.data.body_xpos[b].copy(), e.sim.data.body_xmat[b].reshape(3, 3)[2, :].copy())
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


def settle(env, state):
    """Same reset + set_init_state + 10 no-op steps as a real episode. Returns object poses after it."""
    env.reset()
    env.set_init_state(state)
    for _ in range(WAIT_STEPS):
        env.step(get_libero_dummy_action(MODEL_FAMILY))
    return _poses(env.env)


def check_valid(env, state, info, base):
    """Returns (ok, reason). base = settle(env, unperturbed initial state); info from perturb()."""
    after = settle(env, state)
    for name, (dx, dy, _) in info.items():
        expected = base[name][0] + np.array([dx, dy, 0.0])
        off = np.abs(after[name][0] - expected).max()
        tilt = np.rad2deg(np.arccos(np.clip(base[name][1] @ after[name][1], -1, 1)))
        if off > MAX_SETTLE_MOVE_M or tilt > MAX_SETTLE_TILT_DEG:
            return False, f"{name} {off * 100:.1f} cm off, tilted {tilt:.0f} deg after settling"
    if env.env._check_success():
        return False, "task already solved"
    return True, "ok"


def perturbed_start(env, init_state, seed, task_id, init_idx):
    """First valid perturbed start, or None. Returns (state, info, attempt, rejected reasons)."""
    base = settle(env, init_state)
    rejected = []
    for attempt in range(MAX_ATTEMPTS):
        rng = np.random.default_rng([seed, task_id, init_idx, attempt])
        state, info = perturb(env, init_state, rng)
        ok, reason = check_valid(env, state, info, base)
        if ok:
            return state, info, attempt, rejected
        rejected.append(reason)
    return None, None, None, rejected
