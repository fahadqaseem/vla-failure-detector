# Patterns at t_pnr

Patterns at t_pnr (Prof. Zhu meeting, Oct 30). Timed failures are split by 07_auto_onset.py events: type = first event at or after t_pnr (none = silent). A second table uses the first event of the whole run. Signals from data/physical over the goal objects used by the task: gripper distance = smallest distance, tilt = largest tilt, contact = any contact (articulation slot included), median and 25 to 75% per step relative to t_pnr, -200 to +100, 8-step queries. First contact = first query with contact: compared with t_pnr at 50, 70, 80%; contact is sampled every 8 steps, so a touch between queries is not seen. Writes clip_ids.txt for 36_pnr_clips.py (fixed rule: round robin over the types, lowest id first, 10 ids).

Failure threshold 50%. Natural + perturbed pooled.

| type | first event at or after t_pnr | first event of the run | median t_pnr | median event - t_pnr |
|---|---|---|---|---|
| missed_grasp | 50 | 49 | 124 | +64 |
| drop | 2 | 2 | 52 | +48 |
| stuck | 17 | 27 | 144 | +120 |
| wrong_object | 0 | 0 | 0 | none |
| none | 12 | 3 | 376 | none |

## First contact with a goal object vs t_pnr (timed failures of each threshold)

| threshold | type (50% split) | before t_pnr | at or after t_pnr | never | median contact - t_pnr |
|---|---|---|---|---|---|
| 50% | missed_grasp | 32 | 16 | 2 | -72 |
| 50% | drop | 0 | 2 | 0 | +0 |
| 50% | stuck | 11 | 6 | 0 | -72 |
| 50% | none | 11 | 1 | 0 | -264 |
| 50% | all | 54 | 25 | 2 | -80 |
| 70% | missed_grasp | 41 | 7 | 2 | -152 |
| 70% | drop | 2 | 0 | 0 | -52 |
| 70% | stuck | 16 | 1 | 0 | -104 |
| 70% | none | 8 | 0 | 0 | -196 |
| 70% | all | 72 | 13 | 6 | -128 |
| 80% | missed_grasp | 39 | 6 | 2 | -176 |
| 80% | drop | 2 | 0 | 0 | -88 |
| 80% | stuck | 16 | 1 | 0 | -120 |
| 80% | none | 7 | 0 | 0 | -168 |
| 80% | all | 72 | 17 | 13 | -144 |
