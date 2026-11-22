"""20-replay ground truth pilot (results/plan_nov22_gt20.md, Step 1).

For one recorded failed episode: at every checkpoint every --every steps, bring the replay count to --K. Existing replays with the same
settings are reused (the K 4 scan, seed 0, and the K 12 refinement, seed 1, where present); new replays use --seed (20), with the same
rollout call and rng rule as 03_pnr_scan.py: default_rng([seed, task, episode_idx, checkpoint, k]).
One JSON per checkpoint (OUT/<episode_id>/c<step>.json), so a requeued job resumes where it stopped.

python scripts/63_gt20_scan.py --episode data/perturbed_v2/task00/t00_e06_p0_s1.npz --scans "data/perturbed_v2_scans/*.json" \
    --refine data/week2_refine --out data/gt20_pilot
"""

import argparse
import glob
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np  # noqa: E402

from pnr.policy import CHUNK, DETERMINISTIC, REPLAY_START, Policy, make_task, max_steps, rollout  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("--episode", required=True)
p.add_argument("--scans", required=True, help="glob of existing scan JSONs (one of them is this episode's)")
p.add_argument("--refine", default=None, help="folder of refinement JSONs (extra replays at boundary checkpoints)")
p.add_argument("--every", type=int, default=16)
p.add_argument("--K", type=int, default=20)
p.add_argument("--seed", type=int, default=20, help="seed of the new replays; 0, 1 and 100 are already used")
p.add_argument("--noise_std", type=float, default=0.05)
p.add_argument("--extra_steps", type=int, default=200)
p.add_argument("--out", default="data/gt20_pilot")
args = p.parse_args()
assert args.every % CHUNK == 0

ep = np.load(args.episode, allow_pickle=True)
eid = os.path.splitext(os.path.basename(args.episode))[0]
task, idx = int(ep["task_id"]), int(ep["episode_idx"])
SAME = dict(noise_std=args.noise_std, extra_steps=args.extra_steps, replay_start=REPLAY_START, deterministic=DETERMINISTIC)


def matches(params):
    return all(params.get(k) == v for k, v in SAME.items())


# Reusable replays per checkpoint: (seed, k, success, end_step).
reuse = {}
sources = [f for f in glob.glob(args.scans) if os.path.basename(f) == eid + ".json"]
if args.refine and os.path.exists(os.path.join(args.refine, eid + ".json")):
    sources.append(os.path.join(args.refine, eid + ".json"))
for f in sources:
    s = json.load(open(f))
    if not matches(s["params"]):
        print(f"not reused (settings differ): {f} {s['params']}")
        continue
    for c, succ, ends in zip(s["checkpoints"], s["successes"], s["end_steps"]):
        reuse.setdefault(int(c), []).extend(
            (s["params"]["seed"], k, int(v), int(e)) for k, (v, e) in enumerate(zip(succ, ends)))
print(eid, "reused sources:", sources)

q_steps = [int(s) for s in ep["query_steps"]]
query_of = {s: i for i, s in enumerate(q_steps)}
checkpoints = [s for s in q_steps if s % args.every == 0]
out_dir = os.path.join(args.out, eid)
os.makedirs(out_dir, exist_ok=True)
env, desc, _ = make_task(task)
policy = Policy()
rng_of = lambda seed, c, k: np.random.default_rng([seed, task, idx, c, k])  # noqa: E731

for c in checkpoints:
    path = os.path.join(out_dir, f"c{c:03d}.json")
    if os.path.exists(path):
        continue
    old = reuse.get(c, [])[: args.K]
    new_keys = [(args.seed, k) for k in range(args.K - len(old))]
    # Seeds must not overlap: (seed, k) pairs disjoint, and the first noise vector of each new replay differs from each reused one.
    old_keys = {(s, k) for s, k, _, _ in old}
    assert not old_keys & set(new_keys), (c, old_keys & set(new_keys))
    first = {key: rng_of(key[0], c, key[1]).normal(0, 1, 6) for key in old_keys | set(new_keys)}
    for a in new_keys:
        for b in old_keys:
            assert not np.allclose(first[a], first[b]), (c, a, b)
    replays = [dict(seed=s, k=k, success=v, end_step=e, seconds=None, source="reused") for s, k, v, e in old]
    for s, k in new_keys:
        t0 = time.time()
        r = rollout(env, policy, desc, episode=ep, query=query_of[c], noise_std=args.noise_std, rng=rng_of(s, c, k),
                    record_states=False, horizon=max_steps() + args.extra_steps)
        replays.append(dict(seed=s, k=k, success=int(r.success), end_step=int(r.t_end), seconds=round(time.time() - t0, 2), source="new"))
    rec = dict(episode_id=eid, task_id=task, episode_idx=idx, checkpoint=c, t_end=int(ep["t_end"]), replays=replays,
               params=dict(SAME, every=args.every, K=args.K, new_seed=args.seed, gpu=os.environ.get("CUDA_VISIBLE_DEVICES"),
                           node=os.uname().nodename, job=os.environ.get("SLURM_JOB_ID")))
    with open(path + ".tmp", "w") as fh:
        json.dump(rec, fh, indent=1)
    os.replace(path + ".tmp", path)
    n_ok = sum(r["success"] for r in replays)
    print(f"{eid} t={c}: {len(old)} reused + {len(new_keys)} new, successes {n_ok}/{len(replays)}", flush=True)
env.close()
print(eid, "done")
