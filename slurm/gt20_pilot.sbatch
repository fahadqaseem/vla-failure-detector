#!/bin/bash
#SBATCH --job-name=gt20-pilot
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=12:00:00
#SBATCH --array=0-2
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Nov 22 plan (results/plan_nov22_gt20.md, Step 1): K 20 every 16 steps on the 3 pilot runs, one array task per run.
# Resumable: finished checkpoints (data/gt20_pilot/<eid>/c<step>.json) are skipped.
source slurm/common.sh
RUNS=(data/perturbed_v2/task00/t00_e06_p0_s1.npz data/perturbed_v2/task01/t01_e07_p0_s1.npz data/perturbed_v2/task04/t04_e00_p0_s2.npz)
python scripts/63_gt20_scan.py --episode ${RUNS[$SLURM_ARRAY_TASK_ID]} --scans "data/perturbed_v2_scans/*.json" \
    --refine data/week2_refine --every 16 --K 20 --seed 20 --noise_std 0.05 --extra_steps 200 --out data/gt20_pilot
