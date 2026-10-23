#!/bin/bash
# Week 2: submit every chain at once (docs/PLAN_week2.md). Run once from the repo root: bash slurm/w2_submit.sh
# Phase C (CPU) -> C report. Phase B (GPU, 1 at a time) -> mlp scoring (CPU) -> B report.
# Phase A (GPU, 3 at a time): collection + gate -> pre-check -> scans (submitted by w2_scans_submit) ->
# K 16 refinement (w2_refine_submit) -> Phase D (w2_phase_d: training jobs -> D report). Reports push to GitHub.
set -e
mkdir -p logs results/week2/lookahead
sub() { sbatch --parsable "$@"; }
c_job() { sub -J w2-$1 --export=ALL,DATA=old,NAME=$1,ARGS="$2" slurm/w2_train.sbatch; }
C1=$(c_job C_unseen_rescue "--models progress mlp_rescue combined_rescue mlp_rescue_cusum combined_rescue_cusum")
C2=$(c_job C_unseen_memory "--models progress gru conv gru_cusum conv_cusum")
C3=$(c_job C_seen_rescue "--split episode --models progress mlp_rescue combined_rescue mlp_rescue_cusum combined_rescue_cusum")
C4=$(c_job C_seen_memory "--split episode --models progress gru conv gru_cusum conv_cusum")
C5=$(c_job C_drift_natural "--split episode --calib_source natural --models progress safe mlp combined mlp_cusum combined_cusum")
C6=$(c_job C_drift_pooled "--split episode --calib_source pooled --models progress safe mlp combined mlp_cusum combined_cusum")
CR=$(sub --dependency=afterany:$C1:$C2:$C3:$C4:$C5:$C6 --export=ALL,PHASE=C slurm/w2_report.sbatch)
python scripts/15_lookahead.py --write_targets results/week2/lookahead/targets.txt
NB=$(grep -c . results/week2/lookahead/targets.txt)
B1=$(sub --array=0-$(((NB + 9) / 10 - 1))%1 slurm/w2_lookahead.sbatch)
B2=$(sub --dependency=afterany:$B1 -J w2-B-score --export=ALL,DATA=old,NAME=B_mlp_rerun,ARGS="--models mlp --lookahead data/week2_lookahead --lookahead_out data/week2_lookahead_mlp" slurm/w2_train.sbatch)
BR=$(sub --dependency=afterok:$B2 --export=ALL,PHASE=B slurm/w2_report.sbatch)
A1=$(sub slurm/w2_collect.sbatch)
A2=$(sub --dependency=afterok:$A1 slurm/w2_precheck.sbatch)
A3=$(sub --dependency=afterok:$A2 --export=ALL,C_REPORT=$CR,B_REPORT=$BR slurm/w2_scans_submit.sbatch)
echo "C: $C1 $C2 $C3 $C4 $C5 $C6 report $CR | B: lookahead $B1 score $B2 report $BR | A: collect $A1 precheck $A2 scans-submit $A3"
echo "$(date +%F) C $C1 $C2 $C3 $C4 $C5 $C6 $CR B $B1 $B2 $BR A $A1 $A2 $A3" >> results/week2/jobs.txt
