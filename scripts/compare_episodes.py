"""Check that two recordings of the same episode are identical (same actions, sim states and outcome).

Used after changing the recording code: the new run must reproduce the old one exactly.
python scripts/compare_episodes.py data/rollouts/t00_e00_n0.npz data/feature_check/t00_e00_n0.npz
Exit code 0 = identical, 1 = something differs.
"""

import sys

import numpy as np

a = np.load(sys.argv[1], allow_pickle=True)
b = np.load(sys.argv[2], allow_pickle=True)

ok = True
for key in ["success", "t_end", "query_steps", "actions", "eef", "query_states", "query_grippers"]:
    same = a[key].shape == b[key].shape and np.array_equal(a[key], b[key])
    diff = float(np.abs(a[key].astype(float) - b[key].astype(float)).max()) if a[key].shape == b[key].shape else "shape differs"
    print(f"{key:15s} identical={same}  shape {a[key].shape} vs {b[key].shape}  max |diff| {diff}")
    ok = ok and same

if "features" in b.files:
    print(f"new features {b['features'].shape} {b['features'].dtype}, features_mean {b['features_mean'].shape}; "
          f"one per query: {len(b['features']) == len(b['query_steps'])}")
    ok = ok and len(b["features"]) == len(b["query_steps"])

print("IDENTICAL" if ok else "DIFFERENT: do not collect with this code")
sys.exit(0 if ok else 1)
