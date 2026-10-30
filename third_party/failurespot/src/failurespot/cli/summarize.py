from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

import numpy as np


def main() -> None:
    parser = argparse.ArgumentParser(description="Aggregate FailureSpot seed metrics.")
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    groups = defaultdict(list)
    for path in args.root.rglob("metrics.json"):
        payload = json.loads(path.read_text(encoding="utf-8"))
        if "architecture" not in payload or "metrics" not in payload:
            continue
        key = (payload["method"], payload["architecture"])
        groups[key].append(payload["metrics"])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            ["method", "architecture", "split", "metric", "mean", "sample_std", "seeds"]
        )
        for (method, architecture), runs in sorted(groups.items()):
            for split in ("seen", "unseen"):
                for metric in ("trajectory_auroc", "timestamp_auroc"):
                    values = [
                        run[split][metric]
                        for run in runs
                        if run.get(split, {}).get(metric) is not None
                    ]
                    writer.writerow(
                        [
                            method,
                            architecture,
                            split,
                            metric,
                            float(np.mean(values)) if values else "",
                            float(np.std(values, ddof=1)) if len(values) > 1 else 0.0,
                            len(values),
                        ]
                    )


if __name__ == "__main__":
    main()
