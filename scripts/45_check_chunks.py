"""Before FailureSpot convert (Nov 6): every Pi0.5 episode that 29_fs_convert.py can read (natural, and perturbed in gate-passed folders) has its
50-step chunk file from 41_pi_chunks.py. Prints counts per task and exits 1 if any task is missing files or has none.

python scripts/45_check_chunks.py --policy pi05
"""

import argparse
import glob
import os
import sys

p = argparse.ArgumentParser()
p.add_argument("--policy", default="pi05")
args = p.parse_args()
base = f"data/{args.policy}"
eps = glob.glob(f"{base}/natural/*/*.npz")
eps += [f for d in glob.glob(f"{base}/perturbed/task*") if os.path.exists(d + "/GATE_PASS") for f in glob.glob(d + "/*.npz")]
bad = False
for t in range(10):
    mine = [os.path.splitext(os.path.basename(f))[0] for f in eps if os.path.basename(f).startswith(f"t{t:02d}_") and ".tmp." not in f]
    miss = [e for e in mine if not os.path.exists(f"{base}/chunks/{e}.npz")]
    print(f"task {t}: {len(mine) - len(miss)} of {len(mine)} chunk files" + (f", missing e.g. {miss[:3]}" if miss else ""))
    bad |= bool(miss) or not mine
sys.exit(1 if bad else 0)
