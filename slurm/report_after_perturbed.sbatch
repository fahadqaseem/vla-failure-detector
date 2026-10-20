#!/bin/bash
#SBATCH --job-name=pnr-report
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --time=00:30:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Report tables (Fahad, Oct 20): timely alarms with bootstrap 95% intervals, median window, false alarms, unnecessary
# alarms, on the unseen (leave-one-task-out) and seen-task splits; detection windows vs SAFE-style.
# Natural only and natural + perturbed-natural (7 of 10 tasks) are separate folders, never pooled with each other.
source slurm/common.sh
for key in "fixed 0.05" "fixed 0.10" "fixed 0.20" "time-varying 0.05"; do
    python scripts/13_report.py --pred results/predictor_gated results/predictor_seen_task_gated --key "$key"
    python scripts/13_report.py --pred results/predictor_with_perturbed results/predictor_with_perturbed_seen_task --key "$key"
done
for d in results/predictor_gated results/predictor_seen_task_gated results/predictor_with_perturbed results/predictor_with_perturbed_seen_task; do
    python scripts/12_detection_windows.py --pred $d --models mlp combined gated_mlp gated_combined progress safe --key "fixed 0.05"
done
