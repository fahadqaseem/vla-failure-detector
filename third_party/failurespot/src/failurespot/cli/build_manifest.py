from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def scalar(payload, name):
    if name not in payload:
        raise ValueError(f"Missing {name}")
    return np.asarray(payload[name]).item()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build a FailureSpot JSONL manifest from self-describing NPZ trajectories."
    )
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--policy", required=True)
    args = parser.parse_args()
    rows = []
    for path in sorted(args.root.rglob("*.npz")):
        with np.load(path, allow_pickle=False) as payload:
            task_id = int(scalar(payload, "task_id"))
            episode_id = int(scalar(payload, "episode_id"))
        rows.append(
            {
                "path": str(path.resolve()),
                "policy": args.policy,
                "task_id": task_id,
                "episode_id": episode_id,
            }
        )
    if not rows:
        raise ValueError(f"No NPZ trajectories found under {args.root}")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        "".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8"
    )
    print(f"Wrote {len(rows)} trajectories to {args.output}")


if __name__ == "__main__":
    main()
