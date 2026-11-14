#!/bin/bash
#SBATCH --job-name=n13-smoke2
#SBATCH --partition=reqp
#SBATCH --qos=requeue
#SBATCH --cpus-per-task=2
#SBATCH --mem=16G
#SBATCH --time=00:30:00
#SBATCH --output=logs/%x-%j.out
# Smoke test of 61_regression_report.py and 62_regression_plots.py on the data/regression_v2_smoke output (held-out task 0 only).
source slurm/common.sh
set -e
python scripts/61_regression_report.py --root data/regression_v2_smoke --out data/regression_v2_smoke/report --min_groups 1
python scripts/62_regression_plots.py --root data/regression_v2_smoke --out data/regression_v2_smoke/report/plots
head -30 data/regression_v2_smoke/report/main.md; cat data/regression_v2_smoke/report/backup.md data/regression_v2_smoke/report/seeds.md; ls data/regression_v2_smoke/report/plots
echo smoke2 ok
