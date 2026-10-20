"""Detection window per failure (Fahad, Oct 20): t_alarm - t_pnr for every labelled failure with a t_pnr,
per model, from a 06_train_predictor.py run (per_episode.json).

Negative = alarm before t_pnr (timely), positive = late, "missed" = no alarm. Doomed-from-start failures
(t_pnr 0) are listed but left out of the medians and counts, as in all timing metrics.
"Earlier than SAFE" counts, for each other model, the failures where it alarms and SAFE-style alarms later
or not at all (ties and both missed are counted separately).

python scripts/12_detection_windows.py --pred results/predictor_seen_task --key "fixed 0.05"
"""

import argparse
import json
import os

import numpy as np

p = argparse.ArgumentParser()
p.add_argument("--pred", required=True, help="folder with per_episode.json")
p.add_argument("--models", nargs="+", default=["mlp", "combined", "mlp_reg", "combined_reg", "gated_mlp", "gated_combined", "progress", "safe"])
p.add_argument("--key", default="fixed 0.05", help="threshold mode and false-alarm limit (keys of 'alarms')")
p.add_argument("--reference", default="safe")
args = p.parse_args()

rows = json.load(open(os.path.join(args.pred, "per_episode.json")))
models = [m for m in args.models if any(r["model"] == m for r in rows)]
alarm = {(r["model"], r["eid"]): r["alarms"][args.key] for r in rows}
failures = sorted({(r["eid"], r["t_pnr"]) for r in rows if not r["success"] and r["t_pnr"] is not None})


def window(m, eid, t_pnr):
    a = alarm.get((m, eid))
    return None if a is None else a - t_pnr


lines = [f"# Detection window t_alarm - t_pnr (steps), {args.pred}, threshold {args.key}", "",
         "Negative = before t_pnr (timely). Doomed from start (t_pnr 0) shown, left out of medians and counts.", "",
         "| episode | t_pnr | " + " | ".join(models) + " |", "|---|---|" + "---|" * len(models)]
for eid, t_pnr in failures:
    cells = [("missed" if window(m, eid, t_pnr) is None else str(window(m, eid, t_pnr))) for m in models]
    lines.append(f"| {eid} | {t_pnr}{' (doomed)' if t_pnr == 0 else ''} | " + " | ".join(cells) + " |")
timed = [(eid, t) for eid, t in failures if t > 0]
med = []
for m in models:
    w = [window(m, eid, t) for eid, t in timed if window(m, eid, t) is not None]
    med.append(f"{np.median(w):.0f} ({len(w)} alarmed)" if w else "none")
lines.append(f"| median, t_pnr > 0 | | " + " | ".join(med) + " |")
lines += ["", f"Compared with {args.reference} on the {len(timed)} failures with t_pnr > 0 "
          "(earlier / same step / later / only one of them alarms / both missed):", ""]
for m in models:
    if m == args.reference:
        continue
    earlier = same = later = only_ours = only_ref = both_missed = 0
    for eid, t in timed:
        a, b = alarm.get((m, eid)), alarm.get((args.reference, eid))
        if a is None and b is None:
            both_missed += 1
        elif b is None:
            only_ours += 1
        elif a is None:
            only_ref += 1
        elif a < b:
            earlier += 1
        elif a == b:
            same += 1
        else:
            later += 1
    lines.append(f"- {m}: earlier on {earlier + only_ours} ({earlier} both alarm, {only_ours} {args.reference} missed), "
                 f"same {same}, later on {later + only_ref} ({later} both alarm, {only_ref} {m} missed), both missed {both_missed}")
text = "\n".join(lines) + "\n"
out = os.path.join(args.pred, f"windows_{args.key.replace(' ', '_')}.md")
open(out, "w").write(text)
print(text)
