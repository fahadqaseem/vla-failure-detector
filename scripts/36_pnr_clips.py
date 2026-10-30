"""Clips around t_pnr for the ids in clip_ids.txt (needs EGL rendering, so a GPU node). Replays the recorded actions from the query
--half steps before t_pnr (pnr.sim.restore_query), no policy, front and wrist cameras. The caption turns red at and after t_pnr.

python scripts/36_pnr_clips.py --ids results/week3/patterns/clip_ids.txt --out results/week3/patterns/clips
"""

import argparse
import glob
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import cv2  # noqa: E402
import imageio  # noqa: E402
import numpy as np  # noqa: E402

from pnr.sim import CHUNK, make_task, restore_query  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--ids", default="results/week3/patterns/clip_ids.txt")
p.add_argument("--half", type=int, default=64)
p.add_argument("--out", default="results/week3/patterns/clips")
args = p.parse_args()
os.makedirs(args.out, exist_ok=True)
for line in open(args.ids):
    eid, t_pnr, kind = line.split()
    t_pnr = int(t_pnr)
    f = [g for d in ("natural", "perturbed", "perturbed_v2") for g in glob.glob(f"data/{d}/*/{eid}.npz")][0]
    ep = dict(np.load(f, allow_pickle=True))
    env, desc, _ = make_task(int(ep["task_id"]))
    steps = [int(s) for s in ep["query_steps"]]
    a = max(0, t_pnr - args.half) // CHUNK * CHUNK
    b = min(int(ep["t_end"]), t_pnr + args.half)
    obs = restore_query(env, ep, steps.index(a))
    frames, drift = [], 0.0
    for t in range(a, b):
        img = np.concatenate([obs["agentview_image"][::-1, ::-1], obs["robot0_eye_in_hand_image"][::-1, ::-1]], axis=1)
        img = cv2.resize(np.ascontiguousarray(img), None, fx=2, fy=2, interpolation=cv2.INTER_NEAREST)
        img = np.concatenate([img, np.zeros((44, img.shape[1], 3), dtype=np.uint8)], axis=0)
        color = (255, 60, 60) if t >= t_pnr else (255, 255, 0)
        cv2.putText(img, f"step {t}  t_pnr {t_pnr}  {t - t_pnr:+d}", (10, 34), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
        cv2.putText(img, f"{eid}: {kind}: {desc}", (10, img.shape[0] - 14), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
        frames.append(img)
        obs, _, _, _ = env.step(ep["actions"][t].tolist())
        drift = max(drift, float(np.linalg.norm(obs["robot0_eef_pos"] - ep["eef"][t])) * 1000)
    env.close()
    path = os.path.join(args.out, f"{eid}_{kind}.mp4")
    imageio.mimsave(path, frames, fps=20)
    print(f"{eid}: {a} to {b}, replay vs recorded eef max {drift:.2f} mm -> {path}", flush=True)
