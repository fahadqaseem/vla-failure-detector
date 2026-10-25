#!/bin/bash
# Track 1 on all data (Fahad, Oct 25): physical signals for perturbed_v2 (tasks whose replay gate passed: 0, 1, 4, 7),
# then the best Track 1 models with DATA=all (refined labels), unseen (headline) and seen -> report (pushed).
# bash slurm/t1_all_submit.sh   (CPU only)
set -e
sub() { sbatch --parsable "$@"; }
EPS=""; for d in data/perturbed_v2/task*; do [ -f $d/GATE_PASS ] && EPS="$EPS '$d/*.npz'"; done
X=$(sub -p mdtp -q primary -c 2 --mem 16G -t 12:00:00 -J t1all-physical -o logs/%x-%j.out --mail-type=FAIL --mail-user=hr4625@wayne.edu \
    --wrap "source slurm/common.sh; python scripts/20_physical_signals.py --episodes $EPS --out data/physical")
A="--phys data/physical --alphas 0.025 0.05 0.10 0.20"
M_gru="progress gru_phys gru_physvla gru_phys_cusum gru_physvla_cusum"
M_conv="progress conv_phys conv_physvla conv_physall conv_phys_cusum conv_physvla_cusum conv_physall_cusum"
IDS=""
for arch in gru conv; do
    M=M_$arch
    IDS="$IDS:$(sub --dependency=afterok:$X -J t1all-unseen-$arch --export=ALL,DATA=all,NAME=T1all_unseen_$arch,ARGS="$A --models ${!M}" slurm/w2_train.sbatch)"
    IDS="$IDS:$(sub --dependency=afterok:$X -J t1all-seen-$arch --export=ALL,DATA=all,NAME=T1all_seen_$arch,ARGS="$A --split episode --models ${!M}" slurm/w2_train.sbatch)"
done
R=$(sub --dependency=afterok$IDS --export=ALL,PHASE=T1ALL slurm/w2_report.sbatch)
echo "T1all: physical $X train ${IDS#:} report $R"
echo "$(date +%F) T1all $X ${IDS//:/ } $R" >> results/week2/jobs.txt
