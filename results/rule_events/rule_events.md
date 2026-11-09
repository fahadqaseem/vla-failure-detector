# t_pnr vs the first visible failure event

Rule vs first visible failure (Fahad, Nov 7, item 3): for every failure with t_pnr > 0 under a rule, t_pnr minus the step of the first 07_auto_onset.py event among missed grasp, stuck and drop. Failure type = that first event's type ("none" = no such event). Median and 25 to 75% per rule and type, both policies. Negative = t_pnr comes before the event is visible.

| policy | rule | failure type | failures | median t_pnr - event (steps) | 25 to 75% | t_pnr before the event |
|---|---|---|---|---|---|---|
| OpenVLA-OFT | 50% (labels in use) | missed_grasp | 44 | -56 | -122 to +34 | 28 of 44 |
| OpenVLA-OFT | 50% (labels in use) | stuck | 27 | +0 | -140 to +96 | 13 of 27 |
| OpenVLA-OFT | 50% (labels in use) | drop | 7 | -48 | -56 to -40 | 7 of 7 |
| OpenVLA-OFT | 50% (labels in use) | none | 3 | n/a | n/a | n/a |
| OpenVLA-OFT | 70% (3 of 4 fail) | missed_grasp | 47 | +0 | -56 to +100 | 22 of 47 |
| OpenVLA-OFT | 70% (3 of 4 fail) | stuck | 32 | +24 | -138 to +118 | 13 of 32 |
| OpenVLA-OFT | 70% (3 of 4 fail) | drop | 8 | -24 | -40 to -10 | 6 of 8 |
| OpenVLA-OFT | 70% (3 of 4 fail) | none | 4 | n/a | n/a | n/a |
| OpenVLA-OFT | 80% (4 of 4 fail) | missed_grasp | 57 | +8 | -32 to +120 | 25 of 57 |
| OpenVLA-OFT | 80% (4 of 4 fail) | stuck | 32 | +24 | -138 to +186 | 13 of 32 |
| OpenVLA-OFT | 80% (4 of 4 fail) | drop | 9 | -8 | -24 to +56 | 5 of 9 |
| OpenVLA-OFT | 80% (4 of 4 fail) | none | 4 | n/a | n/a | n/a |
| Pi0.5 | 50% (labels in use) | missed_grasp | 10 | +80 | +10 to +240 | 1 of 10 |
| Pi0.5 | 50% (labels in use) | stuck | 17 | -112 | -168 to +0 | 12 of 17 |
| Pi0.5 | 70% (3 of 4 fail) | missed_grasp | 13 | +120 | +40 to +304 | 1 of 13 |
| Pi0.5 | 70% (3 of 4 fail) | stuck | 18 | -40 | -118 to +122 | 10 of 18 |
| Pi0.5 | 80% (4 of 4 fail) | missed_grasp | 13 | +192 | +48 to +392 | 0 of 13 |
| Pi0.5 | 80% (4 of 4 fail) | stuck | 20 | +68 | -66 to +152 | 7 of 20 |
