#!/bin/bash
#SBATCH --job-name=t2-train-submit
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=00:30:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Track 2 for $P after the scans: physical signals, then the Track 1 models (unseen and seen, mlp / gru / conv),
# natural only and, if perturbed episodes exist, natural + perturbed; report. After pi0, start the pi05 chain.
source slurm/common.sh
X=$(sbatch --parsable -p mdtp -q primary -c 2 --mem 16G -t 12:00:00 -J t2-physical-$P -o logs/%x-%j.out     --wrap "source slurm/common.sh; python scripts/20_physical_signals.py --episodes 'data/$P/natural/*/*.npz' 'data/$P/perturbed/*/*.npz' --out data/$P/physical")
A="--phys data/$P/physical --alphas 0.025 0.05 0.10 0.20"
M_mlp="progress mlp combined mlp_cusum combined_cusum mlp_phys mlp_physvla mlp_physall mlp_phys_cusum mlp_physvla_cusum mlp_physall_cusum"
M_gru="progress gru gru_cusum gru_phys gru_physvla gru_physall gru_phys_cusum gru_physvla_cusum gru_physall_cusum"
M_conv="progress conv conv_cusum conv_phys conv_physvla conv_physall conv_phys_cusum conv_physvla_cusum conv_physall_cusum"
SETS="natural"; ls data/$P/perturbed_scans/*.json >/dev/null 2>&1 && SETS="natural all"
IDS=""
for D in $SETS; do for split in unseen seen; do for arch in mlp gru conv; do
    M=M_$arch; SP=""; [ $split = seen ] && SP="--split episode"
    IDS="$IDS:$(sbatch --parsable --dependency=afterok:$X -J t2-$P-$D-$split-$arch --export=ALL,P=$P,DATA=$D,NAME=${D}_${split}_$arch,ARGS="$A $SP --models ${!M}" slurm/t2_train.sbatch)"
done; done; done
sbatch --dependency=afterok$IDS --export=ALL,PHASE=PI,P=$P,SETS="$SETS" slurm/w2_report.sbatch
[ "$P" = pi0 ] && bash slurm/t2_start.sh pi05
true
