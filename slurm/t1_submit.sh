#!/bin/bash
# Track 1 (Prof. Zhu meeting, Oct 23): physical signals -> plots (pushed) and 6 training jobs -> report (pushed).
# bash slurm/t1_submit.sh   (CPU only; does not touch Phases A to D)
set -e
sub() { sbatch --parsable "$@"; }
X=$(sub ${AFTER:+--dependency=afterok:$AFTER} -p mdtp -q primary -c 2 --mem 16G -t 12:00:00 -J t1-physical -o logs/%x-%j.out --mail-type=FAIL --mail-user=hr4625@wayne.edu \
    --wrap "source slurm/common.sh; python scripts/20_physical_signals.py --episodes 'data/natural/*/*.npz' 'data/perturbed/task0[0145678]/*.npz' --out data/physical")
PL=$(sub --dependency=afterok:$X -J t1-plot --export=ALL,PHASE=PLOT slurm/w2_report.sbatch)
A="--phys data/physical --alphas 0.025 0.05 0.10 0.20"
M_mlp="progress mlp combined mlp_cusum combined_cusum mlp_phys mlp_physvla mlp_physall mlp_phys_cusum mlp_physvla_cusum mlp_physall_cusum"
M_gru="progress gru gru_cusum gru_phys gru_physvla gru_physall gru_phys_cusum gru_physvla_cusum gru_physall_cusum"
M_conv="progress conv conv_cusum conv_phys conv_physvla conv_physall conv_phys_cusum conv_physvla_cusum conv_physall_cusum"
IDS=""
for arch in mlp gru conv; do
    M=M_$arch
    IDS="$IDS:$(sub --dependency=afterok:$X -J t1-unseen-$arch --export=ALL,DATA=old,NAME=T1_unseen_$arch,ARGS="$A --models ${!M}" slurm/w2_train.sbatch)"
    IDS="$IDS:$(sub --dependency=afterok:$X -J t1-seen-$arch --export=ALL,DATA=old,NAME=T1_seen_$arch,ARGS="$A --split episode --models ${!M}" slurm/w2_train.sbatch)"
done
R=$(sub --dependency=afterok$IDS --export=ALL,PHASE=T1 slurm/w2_report.sbatch)
echo "T1: physical $X plot $PL train ${IDS#:} report $R"
echo "$(date +%F) T1 $X $PL ${IDS//:/ } $R" >> results/week2/jobs.txt
