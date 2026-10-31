# OR ensemble: actual false alarms

Did the OR ensemble stay within its budget? (Oct 31). Actual false alarms per held-out task for or_25, or_50, or_75, and, for any setting whose actual rate is within 5%, timely alarms against progress at its 5% threshold (paired bootstrap over timed failures, 10000 draws, seed 0). That comparison is chosen after seeing the rates, so it is a lead to test, not a result.

| model | target | actual false alarms | natural / perturbed | worst tasks (rate) | timely | vs progress at 5% (17 timely) |
|---|---|---|---|---|---|---|
| or_25 | 0.05 | 0.110 | 0.059 / 0.150 | t1 0.51, t6 0.10, t0 0.09 | 28 of 81 | over 5%, not compared |
| or_25 | 0.025 | 0.064 | 0.028 / 0.093 | t1 0.30, t6 0.08, t0 0.04 | 21 of 81 | over 5%, not compared |
| or_50 | 0.05 | 0.104 | 0.055 / 0.142 | t1 0.43, t6 0.12, t0 0.09 | 26 of 81 | over 5%, not compared |
| or_50 | 0.025 | 0.040 | 0.023 / 0.053 | t1 0.14, t6 0.07, t0 0.06 | 20 of 81 | +3 (-4 to +10) |
| or_75 | 0.05 | 0.081 | 0.061 / 0.097 | t1 0.22, t0 0.14, t6 0.11 | 25 of 81 | over 5%, not compared |
| or_75 | 0.025 | 0.029 | 0.025 / 0.032 | t6 0.08, t0 0.07, t1 0.06 | 17 of 81 | +0 (-6 to +6) |
