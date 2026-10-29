# Micro-event counts around t_pnr: failures vs matched successes

81 failures with t_pnr > 0 (natural + perturbed + perturbed_v2, pooled), 81 matched successes (same task and source, read at the same steps). AUROC of the per-episode mean in each window, failures = positive (above 0.5 = higher in failures); n = failures / successes with data in the window.

| signal | early (-200 to -136) | before (-64 to 0) | after (0 to +64) |
|---|---|---|---|
| contact_flicker8 | 0.47 (n 42 / 39) | 0.40 (n 81 / 70) | 0.42 (n 81 / 63) |
| grip_reopen8 | 0.53 (n 42 / 39) | 0.59 (n 81 / 70) | 0.71 (n 81 / 63) |
| jerk_spikes8 | 0.52 (n 42 / 39) | 0.53 (n 81 / 70) | 0.53 (n 81 / 63) |

Rows sorted by how far the 'before' AUROC is from 0.5. Figures: overview.png and one png per signal.
