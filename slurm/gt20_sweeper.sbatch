#!/bin/bash
#SBATCH --job-name=gt20-oft-sweep
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=7-00:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Nov 27: one OFT worker after all OFT worker jobs end (afterany). Runs exactly the OFT branch of slurm/gt20_worker.sbatch (same script,
# every 8, K 20, seed 20, noise 0.05, +200); 67_gt20_worker.py passes until no checkpoint is missing, taking over stale locks of
# timed-out workers. GPU cap: the Pi0.5 array is throttled to 4 while this runs; at the end this job sets it back to 5 (PI05_JOB).
cd ~/vla-failure-detector
P=oft bash slurm/gt20_worker.sbatch
rc=$?
python scripts/70_gt20_complete.py --targets results/gt20/targets_oft.txt --dir data/gt20/oft
[ -n "$PI05_JOB" ] && scontrol update JobId=$PI05_JOB ArrayTaskThrottle=5
exit $rc
