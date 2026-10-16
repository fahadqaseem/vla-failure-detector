"""Videos of recorded episodes for labelling t_onset by eye. No policy needed: replays the recorded actions
from the initial state (same reset + 10 wait steps as the original run) and draws the policy step on each frame.

python scripts/05_make_videos.py --episodes "data/rollouts/*.npz" --failed_only
Frame k shows the scene after k policy steps (k = 0 is the start, after the wait steps).
Episodes recorded one after another in the same env depend on how many env.reset() calls came before
(each reset draws from the env's random stream, and the start of an episode depends on it). So the script
tries 0, 1, 2, ... extra resets first and keeps the first one where the replayed hand matches the recorded
one (max drift under --tol_mm). Episodes that never match are skipped, not written.
"""

import argparse
import glob
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import cv2  # noqa: E402
import imageio  # noqa: E402
import numpy as np  # noqa: E402

from pnr.sim import MODEL_FAMILY, WAIT_STEPS, make_task  # noqa: E402
from experiments.robot.libero.libero_utils import get_libero_dummy_action  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--episodes", default="data/rollouts/*.npz")
p.add_argument("--failed_only", action="store_true")
p.add_argument("--fps", type=int, default=20, help="20 = real time (LIBERO control rate is 20 Hz)")
p.add_argument("--out", default="results/videos")
p.add_argument("--tol_mm", type=float, default=0.1, help="max allowed drift from the recorded hand position")
args = p.parse_args()
os.makedirs(args.out, exist_ok=True)


def frame(obs, step, t_end, text):
    """Front camera and wrist camera side by side (upright), 2x size, with the step number drawn on."""
    img = np.concatenate([obs["agentview_image"][::-1, ::-1], obs["robot0_eye_in_hand_image"][::-1, ::-1]], axis=1)
    img = cv2.resize(np.ascontiguousarray(img), None, fx=2, fy=2, interpolation=cv2.INTER_NEAREST)
    img = np.concatenate([img, np.zeros((44, img.shape[1], 3), dtype=np.uint8)], axis=0)  # caption strip
    cv2.putText(img, f"step {step:3d} / {t_end}", (10, 34), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 0), 2)
    cv2.putText(img, text, (10, img.shape[0] - 14), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
    return img


def replay(env, ep, n_prior, label=None):
    """Replay the recorded actions after n_prior extra resets. Returns (max drift in mm, frames or None)."""
    for _ in range(n_prior):
        env.reset()
    env.reset()
    obs = env.set_init_state(ep["init_state"])
    for _ in range(WAIT_STEPS):
        obs, _, _, _ = env.step(get_libero_dummy_action(MODEL_FAMILY))
    t_end = int(ep["t_end"])
    frames = [frame(obs, 0, t_end, label)] if label else None
    dev = 0.0
    for k, action in enumerate(ep["actions"]):
        obs, _, _, _ = env.step(action.tolist())
        dev = max(dev, float(np.linalg.norm(obs["robot0_eef_pos"] - ep["eef"][k])) * 1000)
        if label:
            frames.append(frame(obs, k + 1, t_end, label))
    return dev, frames


for f in sorted(glob.glob(args.episodes)):
    ep = np.load(f, allow_pickle=True)
    if args.failed_only and bool(ep["success"]):
        continue
    eid = os.path.splitext(os.path.basename(f))[0]
    label = f"{eid} ({'induced' if bool(ep['induced']) else 'natural'}, {'success' if bool(ep['success']) else 'failure'}): "
    match = None
    for n_prior in range(int(ep["episode_idx"]) + 1):  # an episode can have at most episode_idx episodes before it
        env, desc, _ = make_task(int(ep["task_id"]))      # fresh env = fresh random stream
        dev, _ = replay(env, ep, n_prior)
        env.close()
        if dev <= args.tol_mm:
            match = n_prior
            break
    if match is None:
        print(f"{eid}: SKIPPED, replay never matched the recording (last max drift {dev:.3f} mm)", flush=True)
        continue
    env, desc, _ = make_task(int(ep["task_id"]))
    dev, frames = replay(env, ep, match, label + desc)
    env.close()
    path = os.path.join(args.out, eid + ".mp4")
    imageio.mimsave(path, frames, fps=args.fps)
    print(f"{eid}: {len(frames)} frames -> {path} | extra resets {match} | replay vs recorded eef: max {dev:.3f} mm", flush=True)
