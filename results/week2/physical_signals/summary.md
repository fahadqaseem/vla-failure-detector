# Physical signals around t_pnr: failures vs matched successes

46 failures with t_pnr > 0 (natural + perturbed, 7 of 10 tasks, pooled), 46 matched successes (same task and source, read at the same steps). AUROC of the per-episode mean in each window, failures = positive (above 0.5 = higher in failures); n = failures / successes with data in the window.

| signal | early (-200 to -136) | before (-64 to 0) | after (0 to +64) |
|---|---|---|---|
| obj1_dist | 0.45 (n 31 / 27) | 0.35 (n 46 / 35) | 0.44 (n 46 / 33) |
| obj1_tilt | 0.54 (n 31 / 27) | 0.64 (n 46 / 35) | 0.69 (n 46 / 33) |
| obj1_contact | 0.55 (n 31 / 27) | 0.61 (n 46 / 35) | 0.52 (n 46 / 33) |
| obj1_pos_x | 0.53 (n 31 / 27) | 0.58 (n 46 / 35) | 0.54 (n 46 / 33) |
| eef_x | 0.59 (n 31 / 27) | 0.57 (n 46 / 35) | 0.60 (n 46 / 33) |
| eef_z | 0.44 (n 31 / 27) | 0.43 (n 46 / 35) | 0.42 (n 46 / 33) |
| obj1_in_goal | 0.44 (n 31 / 27) | 0.44 (n 46 / 35) | 0.37 (n 46 / 33) |
| obj1_dz | 0.47 (n 31 / 27) | 0.56 (n 46 / 35) | 0.42 (n 46 / 33) |
| obj1_lifted | 0.46 (n 31 / 27) | 0.55 (n 46 / 35) | 0.43 (n 46 / 33) |
| obj1_pos_z | 0.50 (n 31 / 27) | 0.55 (n 46 / 35) | 0.50 (n 46 / 33) |
| obj2_lifted | 0.46 (n 31 / 27) | 0.46 (n 46 / 35) | 0.34 (n 46 / 33) |
| obj2_pos_z | 0.50 (n 31 / 27) | 0.54 (n 46 / 35) | 0.44 (n 46 / 33) |
| obj1_pos_y | 0.51 (n 31 / 27) | 0.54 (n 46 / 35) | 0.55 (n 46 / 33) |
| obj1_goal_dist | 0.53 (n 31 / 27) | 0.54 (n 46 / 35) | 0.56 (n 46 / 33) |
| grip_open | 0.49 (n 31 / 27) | 0.47 (n 46 / 35) | 0.58 (n 46 / 33) |
| obj2_pos_x | 0.53 (n 31 / 27) | 0.53 (n 46 / 35) | 0.49 (n 46 / 33) |
| obj2_ddist | 0.62 (n 31 / 27) | 0.53 (n 46 / 35) | 0.54 (n 46 / 33) |
| eef_y | 0.51 (n 31 / 27) | 0.52 (n 46 / 35) | 0.46 (n 46 / 33) |
| obj2_goal_dist | 0.49 (n 31 / 27) | 0.48 (n 46 / 35) | 0.51 (n 46 / 33) |
| obj2_tilt | 0.51 (n 31 / 27) | 0.52 (n 46 / 35) | 0.42 (n 46 / 33) |
| obj2_dz | 0.49 (n 31 / 27) | 0.52 (n 46 / 35) | 0.37 (n 46 / 33) |
| obj2_dist | 0.51 (n 31 / 27) | 0.48 (n 46 / 35) | 0.53 (n 46 / 33) |
| obj1_ddist | 0.53 (n 31 / 27) | 0.48 (n 46 / 35) | 0.60 (n 46 / 33) |
| art_ddist | 0.57 (n 31 / 27) | 0.48 (n 46 / 35) | 0.46 (n 46 / 33) |
| art_contact | nan (n 31 / 27) | 0.49 (n 46 / 35) | 0.51 (n 46 / 33) |
| obj2_contact | 0.49 (n 31 / 27) | 0.49 (n 46 / 35) | 0.42 (n 46 / 33) |
| obj2_pos_y | 0.52 (n 31 / 27) | 0.49 (n 46 / 35) | 0.43 (n 46 / 33) |
| art_dist | 0.49 (n 31 / 27) | 0.50 (n 46 / 35) | 0.49 (n 46 / 33) |
| art_true | 0.49 (n 31 / 27) | 0.50 (n 46 / 35) | 0.50 (n 46 / 33) |
| obj2_in_goal | 0.50 (n 31 / 27) | 0.50 (n 46 / 35) | 0.50 (n 46 / 33) |

Rows sorted by how far the 'before' AUROC is from 0.5. Figures: overview.png and one png per signal.
