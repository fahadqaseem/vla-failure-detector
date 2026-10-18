#!/bin/bash
#SBATCH --job-name=pnr-train
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=16
#SBATCH --mem=32G
#SBATCH --time=04:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Per-step t_pnr predictor, leave-one-task-out (CPU only). Extra flags via ARGS, e.g. ARGS="--epochs 100".
source slurm/common.sh
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
python scripts/06_train_predictor.py --scans "data/full_scans/*.json" --episodes "data/natural/*/*.npz" \
    --out results/predictor ${ARGS:-}
