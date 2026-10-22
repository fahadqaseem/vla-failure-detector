#!/bin/bash
#SBATCH --job-name=pnr-lead
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=16
#SBATCH --mem=32G
#SBATCH --time=08:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Lead-label and CUSUM experiments (Fahad, Oct 22): one model (MODEL = mlp or combined) trained with label 1 from
# t_pnr - LEAD, its CUSUM alarm, and progress for the paired comparison. Leave-one-task-out, natural + perturbed-natural
# (7 of 10 tasks), fixed 5% threshold. LEAD=0 is today's model (same seed, so the same scores as predictor_with_perturbed).
# sbatch --export=ALL,LEAD=32,MODEL=mlp slurm/lead_experiments.sbatch
source slurm/common.sh
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
python scripts/06_train_predictor.py --scans "data/full_scans/*.json" "data/perturbed_scans/*.json" \
    --episodes "data/natural/*/*.npz" "data/perturbed/task0[0145678]/*.npz" --prechecks data/perturbed/prechecks \
    --lead $LEAD --models progress $MODEL ${MODEL}_cusum --out results/lead_experiments/lead${LEAD}_${MODEL}
