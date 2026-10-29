# Sourced by Track 2 jobs (Fahad, Oct 28): if the job exits non-zero, append a 3-line note (job, time, error) to
# results/$P/BLOCKED.md and push. Jobs killed by Slurm (time limit, out of memory) cannot run this.
T2_POL=${P:-$PNR_POLICY}
t2_fail() {
    rc=$?; [ $rc = 0 ] && return
    LOGF=$(scontrol show job $SLURM_JOB_ID | grep -o 'StdOut=[^ ]*' | cut -d= -f2)
    [ -f "$LOGF" ] || LOGF=logs/$SLURM_JOB_NAME-$SLURM_JOB_ID.out
    ERR=$(grep -E 'Error|error:|Exception|Traceback|FAILED|not found' "$LOGF" 2>/dev/null | grep -vE "^ *(File|raise|ret)" | grep -vE 'EGL|Exception ignored|[Ww]arn' | tail -1 | cut -c1-300)
    mkdir -p results/$T2_POL
    ID=${SLURM_ARRAY_JOB_ID:+${SLURM_ARRAY_JOB_ID}_$SLURM_ARRAY_TASK_ID}
    { echo "- job $SLURM_JOB_NAME ${ID:-$SLURM_JOB_ID} (exit $rc), log $LOGF"
      echo "  time $(date '+%F %H:%M')"
      echo "  error: ${ERR:-see log}"; } >> results/$T2_POL/BLOCKED.md
    bash slurm/w2_push.sh "$T2_POL: job $SLURM_JOB_ID failed"
}
trap t2_fail EXIT
