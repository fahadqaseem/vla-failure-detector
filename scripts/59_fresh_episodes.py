"""Pi0.5 episode counts (Fahad, Nov 9): per task and seed for the fresh perturbed seeds 2 to 4 (collected, gate, successes, failures, scanned
failures with timed / doomed / recoverable at 50%, 70%, 80%), totals for the whole Pi0.5 set, and per held-out task of the fresh unseen test
(catchable failures = t_pnr > 0, and successes, from results of the fresh report). Rules as 32_relabel.py: 50% = Jeffreys tau 0.5, 70% / 80% =
raw failure fraction of the K 4 retries.

python scripts/59_fresh_episodes.py --out results/pi05/fresh/episodes.md
"""

import argparse
import csv
import glob
import json
import os

from scipy.stats import beta

p = argparse.ArgumentParser()
p.add_argument("--out", default="results/pi05/fresh/episodes.md")
args = p.parse_args()
B = "data/pi05"
RULES = {50: lambda x: beta.ppf(0.25, sum(x) + 0.5, len(x) - sum(x) + 0.5) >= 0.5, 70: lambda x: 1 - sum(x) / len(x) < 0.7,
         80: lambda x: 1 - sum(x) / len(x) < 0.8}
EXCLUDED = {"task05_s3": "index.csv lost its header after a reqp requeue (13 episodes), no replay gate run",
            "task04_s3": "replay gate failed", "task05_s2": "replay gate failed", "task05_s4": "replay gate failed"}
scans = {}
for f in glob.glob(f"{B}/full_scans/*.json") + glob.glob(f"{B}/perturbed_scans/*.json"):
    s = json.load(open(f))
    scans[s["episode_id"]] = s


def t_pnr(s, rule):
    ok = [rule(list(x)) for x in s["successes"]]
    if ok[-1]:
        return None
    i = len(ok) - 1
    while i > 0 and not ok[i - 1]:
        i -= 1
    return s["checkpoints"][i]


def kinds(fails):
    out = []
    for thr, rule in RULES.items():
        t = [t_pnr(scans[e], rule) for e in fails if e in scans]
        out.append(f"{sum(x not in (None, 0) for x in t)} / {sum(x == 0 for x in t)} / {sum(x is None for x in t)}")
    return out


def folder(d):
    name = os.path.basename(d)
    if name == "task05_s3":  # no header: count lines, read success from column 5
        rows = [dict(episode_id=r[0], success=r[4]) for r in csv.reader(open(d + "/index.csv")) if len(r) > 4]
    else:
        rows = [r for r in csv.DictReader(open(d + "/index.csv")) if r.get("success") not in (None, "")]
    gate = "pass" if os.path.exists(d + "/GATE_PASS") else "FAIL" if os.path.exists(d + "/GATE_FAIL") else "none"
    fails = [r["episode_id"] for r in rows if int(r["success"]) == 0]
    return name, rows, gate, fails


lines = ["# Pi0.5 episodes: fresh seeds 2 to 4 and the whole set", "", __doc__.split("\n\n")[0].replace("\n", " "), "",
         "## Fresh perturbed seeds 2 to 4, per task and seed", "",
         "| folder | collected | gate | successes | failures | scanned failures | timed / doomed / recoverable 50% | 70% | 80% | status |",
         "|---|---|---|---|---|---|---|---|---|---|"]
for d in sorted(glob.glob(f"{B}/perturbed/task??_s[234]")):
    name, rows, gate, fails = folder(d)
    sc = sum(e in scans for e in fails)
    status = f"EXCLUDED: {EXCLUDED[name]}" if name in EXCLUDED else ("used" if gate == "pass" else "excluded (no gate pass)")
    lines.append(f"| {name} | {len(rows)} | {gate} | {len(rows) - len(fails)} | {len(fails)} | {sc} | " + " | ".join(kinds(fails)) + f" | {status} |")
lines += ["", "Failures of used folders that are not scanned: either recoverable by pre-check (no scan, label 0) or seed 4 failures past the",
          "70th scanned failure (pre-checked, never scanned, no label, not scored).", "", "## Whole Pi0.5 set", "",
          "| set | episodes | successes | failures | scanned failures | catchable at 50% (t_pnr > 0) |", "|---|---|---|---|---|---|"]
tot = {}
for d in sorted(glob.glob(f"{B}/natural/task??")) + sorted(glob.glob(f"{B}/perturbed/task??*")):
    name, rows, gate, fails = folder(d)
    seed = "natural" if "/natural/" in d else ("perturbed seed " + (name.split("_s")[1] if "_s" in name else "0"))
    used = "/natural/" in d or (gate == "pass" and name not in EXCLUDED)
    for k in (seed + (" (used)" if used else " (not used)"), "all collected") + (("analysis set (used)",) if used else ()):
        t = tot.setdefault(k, [0, 0, 0, 0, 0])
        cat = sum(t_pnr(scans[e], RULES[50]) not in (None, 0) for e in fails if e in scans)
        for i, v in enumerate((len(rows), len(rows) - len(fails), len(fails), sum(e in scans for e in fails), cat)):
            t[i] += v
for k in sorted(tot, key=lambda k: (k.startswith(("all", "analysis")), k)):
    lines.append(f"| {k} | " + " | ".join(map(str, tot[k])) + " |")
lines += ["", "The natural set keeps all 10 tasks (successes of tasks 2, 3, 8, 9 are used; their failures are not scanned because the natural",
          "gate failed). Old = natural + perturbed seeds 0 and 1 (training); fresh = perturbed seeds 2 to 4 (test).", "",
          "## Fresh unseen test, per held-out task (scored episodes, from the fresh report)", "",
          "| held-out task | successes | catchable 50% | catchable 70% | catchable 80% | recoverable failures 50% |", "|---|---|---|---|---|---|"]
per = {}
for thr in RULES:
    rows = [r for r in json.load(open(f"data/pi05_fresh/thr{thr}/unseen/merged/per_episode.json")) if r["model"] == "progress"]
    for r in rows:
        x = per.setdefault(r["task"], {"succ": 0})
        x["succ"] = x["succ"] + r["success"] if thr == 50 else x["succ"]
        x[thr] = x.get(thr, 0) + (not r["success"] and r["t_pnr"] not in (None, 0))
        if thr == 50:
            x["rec"] = x.get("rec", 0) + (not r["success"] and r["t_pnr"] is None)
for t in sorted(per):
    x = per[t]
    lines.append(f"| {t} | {x['succ']} | {x.get(50, 0)} | {x.get(70, 0)} | {x.get(80, 0)} | {x.get('rec', 0)} |")
lines.append(f"| all | {sum(x['succ'] for x in per.values())} | " + " | ".join(str(sum(x.get(k, 0) for x in per.values())) for k in (50, 70, 80, "rec")) + " |")
os.makedirs(os.path.dirname(args.out), exist_ok=True)
open(args.out, "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
