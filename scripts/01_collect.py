"""Record LIBERO-10 episodes with OpenVLA-OFT: actions, eef positions and sim states at every chunk boundary.

Natural failures:  python scripts/01_collect.py --tasks 0 1 2 3 4 5 6 7 8 9 --episodes 5
Induced failures:  python scripts/01_collect.py --tasks 0 1 --episodes 5 --noise_std 0.15   (labelled induced)
"""

import argparse
import csv
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import imageio  # noqa: E402
import numpy as np  # noqa: E402

from pnr.sim import Policy, make_task, rollout, save_episode  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--tasks", type=int, nargs="+", default=list(range(10)))
p.add_argument("--episodes", type=int, default=5, help="episodes per task")
p.add_argument("--start_idx", type=int, default=0, help="first LIBERO initial-state index to use")
p.add_argument("--noise_std", type=float, default=0.0, help=">0 means induced failures (labelled)")
p.add_argument("--seed", type=int, default=0)
p.add_argument("--out", default="data/rollouts")
p.add_argument("--save_video", action="store_true")
args = p.parse_args()

os.makedirs(args.out, exist_ok=True)
index_path = os.path.join(args.out, "index.csv")
new_index = not os.path.exists(index_path)
policy = Policy()

with open(index_path, "a", newline="") as f:
    w = csv.writer(f)
    if new_index:
        w.writerow(["episode_id", "task_id", "episode_idx", "description", "success", "t_end", "noise_std", "induced"])
    for task_id in args.tasks:
        env, desc, inits = make_task(task_id)
        for ep in range(args.start_idx, args.start_idx + args.episodes):
            rng = np.random.default_rng([args.seed, task_id, ep])
            t0 = time.time()
            r = rollout(env, policy, desc, init_state=inits[ep], noise_std=args.noise_std, rng=rng,
                        save_frames=args.save_video)
            eid = f"t{task_id:02d}_e{ep:02d}_n{args.noise_std:g}"
            save_episode(os.path.join(args.out, eid + ".npz"), r, task_id=task_id, episode_idx=ep,
                         description=desc, init_state=inits[ep], noise_std=args.noise_std, seed=args.seed)
            if args.save_video and r.frames:
                imageio.mimsave(os.path.join(args.out, eid + ".mp4"), r.frames, fps=30)
            w.writerow([eid, task_id, ep, desc, int(r.success), r.t_end, args.noise_std, int(args.noise_std > 0)])
            f.flush()
            print(f"{eid} | success={r.success} | steps={r.t_end} | {time.time() - t0:.0f}s | {desc}", flush=True)
        env.close()
