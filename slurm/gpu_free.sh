#!/bin/bash
# Free GPU slots under the cap of 5 GPU jobs at once (Fahad, Oct 23): 5 minus what my galhp / gmsap jobs can run at
# once (for an array: its remaining tasks, at most its throttle). At least 1.
used=0
for J in $(squeue -h -u $USER -p galhp,gmsap -t R,PD -o "%F %r" | grep -v Held | cut -d" " -f1 | sort -u); do  # held jobs do not count
    n=$(squeue -h -r -j $J -t R,PD | wc -l)
    t=$(scontrol show job $J 2>/dev/null | grep -o 'ArrayTaskThrottle=[0-9]*' | head -1 | cut -d= -f2)
    [ -z "$t" ] || [ "$t" = 0 ] && t=$n
    used=$((used + (n < t ? n : t)))
done
free=$((5 - used)); [ $free -lt 1 ] && free=1
echo $free
