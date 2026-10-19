#!/bin/bash
#SBATCH --job-name=pnr-train-pert
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=16
#SBATCH --mem=32G
#SBATCH --time=08:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Same as train.sbatch, with perturbed-natural episodes added (scanned failures, pre-check recoverable
# failures labelled 0, all perturbed successes). Separate output folder: the natural-only table stays as it is.
# Submitted by perturbed_submit_scans.sbatch after the perturbed scan array (afterany).
source slurm/common.sh
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
python scripts/06_train_predictor.py --scans "data/full_scans/*.json" "data/perturbed_scans/*.json" \
    --episodes "data/natural/*/*.npz" "data/perturbed/*/*.npz" --prechecks data/perturbed/prechecks \
    --out results/predictor_with_perturbed ${ARGS:-}
