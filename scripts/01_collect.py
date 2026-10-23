"""Record LIBERO-10 episodes with OpenVLA-OFT: actions, eef positions and sim states at every chunk boundary.

Natural failures:  python scripts/01_collect.py --tasks 0 1 2 3 4 5 6 7 8 9 --episodes 5
Induced failures:  python scripts/01_collect.py --tasks 0 1 --episodes 5 --noise_std 0.15   (labelled induced)
Perturbed-natural: python scripts/01_collect.py --tasks 0 --episodes 50 --perturb --out data/perturbed/task00
                   (no action noise; objects moved at the start, rule in pnr/perturb.py and CLAUDE.md)
"""

import argparse
import csv
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import imageio  # noqa: E402
import numpy as np  # noqa: E402

from pnr.perturb import perturbed_start  # noqa: E402
from pnr.sim import Policy, make_task, rollout, save_episode  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--tasks", type=int, nargs="+", default=list(range(10)))
p.add_argument("--episodes", type=int, default=5, help="episodes per task")
p.add_argument("--start_idx", type=int, default=0, help="first LIBERO initial-state index to use")
p.add_argument("--noise_std", type=float, default=0.0, help=">0 means induced failures (labelled)")
p.add_argument("--seed", type=int, default=0)
p.add_argument("--out", default="data/rollouts")
p.add_argument("--save_video", action="store_true")
p.add_argument("--perturb", action="store_true", help="perturbed-natural: move the objects of each initial state (pnr/perturb.py)")
args = p.parse_args()

os.makedirs(args.out, exist_ok=True)
index_path = os.path.join(args.out, "index.csv")
new_index = not os.path.exists(index_path)
policy = Policy()

with open(index_path, "a", newline="") as f:
    w = csv.writer(f)
    if new_index:
        w.writerow(["episode_id", "task_id", "episode_idx", "description", "success", "t_end", "noise_std", "induced", "perturbed"])
    for task_id in args.tasks:
        env, desc, inits = make_task(task_id)
        for ep in range(args.start_idx, args.start_idx + args.episodes):
            rng = np.random.default_rng([args.seed, task_id, ep])
            t0 = time.time()
            init, extra = inits[ep], {}
            if args.perturb:
                init, info, attempt, rejected = perturbed_start(env, inits[ep], args.seed, task_id, ep)
                if init is None:
                    print(f"t{task_id:02d}_e{ep:02d}: no valid perturbed start in {len(rejected)} attempts, skipped: {rejected[:3]}", flush=True)
                    continue
                extra = dict(perturbed=True, perturbation=json.dumps(info), perturb_attempt=attempt,
                             base_init_state=np.asarray(inits[ep]))
                print(f"t{task_id:02d}_e{ep:02d}: perturbed start, attempt {attempt}, rejected: {rejected}", flush=True)
            r = rollout(env, policy, desc, init_state=init, noise_std=args.noise_std, rng=rng,
                        save_frames=args.save_video)
            eid = f"t{task_id:02d}_e{ep:02d}_{'p' if args.perturb else 'n'}{args.noise_std:g}"
            if args.perturb and args.seed:  # week 2 (Oct 23): new perturbation seeds get their own ids
                eid += f"_s{args.seed}"
            save_episode(os.path.join(args.out, eid + ".npz"), r, task_id=task_id, episode_idx=ep,
                         description=desc, init_state=init, noise_std=args.noise_std, seed=args.seed, **extra)
            if args.save_video and r.frames:
                imageio.mimsave(os.path.join(args.out, eid + ".mp4"), r.frames, fps=30)
            w.writerow([eid, task_id, ep, desc, int(r.success), r.t_end, args.noise_std, int(args.noise_std > 0), int(args.perturb)])
            f.flush()
            feats = np.stack(r.features)
            # float16 overflows above 65504 (becomes inf), so print the largest value as a check.
            feat_info = f"features {feats.shape} max|x| {np.abs(feats.astype(np.float32)).max():.1f} finite {np.isfinite(feats).all()}"
            print(f"{eid} | success={r.success} | steps={r.t_end} | {time.time() - t0:.0f}s | {feat_info} | {desc}", flush=True)
        env.close()
