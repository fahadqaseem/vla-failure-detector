#!/bin/bash
#SBATCH --job-name=gt20-worker
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=7-00:00:00
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Nov 22 amendment (results/plan_nov22_gt20.md): full 20-replay ground truth, every 8 steps. One array task = one worker; every worker
# walks the same target list and claims checkpoints by lock (67_gt20_worker.py), so a killed or restarted worker loses at most the
# checkpoint it was on. One array (%5) = the 5-GPU cap. L40S only: on A30 the same seeds gave a different outcome in 12 of 40 replays
# (results/gt20/gpu_check/NVIDIA_A30.json); H200 untested. GPU name stored per replay.
# P=oft|pi05.
P=${P:-oft}
if [ "$P" = oft ]; then
  source slurm/common.sh
  python scripts/67_gt20_worker.py --targets results/gt20/targets_oft.txt \
    --scans "data/full_scans/*.json" "data/perturbed_scans/*.json" "data/perturbed_v2_scans/*.json" \
    --refine data/week2_refine --pilot data/gt20_pilot --every 8 --K 20 --seed 20 --noise_std 0.05 --extra_steps 200 --out data/gt20/oft
else
  export PNR_POLICY=pi05; source slurm/common_pi.sh
  python scripts/67_gt20_worker.py --targets results/gt20/targets_pi05.txt \
    --scans "data/pi05/full_scans/*.json" "data/pi05/perturbed_scans/*.json" \
    --every 8 --K 20 --seed 20 --noise_std 0 --extra_steps 200 --out data/gt20/pi05
fi
