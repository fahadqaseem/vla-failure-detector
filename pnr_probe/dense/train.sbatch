#!/bin/bash
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=16
#SBATCH --mem=64G
#SBATCH --time=3-00:00:00
#SBATCH --output=pnr_probe/logs/%x-%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# One 06_train_predictor.py run (pnr_probe copy, unchanged) on the episodes that passed the dense replay check
# (PASSED, default pnr_probe/data/dense_feat/unseen/passed.txt), labels as DATA=all (refined).
# Env: PHYS, NAME, ARGS, OUTR (results dir, default pnr_probe/results/dense).
source slurm/common.sh
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
D=$HOME/vla-failure-detector/data
python pnr_probe/06_train_predictor.py --scans "$D/full_scans/*.json" "$D/perturbed_scans/*.json" "$D/perturbed_v2_scans/*.json" \
    --episodes $(cat ${PASSED:-pnr_probe/data/dense_feat/unseen/passed.txt}) --prechecks $D/perturbed/prechecks $D/perturbed_v2/prechecks \
    --refine $D/week2_refine --phys $PHYS --alphas 0.025 0.05 0.10 0.20 --models progress gru_phys gru_phys_cusum \
    $ARGS --out ${OUTR:-pnr_probe/results/dense}/$NAME
