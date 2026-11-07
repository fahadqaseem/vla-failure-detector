"""Replay scans with per-retry end steps, for 54_rescue.py and 56_clock.py (OpenVLA-OFT adds the K 12 refinement)."""

import glob
import json
import os

SCANS = {"oft": (["data/full_scans/*.json", "data/perturbed_scans/*.json", "data/perturbed_v2_scans/*.json"], "data/week2_refine"),
         "pi05": (["data/pi05/full_scans/*.json", "data/pi05/perturbed_scans/*.json"], None)}


def load_scans(pol):
    pats, refine = SCANS[pol]
    scans = {}
    for f in [f for pat in pats for f in glob.glob(pat)]:
        s = json.load(open(f))
        scans[s["episode_id"]] = dict(c=s["checkpoints"], ok=[list(x) for x in s["successes"]], end=[list(x) for x in s["end_steps"]])
    for f in glob.glob(os.path.join(refine, "*.json")) if refine else []:
        r = json.load(open(f))
        s = scans[r["episode_id"]]
        for c, ok, end in zip(r["checkpoints"], r["successes"], r["end_steps"]):
            i = s["c"].index(c)
            s["ok"][i] += list(ok)
            s["end"][i] += list(end)
    return scans
