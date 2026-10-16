"""Sanity check: GPU, imports, LIBERO-10 tasks, one short policy rollout (40 steps).

Run on a GPU node:  python scripts/00_check_env.py
"""

import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import torch  # noqa: E402

print("torch", torch.__version__, "| cuda available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("gpu:", torch.cuda.get_device_name(0))
print("MUJOCO_GL =", os.environ.get("MUJOCO_GL"), "| OFT_ROOT =", os.environ.get("OFT_ROOT"))

from pnr.sim import DEVICE, Policy, make_task, max_steps, rollout  # noqa: E402

print("policy device:", DEVICE, "(mps = Mac GPU, cuda:0 = NVIDIA, cpu = too slow for this pipeline)")

env, desc, inits = make_task(0)
print(f"task 0: '{desc}' | initial states: {len(inits)} | max policy steps: {max_steps()}")

t = time.time()
policy = Policy()
print(f"policy loaded in {time.time() - t:.0f}s")

t = time.time()
r = rollout(env, policy, desc, init_state=inits[0], limit=40)
print(f"40-step dry run: {time.time() - t:.1f}s | queries: {r.query_steps} | state dim: {r.query_states[0].shape}")
print("OK")
