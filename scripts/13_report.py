"""One table per run of 06_train_predictor.py (Fahad, Oct 20): for every model, timely alarms with a bootstrap 95%
interval, median detection window, false alarms on successes and unnecessary alarms on recoverable failures.

Bootstrap over failures: draw the failures with t_pnr > 0 with replacement (--n_boot times, seeded), count timely
alarms in each draw, take the 2.5 and 97.5 percentiles. "vs reference" is a paired bootstrap of (timely of the model
minus timely of --reference) on the same draws: if its interval holds 0, the difference is not clear from these data.
Successes and recoverable failures are not resampled (their numbers are shown as counted).
Doomed-from-start failures (t_pnr 0) are left out, as in all timing metrics.

python scripts/13_report.py --pred results/predictor results/predictor_seen_task --key "fixed 0.05"
"""

import argparse
import json
import os

import numpy as np

p = argparse.ArgumentParser()
p.add_argument("--pred", nargs="+", required=True, help="folders with per_episode.json (one table row block each)")
p.add_argument("--key", default="fixed 0.05", help="threshold mode and false-alarm limit (keys of 'alarms')")
p.add_argument("--reference", default="progress")
p.add_argument("--n_boot", type=int, default=10000)
p.add_argument("--seed", type=int, default=0)
p.add_argument("--out", default=None, help="markdown file (default: report_{key}.md in the first --pred folder)")
args = p.parse_args()

lines = [f"# Timely alarms with bootstrap 95% intervals, threshold {args.key}", "",
         "Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, "
         f"{args.n_boot} draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). "
         f"vs {args.reference} = paired bootstrap interval of the difference in timely counts.", "",
         f"| run | model | timely (95% interval) | vs {args.reference} | median window (alarmed) | false alarms on successes "
         "| unnecessary alarms on recoverable failures |",
         "|---|---|---|---|---|---|---|"]
for pred in args.pred:
    rows = json.load(open(os.path.join(pred, "per_episode.json")))
    models = list(dict.fromkeys(r["model"] for r in rows))
    alarm = {(r["model"], r["eid"]): r["alarms"][args.key] for r in rows}
    timed = sorted({r["eid"]: r["t_pnr"] for r in rows if not r["success"] and r["t_pnr"] not in (None, 0)}.items())
    rng = np.random.default_rng(args.seed)
    draws = rng.integers(0, len(timed), size=(args.n_boot, len(timed)))  # same draws for every model (paired)
    timely = {m: np.array([alarm[(m, eid)] is not None and alarm[(m, eid)] <= t for eid, t in timed]) for m in models}
    for m in models:
        mine = [r for r in rows if r["model"] == m]
        succ = [r for r in mine if r["success"]]
        recov = [r for r in mine if not r["success"] and r["t_pnr"] is None]
        window = [alarm[(m, eid)] - t for eid, t in timed if alarm[(m, eid)] is not None]
        lo, hi = np.percentile(timely[m][draws].sum(1), [2.5, 97.5])
        if m == args.reference or args.reference not in timely:
            vs = ""
        else:
            d = timely[m][draws].sum(1) - timely[args.reference][draws].sum(1)
            d_lo, d_hi = np.percentile(d, [2.5, 97.5])
            vs = f"{int(timely[m].sum() - timely[args.reference].sum()):+d} ({d_lo:+.0f} to {d_hi:+.0f})"
        lines.append(f"| {pred} | {m} | {int(timely[m].sum())} of {len(timed)} ({lo:.0f} to {hi:.0f}) | {vs} | "
                     + (f"{np.median(window):+.0f} ({len(window)})" if window else "none") + " | "
                     f"{sum(r['alarms'][args.key] is not None for r in succ)} of {len(succ)} "
                     f"({np.mean([r['alarms'][args.key] is not None for r in succ]):.3f}) | "
                     f"{sum(r['alarms'][args.key] is not None for r in recov)} of {len(recov)} |")
text = "\n".join(lines) + "\n"
out = args.out or os.path.join(args.pred[0], f"report_{args.key.replace(' ', '_')}.md")
open(out, "w").write(text)
print(text)
