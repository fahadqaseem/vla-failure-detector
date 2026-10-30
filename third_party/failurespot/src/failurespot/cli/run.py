from __future__ import annotations

import argparse
from pathlib import Path

from failurespot.config import ExperimentConfig
from failurespot.data import read_manifest, split_trajectories, validate_trajectories
from failurespot.experiment import (
    clone_config,
    run_action_probe,
    run_logpzo,
    run_score_baseline,
    run_trainable,
    write_result,
)


ABLATION_METHODS = (
    "weak_only",
    "weak_random_finetune",
    "trajectory_active_finetune",
    "failurespot",
)


def split_for(config, trajectories, seed, train_fraction=0.60):
    seen = config.data.seen_task_splits[seed % len(config.data.seen_task_splits)]
    return split_trajectories(trajectories, seen, train_fraction, seed)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run FailureSpot main, ablation, or data-scaling experiments."
    )
    parser.add_argument("--config", required=True)
    parser.add_argument(
        "--experiment", choices=("main", "ablation", "scaling"), default="main"
    )
    parser.add_argument("--architectures", nargs="+", choices=("mlp", "lstm"), default=("mlp", "lstm"))
    parser.add_argument("--seeds", nargs="+", type=int, default=(0, 1, 2))
    parser.add_argument("--device")
    parser.add_argument("--output")
    args = parser.parse_args()
    base_config = ExperimentConfig.load(args.config)
    if args.device:
        base_config.training.device = args.device
    if args.output:
        base_config.output.directory = args.output
    trajectories = read_manifest(base_config.data.manifest, base_config.policy.name)
    validate_trajectories(trajectories, base_config)
    output_root = Path(base_config.output.directory)

    for seed in args.seeds:
        config = clone_config(base_config)
        config.training.seed = seed
        split = split_for(config, trajectories, seed)
        if args.experiment == "main":
            for architecture in args.architectures:
                for method in ("safe", "supervised_random", "failurespot"):
                    destination = output_root / "main" / f"seed{seed}" / method / architecture
                    result = run_trainable(method, architecture, split, config, destination)
                    write_result(destination / "metrics.json", result)
                if config.policy.name in {"pi0", "openvla"}:
                    destination = output_root / "main" / f"seed{seed}" / "actprobe" / architecture
                    write_result(
                        destination / "metrics.json",
                        run_action_probe(architecture, split, config, destination),
                    )
            result = run_score_baseline("stac", split, config)
            write_result(
                output_root / "main" / f"seed{seed}" / "stac" / "metrics.json",
                result,
            )
            destination = output_root / "main" / f"seed{seed}" / "logpzo"
            result = run_logpzo(split, config, destination)
            write_result(
                destination / "metrics.json",
                result,
            )

        elif args.experiment == "ablation":
            for architecture in args.architectures:
                for method in ABLATION_METHODS:
                    destination = (
                        output_root / "ablation" / f"seed{seed}" / method / architecture
                    )
                    result = run_trainable(method, architecture, split, config, destination)
                    write_result(destination / "metrics.json", result)

        else:
            for architecture in args.architectures:
                for pretrain_fraction in (0.20, 0.40, 0.60, 0.80):
                    scaling_split = split_for(
                        config, trajectories, seed, pretrain_fraction
                    )
                    for annotation_fraction in (0.00, 0.05, 0.10, 0.15, 0.20):
                        destination = (
                            output_root
                            / "scaling"
                            / f"seed{seed}"
                            / architecture
                            / f"pretrain_{pretrain_fraction:.2f}"
                            / f"annotation_{annotation_fraction:.2f}"
                        )
                        method = "weak_only" if annotation_fraction == 0.0 else "failurespot"
                        result = run_trainable(
                            method,
                            architecture,
                            scaling_split,
                            config,
                            destination,
                            annotation_fraction,
                        )
                        result["pretrain_fraction"] = pretrain_fraction
                        result["annotation_fraction"] = annotation_fraction
                        write_result(destination / "metrics.json", result)


if __name__ == "__main__":
    main()
