#!/bin/bash
#SBATCH --job-name=pnr-lead-report
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --time=00:30:00
#SBATCH --output=logs/%x-%j.out
# Report of the lead-label and CUSUM runs (results/lead_experiments), bootstrap 95% intervals vs progress.
source slurm/common.sh
R=results/lead_experiments
python scripts/13_report.py --pred $R/lead0_mlp $R/lead32_mlp $R/lead64_mlp $R/lead0_combined $R/lead32_combined \
    $R/lead64_combined --key "fixed 0.05" --out $R/report_fixed_0.05.md
