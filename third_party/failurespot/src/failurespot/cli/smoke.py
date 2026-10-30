from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path

from failurespot.smoke import run_smoke


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the FailureSpot CPU smoke test.")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.output:
        results = run_smoke(args.output)
    else:
        with tempfile.TemporaryDirectory(prefix="failurespot-smoke-") as directory:
            results = run_smoke(directory)
    summary = {
        architecture: {
            "selected_count": result["selected_count"],
            "seen": result["metrics"]["seen"],
            "unseen": result["metrics"]["unseen"],
        }
        for architecture, result in results.items()
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
