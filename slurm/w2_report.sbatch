#!/bin/bash
#SBATCH --job-name=w2-report
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --time=02:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Week 2 report for PHASE = C, B or D: tables into results/week2/, one LOG.md row, commit and push.
source slurm/common.sh
W=results/week2
C=$(git rev-parse --short HEAD)
log() { echo "| $(date +%F) | $1 | $C | $2 | written by job $SLURM_JOB_ID (auto) |" >> results/LOG.md; }
case $PHASE in
C)
    for k in "fixed 0.05" "fixed 0.10" "fixed 0.20"; do
        python scripts/13_report.py --pred $W/C_unseen_rescue $W/C_unseen_memory --key "$k" --out "$W/C_unseen_report_${k// /_}.md"
        python scripts/13_report.py --pred $W/C_seen_rescue $W/C_seen_memory --key "$k" --out "$W/C_seen_report_${k// /_}.md"
        python scripts/13_report.py --pred $W/C_drift_natural $W/C_drift_pooled --key "$k" --out "$W/C_drift_report_${k// /_}.md"
    done
    python scripts/17_pick_best.py --pred $W/C_unseen_rescue $W/C_unseen_memory --out $W/C_best.md > $W/C_best.txt
    log "Phase C report: 13_report.py on $W/C_*; 17_pick_best.py -> $(cat $W/C_best.txt)" "$W/C_unseen_report_fixed_0.05.md, C_seen_report_*, C_drift_report_*, C_best.md"
    ;;
B)
    python scripts/16_lookahead_alarm.py --la data/week2_lookahead --risk data/week2_lookahead_mlp --out $W/B_lookahead
    python scripts/13_report.py --pred $W/B_lookahead --key "fixed 0.05" --out $W/B_report_fixed_0.05.md
    log "Phase B report (UPPER BOUND, simulator at test time): 16_lookahead_alarm.py, 13_report.py" "$W/B_report_fixed_0.05.md"
    ;;
D)
    python scripts/19_completeness.py --out $W/D_completeness.md
    for k in "fixed 0.05" "fixed 0.10" "fixed 0.20"; do
        python scripts/13_report.py --pred $W/D_unseen $( [ -d $W/B_lookahead ] && echo $W/B_lookahead ) --key "$k" --out "$W/D_unseen_report_${k// /_}.md"
        python scripts/13_report.py --pred $W/D_seen --key "$k" --out "$W/D_seen_report_${k// /_}.md"
        for f in "$W/D_unseen_report_${k// /_}.md" "$W/D_seen_report_${k// /_}.md"; do  # completeness at the top
            cat $W/D_completeness.md "$f" > "$f.tmp" && mv "$f.tmp" "$f"
        done
    done
    python scripts/18_refine_changes.py --scans "data/full_scans/*.json" "data/perturbed_scans/*.json" \
        "data/perturbed_v2_scans/*.json" --refine data/week2_refine --out $W/refine_changes.md
    log "Phase D report: 13_report.py on $W/D_unseen (+ B_lookahead row, UPPER BOUND) and $W/D_seen" "$W/D_unseen_report_fixed_0.05.md (headline), D_seen_report_*"
    ;;
T1)
    P="$W/T1_unseen_mlp $W/T1_unseen_gru $W/T1_unseen_conv"; Q="$W/T1_seen_mlp $W/T1_seen_gru $W/T1_seen_conv"
    for k in "fixed 0.05" "fixed 0.025"; do
        python scripts/13_report.py --pred $P --key "$k" --headline "fixed 0.05" "fixed 0.025" --out "$W/T1_unseen_report_${k// /_}.md"
        python scripts/13_report.py --pred $Q --key "$k" --headline "fixed 0.05" "fixed 0.025" --out "$W/T1_seen_report_${k// /_}.md"
    done
    log "Track 1 report (physical signals): 13_report.py --headline on $W/T1_*" "$W/T1_unseen_report_fixed_0.05.md (headline), T1_unseen_report_fixed_0.025.md, T1_seen_report_*, physical_signals/summary.md"
    ;;
PLOT)
    python scripts/21_plot_physical.py --phys data/physical --out $W/physical_signals
    log "Track 1 visual check: 20_physical_signals.py -> data/physical; 21_plot_physical.py" "$W/physical_signals/summary.md, overview.png, one png per signal"
    ;;
esac
bash slurm/w2_push.sh "week2: phase $PHASE report"
