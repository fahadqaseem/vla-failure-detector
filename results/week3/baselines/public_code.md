# Public code check (2026-10-30). Nothing below has been run.

## PREFAIL (arXiv 2607.16921): code is public
- Repo: https://github.com/zshanggu/PREFAIL (MIT, linked from https://zshanggu.github.io/zeyu-prefail/). I found no dataset download link.
- Model (README, model.py, dataset.py): ResNet-18 frame encoders on 2 RGB cameras plus a temporal motion encoder on `state_to_init_relative`
  (21 values per frame), Transformer fusion, risk output. Trained on a per-frame risk ramp. Reports TP / TN / FP1 (false alarm) / FP2 (late) / FN.
- It was built for non-prehensile lift-and-place on a part carrier, not for VLA policies. To run it here:
  1. Env: torch 2.6 and torchvision 0.21 are already in ~/envs/pi; add wandb 0.19.5 (imported, disabled at run time). GPU.
  2. Images: our episodes save no frames. Re-render agentview and wrist from the saved sim states at each query (one pass over 1238 episodes, GPU).
  3. Motion input: define a 21-value analogue from data/physical (goal object relative to gripper). This is our design choice, not theirs.
  4. Labels: write its per-frame `risk` from t_pnr (their ramp) or our replay risk; write the episode format in dataset.py.
  5. Add leave-one-task-out and our thresholds (it has a fixed train / val / test split and no conformal calibration in its README).

## CheckVLA (arXiv 2607.26789): no public code found
- No link in the arXiv page, full HTML or TeX source, and a GitHub name search finds nothing relevant. Absence of a link is not proof that none exists.
- It would have to be reimplemented from the paper: a frozen V-JEPA 2-AC encoder, an action-conditioned world model trained on nominal rollouts, natural
  failures and physics-perturbed episodes, a verifier with conformal calibration. It was tested with pi0.5 on RoboCasa365, not LIBERO.
- Needs frames as for PREFAIL (step 2) and pretrained V-JEPA 2 weights. Its timely recall at 5% episode false alarms is the same kind of metric as ours.

## Hide-and-Seek (arXiv 2605.30834): code announced, not released
- https://github.com/deeplearning-wisc/hide_and_seek holds only a README ("Code coming soon"). Our `hideseek` is built from the paper.
