# Sourced by Track 2 jobs (Fahad, Oct 31): L40S on galhp plus reqp L40S as overflow, sharing the free slots F (5 GPU job cap). Only for
# jobs that survive a preemption: scans (03_pnr_scan.py: lock per episode, temp file then rename), collection and chunks (skip finished
# episodes, whole files only), pre-checks (skip, temp file). Each prints the job ids joined by ":" for a dependency.
RQ="-p reqp -q requeue --requeue --open-mode=append --gres=gpu:nvidia_l40s:1"
split_scan() {  # name, number of targets, exports, dependency, F. Both arrays cover the list, from opposite ends.
    local a=$(( ($5 + 1) / 2 )) b=$(( $5 / 2 )) dep=${4:+--dependency=$4} A B
    A=$(sbatch --parsable -J "$1" --array=0-$(($2 - 1))%$a $dep --export="$3" slurm/t2_scan_array.sbatch) || return 1
    [ $b -lt 1 ] && { echo "$A"; return; }
    B=$(sbatch --parsable -J "$1-rq" $RQ --array=0-$(($2 - 1))%$b $dep --export="$3",REV=1 slurm/t2_scan_array.sbatch) || return 1
    echo "$A:$B"
}
split_tasks() {  # name, exports, dependency, F, script. One array task per LIBERO-10 task: even on galhp, odd on reqp.
    local a=$(( ($4 + 1) / 2 )) b=$(( $4 / 2 )) dep=${3:+--dependency=$3} A B
    if [ $b -lt 1 ]; then sbatch --parsable -J "$1" --array=0-9%$a $dep --export="$2" "$5"; return; fi
    A=$(sbatch --parsable -J "$1" --array=0,2,4,6,8%$a $dep --export="$2" "$5") || return 1
    B=$(sbatch --parsable -J "$1-rq" $RQ --array=1,3,5,7,9%$b $dep --export="$2" "$5") || return 1
    echo "$A:$B"
}
