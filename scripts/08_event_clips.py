"""Short clips around the automatic onset events, to check them by eye (needs EGL rendering, so a GPU node).

For each event in results/auto_onset.csv, the window is --half steps before and after it (100 = 5 s each
side at 20 Hz). Overlapping windows of one episode are merged. Each window starts from the saved sim state
at the chunk boundary just before it (pnr.sim.restore) and replays the recorded actions, so no policy is
needed. The caption names the events; drift between replayed and recorded eef is printed as a check.
An episode with no event (silent failure) gets the whole episode, sped up to about 10 s.

python scripts/08_event_clips.py --ids t02_e10_n0 t00_e14_n0 t08_e06_n0 --out results/clips
"""

import argparse
import csv
import glob
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import cv2  # noqa: E402
import imageio  # noqa: E402
import numpy as np  # noqa: E402

from pnr.sim import CHUNK, make_task, restore  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--ids", nargs="+", required=True)
p.add_argument("--onsets", default="results/auto_onset.csv")
p.add_argument("--root", default="data/natural")
p.add_argument("--half", type=int, default=100, help="steps before and after each event")
p.add_argument("--fps", type=int, default=20, help="20 = real time")
p.add_argument("--out", default="results/clips")
args = p.parse_args()
os.makedirs(args.out, exist_ok=True)
rows = {r["episode_id"]: r for r in csv.DictReader(open(args.onsets))}


def frame(obs, step, top, bottom):
    """Front and wrist cameras side by side (upright), 2x size, step and event text drawn on."""
    img = np.concatenate([obs["agentview_image"][::-1, ::-1], obs["robot0_eye_in_hand_image"][::-1, ::-1]], axis=1)
    img = cv2.resize(np.ascontiguousarray(img), None, fx=2, fy=2, interpolation=cv2.INTER_NEAREST)
    img = np.concatenate([img, np.zeros((44, img.shape[1], 3), dtype=np.uint8)], axis=0)
    cv2.putText(img, f"step {step:3d}  {top}", (10, 34), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 0), 2)
    cv2.putText(img, bottom, (10, img.shape[0] - 14), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
    return img


for eid in args.ids:
    ep = np.load(glob.glob(os.path.join(args.root, "*", eid + ".npz"))[0], allow_pickle=True)
    row = rows[eid]
    events = [(int(e.split(" ", 1)[0]), e.split(" ", 2)[1]) for e in row["events"].split("; ") if e]
    t_end, steps = int(ep["t_end"]), [int(s) for s in ep["query_steps"]]
    if events:
        windows = []
        for s, _ in events:
            a, b = max(0, s - args.half) // CHUNK * CHUNK, min(t_end, s + args.half)
            if windows and a <= windows[-1][1]:
                windows[-1][1] = max(windows[-1][1], b)
            else:
                windows.append([a, b])
        fps, every = args.fps, 1
    else:
        windows, every = [[0, t_end]], max(1, round(t_end / (10 * args.fps)))  # silent: whole run, about 10 s
        fps = args.fps
    env, desc, _ = make_task(int(ep["task_id"]))
    frames, drift = [], 0.0
    for a, b in windows:
        k = steps.index(a)
        obs = restore(env, ep["query_states"][k], ep["query_grippers"][k])
        for t in range(a, b):
            now = [kind for s, kind in events if abs(s - t) <= 8]
            if (t - a) % every == 0:
                frames.append(frame(obs, t, " + ".join(now).upper(), f"{eid}: {desc} | events: "
                                    + (", ".join(f"{s} {kind}" for s, kind in events) or "none (silent failure)")))
            obs, _, _, _ = env.step(ep["actions"][t].tolist())
            drift = max(drift, float(np.linalg.norm(obs["robot0_eef_pos"] - ep["eef"][t])) * 1000)
    env.close()
    path = os.path.join(args.out, eid + ".mp4")
    imageio.mimsave(path, frames, fps=fps)
    print(f"{eid}: windows {windows}, {len(frames)} frames ({len(frames) / fps:.1f} s{', 1 of every %d steps' % every if every > 1 else ''}), "
          f"replay vs recorded eef max {drift:.2f} mm -> {path}", flush=True)
