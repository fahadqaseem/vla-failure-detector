#!/bin/bash
#SBATCH --job-name=pifs-submit
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=00:30:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# FailureSpot on Pi0.5 (Fahad, Oct 31), started by t2_train_submit after the Pi0.5 report: chunks (GPU) -> convert -> its methods on both splits,
# H 50, K 8 -> report next to gru_phys and progress of results/$P/${DATA}_unseen_gru. LogpZO on GPU, the rest on CPU. DATA = natural or all.
source slurm/common.sh
source slurm/t2_fail.sh
L=results/$P/${DATA}_unseen_gru/per_episode.json
F=$(bash slurm/gpu_free.sh)
C=$(sbatch --parsable --array=0-9%$F --export=ALL,PNR_POLICY=$P slurm/pifs_chunks.sbatch) || exit 1
V=$(sbatch --parsable -p reqp -q requeue --requeue -c 2 --mem 32G -t 02:00:00 -J pifs-convert -o logs/%x-%j.out --dependency=afterok:$C \
    --wrap "source slurm/common.sh; python scripts/29_fs_convert.py --policy $P --labels $L --out data/$P/failurespot.npz") || exit 1
FS="MODE_ARGS=--data data/$P/failurespot.npz --config third_party/failurespot/configs/pi0.yaml --execution_horizon 8,OUT=results/$P/failurespot"
ML="safe_mlp actprobe_mlp supervised_random_mlp failurespot_mlp"; LS="safe_lstm actprobe_lstm supervised_random_lstm failurespot_lstm"
IDS=""
for mode in own loto; do
    r=0-9; [ $mode = own ] && r=0-2
    for M in "$ML" "$LS"; do
        IDS="$IDS:$(sbatch --parsable --array=$r -J pifs-$mode --dependency=afterok:$V --export=ALL,MODE=$mode,METHODS="$M","$FS" slurm/fs_run.sbatch)"
    done
    IDS="$IDS:$(sbatch --parsable --array=$r%2 -p galhp -q gpu --gres=gpu:nvidia_l40s:1 -c 6 --no-requeue -J pifs-$mode-logpzo --dependency=afterok:$V --export=ALL,MODE=$mode,METHODS=logpzo,DEVICE=cuda,"$FS" slurm/fs_run.sbatch)"
done
sbatch --dependency=afterany$IDS --export=ALL,P=$P,DATA=$DATA slurm/pifs_report.sbatch
