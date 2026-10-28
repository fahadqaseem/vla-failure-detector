#!/bin/bash
#SBATCH --job-name=t2-diag
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=06:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Track 2 diagnosis (Oct 28): tasks 0 and 8, initial states 0 to 9. MODE=lerobot: LeRobot's own lerobot-eval with its
# default settings (compile off only); MODE=ours: 25_pi_diag.py with PNR_PI_STEPS actions per query.
source slurm/common_pi.sh
source slurm/t2_fail.sh
D=results/$PNR_POLICY/diag
if [ "$MODE" = lerobot ]; then
    rm -rf $D/lerobot_eval
    lerobot-eval --policy.path=$( [ $PNR_POLICY = pi0 ] && echo lerobot/pi0_libero_finetuned_v044 || echo lerobot/pi05_libero_finetuned_v044 ) \
        --policy.compile_model=false --policy.device=cuda --env.type=libero --env.task=libero_10 --env.task_ids='[0,8]' \
        --eval.batch_size=1 --eval.n_episodes=10 --output_dir=$D/lerobot_eval || exit 1
    find $D/lerobot_eval -name "*.mp4" -delete
else
    python scripts/25_pi_diag.py --tasks 0 8 --episodes 10 --out $D/ours_$PNR_PI_STEPS.json || exit 1
fi
