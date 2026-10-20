# t_pnr before and after the restore fix

Old: `data/full_scans_oct18_restore/*.json` (48 scans). New: `data/full_scans/*.json` (48 scans). In both: 48 (28 failures). Only in old: none. Only in new: none.

t_pnr changed: 9 of 48. recoverable -> t_pnr: 0, t_pnr -> recoverable: 0, t_pnr moved: 9. Where both have a t_pnr, |change| median 32 steps, max 80.
Replay success counts identical at every checkpoint: 10 of 48.

| episode | recorded | old t_pnr | new t_pnr | changed | success counts |
|---|---|---|---|---|---|
| t00_e00_n0 | success | None | None |  |  |
| t00_e01_n0 | success | None | None |  | differs |
| t00_e08_n0 | failure | 0 | 0 |  |  |
| t00_e14_n0 | failure | 368 | 288 | yes | differs |
| t00_e27_n0 | failure | 0 | 0 |  |  |
| t00_e42_n0 | failure | 0 | 0 |  |  |
| t01_e00_n0 | success | None | None |  |  |
| t01_e01_n0 | success | None | None |  | differs |
| t01_e41_n0 | failure | 152 | 176 | yes | differs |
| t02_e00_n0 | success | None | None |  |  |
| t02_e01_n0 | success | None | None |  | differs |
| t02_e10_n0 | failure | 184 | 184 |  | differs |
| t03_e00_n0 | success | None | None |  | differs |
| t03_e01_n0 | success | None | None |  |  |
| t03_e37_n0 | failure | None | None |  | differs |
| t03_e43_n0 | failure | None | None |  | differs |
| t04_e00_n0 | success | None | None |  | differs |
| t04_e01_n0 | success | None | None |  |  |
| t04_e11_n0 | failure | 176 | 184 | yes | differs |
| t05_e00_n0 | success | None | None |  |  |
| t05_e01_n0 | success | None | None |  | differs |
| t06_e00_n0 | success | None | None |  | differs |
| t06_e01_n0 | success | None | None |  | differs |
| t06_e20_n0 | failure | None | None |  | differs |
| t06_e23_n0 | failure | 432 | 472 | yes | differs |
| t06_e25_n0 | failure | 392 | 464 | yes | differs |
| t06_e26_n0 | failure | 376 | 312 | yes | differs |
| t06_e27_n0 | failure | 472 | 464 | yes | differs |
| t06_e28_n0 | failure | None | None |  | differs |
| t07_e00_n0 | success | None | None |  |  |
| t07_e01_n0 | success | None | None |  | differs |
| t08_e00_n0 | success | None | None |  | differs |
| t08_e01_n0 | success | None | None |  | differs |
| t08_e04_n0 | failure | 488 | 488 |  | differs |
| t08_e06_n0 | failure | None | None |  | differs |
| t08_e08_n0 | failure | None | None |  | differs |
| t08_e11_n0 | failure | None | None |  | differs |
| t08_e12_n0 | failure | None | None |  | differs |
| t08_e20_n0 | failure | None | None |  | differs |
| t08_e27_n0 | failure | None | None |  | differs |
| t08_e30_n0 | failure | None | None |  | differs |
| t08_e38_n0 | failure | 232 | 264 | yes | differs |
| t08_e45_n0 | failure | None | None |  | differs |
| t08_e47_n0 | failure | None | None |  | differs |
| t09_e00_n0 | success | None | None |  | differs |
| t09_e01_n0 | success | None | None |  | differs |
| t09_e25_n0 | failure | 192 | 176 | yes | differs |
| t09_e34_n0 | failure | None | None |  | differs |
