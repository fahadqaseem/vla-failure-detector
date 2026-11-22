# Cost plan for a 20-replay ground truth (plan: results/plan_nov22_gt20.md, Step 2)

## Time per replay, OpenVLA-OFT pilot (99 checkpoints done, 1560 new replays, galhp L40S)

| replays | n | mean seconds | median | mean steps |
|---|---|---|---|---|
| successful | 266 | 9.2 | 8.3 | 260 |
| failed | 1294 | 14.2 | 13.9 | 436 |
| all | 1560 | 13.4 | 12.7 | 406 |

Fit seconds = 1.65 + 0.0288 x replay steps (a failed replay from step c runs 720 - c steps).

## Time per replay from the existing K 4 scans (minutes per scan; fit seconds = a + b x steps)

| policy | scans | a (s per replay) | b (s per step) | failed replay from step 0 (720 steps), s | mean scan minutes |
|---|---|---|---|---|---|
| OpenVLA-OFT | 171 | 1.11 | 0.0296 | 22 | 51 |
| Pi0.5 | 82 | 0.84 | 0.0629 | 46 | 98 |

OFT projections below use the pilot fit; Pi0.5 uses its scan fit (no Pi0.5 pilot this week).

## Projected cost (5 GPUs at once, all the time; real queue waits come on top)

| policy | runs | every | design | new replays | GPU hours | days |
|---|---|---|---|---|---|---|
| OpenVLA-OFT | 136 | 8 | K 8 | 34728 | 132 | 1.1 |
| OpenVLA-OFT | 136 | 8 | K 20 | 139544 | 528 | 4.4 |
| OpenVLA-OFT | 136 | 8 | adaptive (K 20 where 0.25 <= f4 <= 0.75 or at a change) | 36312 | 137 | 1.1 |
| OpenVLA-OFT | 136 | 16 | K 8 | 17636 | 67 | 0.6 |
| OpenVLA-OFT | 136 | 16 | K 20 | 70860 | 268 | 2.2 |
| OpenVLA-OFT | 136 | 16 | adaptive (K 20 where 0.25 <= f4 <= 0.75 or at a change) | 18708 | 71 | 0.6 |
| OpenVLA-OFT | 136 | 32 | K 8 | 9124 | 34 | 0.3 |
| OpenVLA-OFT | 136 | 32 | K 20 | 36620 | 138 | 1.1 |
| OpenVLA-OFT | 136 | 32 | adaptive (K 20 where 0.25 <= f4 <= 0.75 or at a change) | 10248 | 39 | 0.3 |
| OpenVLA-OFT | 50 | 8 | K 8 | 12736 | 48 | 0.4 |
| OpenVLA-OFT | 50 | 8 | K 20 | 51208 | 192 | 1.6 |
| OpenVLA-OFT | 50 | 8 | adaptive (K 20 where 0.25 <= f4 <= 0.75 or at a change) | 16104 | 60 | 0.5 |
| OpenVLA-OFT | 50 | 16 | K 8 | 6468 | 24 | 0.2 |
| OpenVLA-OFT | 50 | 16 | K 20 | 26004 | 97 | 0.8 |
| OpenVLA-OFT | 50 | 16 | adaptive (K 20 where 0.25 <= f4 <= 0.75 or at a change) | 8244 | 31 | 0.3 |
| OpenVLA-OFT | 50 | 32 | K 8 | 3344 | 12 | 0.1 |
| OpenVLA-OFT | 50 | 32 | K 20 | 13432 | 50 | 0.4 |
| OpenVLA-OFT | 50 | 32 | adaptive (K 20 where 0.25 <= f4 <= 0.75 or at a change) | 4664 | 17 | 0.1 |
| Pi0.5 | 37 | 8 | K 8 | 9620 | 68 | 0.6 |
| Pi0.5 | 37 | 8 | K 20 | 38480 | 273 | 2.3 |
| Pi0.5 | 37 | 8 | adaptive (K 20 where 0.25 <= f4 <= 0.75 or at a change) | 12608 | 89 | 0.7 |
| Pi0.5 | 37 | 16 | K 8 | 4884 | 35 | 0.3 |
| Pi0.5 | 37 | 16 | K 20 | 19536 | 139 | 1.2 |
| Pi0.5 | 37 | 16 | adaptive (K 20 where 0.25 <= f4 <= 0.75 or at a change) | 6656 | 47 | 0.4 |
| Pi0.5 | 37 | 32 | K 8 | 2516 | 18 | 0.1 |
| Pi0.5 | 37 | 32 | K 20 | 10064 | 71 | 0.6 |
| Pi0.5 | 37 | 32 | adaptive (K 20 where 0.25 <= f4 <= 0.75 or at a change) | 3520 | 25 | 0.2 |

## Recommendation

Largest design within about 10 days on 5 GPUs (preference: K 20 everywhere, then adaptive, then K 8; then more runs; then a finer grid; Pi0.5 with the same design): OpenVLA-OFT 136 runs, every 8, K 20: 528 GPU h (4.4 days) + Pi0.5 37 runs: 273 GPU h (2.3 days) = 6.7 days.
