#!/bin/bash
#SBATCH --job-name=w2-phase-d
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=00:20:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Week 2 Phase D: after the refinement (and the Phase C report, for the best variants): the final comparison on
# all data (natural + perturbed + perturbed_v2, refined labels), unseen (headline) and seen, then the report.
source slurm/common.sh
BEST=$(cat results/week2/C_best.txt 2>/dev/null)
MODELS="progress gated_mlp gated_combined mlp_cusum combined_cusum $BEST"
echo "Phase D models: $MODELS"
U=$(sbatch --parsable -J w2-D-unseen --export=ALL,DATA=all,NAME=D_unseen,ARGS="--models $MODELS" slurm/w2_train.sbatch)
S=$(sbatch --parsable -J w2-D-seen --export=ALL,DATA=all,NAME=D_seen,ARGS="--split episode --models $MODELS" slurm/w2_train.sbatch)
sbatch --dependency=afterok:$U:$S --export=ALL,PHASE=D slurm/w2_report.sbatch
