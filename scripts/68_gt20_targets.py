"""Target lists for the full 20-replay run (plan_nov22_gt20.md amendment): the kept failed runs of regression v2 (data/regression_v2,
any model, seed 0 rows; OFT 136, Pi0.5 37), one episode .npz per line, sorted by episode id. Reads JSON only.

python scripts/68_gt20_targets.py
"""
import glob
import json
import os

ROOTS = {"oft": ["data/natural", "data/perturbed", "data/perturbed_v2"], "pi05": ["data/pi05/natural", "data/pi05/perturbed"]}
os.makedirs("results/gt20", exist_ok=True)
for pol, roots in ROOTS.items():
    eids = sorted({r["eid"] for f in glob.glob(f"data/regression_v2/{pol}/const/s0/g*.json") for r in json.load(open(f))["rows"]
                   if not r["success"]})
    paths = {os.path.basename(f)[:-4]: f for r in roots for f in glob.glob(os.path.join(r, "*", "*.npz"))}
    lines = [paths[e] for e in eids]
    open(f"results/gt20/targets_{pol}.txt", "w").write("\n".join(lines) + "\n")
    print(pol, len(lines))
