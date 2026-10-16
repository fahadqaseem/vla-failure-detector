# Results log

Every number shown in a meeting must trace to a line here.

| date | command | commit | output | notes |
|---|---|---|---|---|
| 2026-10-16 | setup per docs/SETUP.md step 2 (Miniforge via brew, env `openvla-oft`, py3.10) | 0b39156 | imports ok, `pip check` clean, `pytest -q tests`: 6 passed | openvla-oft e4287e9. Deviations from SETUP: LIBERO needed `pip install -e . --config-settings editable_mode=compat` (plain -e was not importable); pinned numpy==1.26.4 and opencv-python==4.10.0.84 (opencv 5 forced numpy 2, tensorflow-macos 2.15 needs numpy<2). Blocker: openvla-oft pins torch 2.2.0, which raises "BFloat16 is not supported on MPS". torch 2.3.1 does bf16 matmul on MPS (scratch test). |
| 2026-10-16 | `pip install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1` | 0b39156 | bf16 matmul on MPS ok | Fahad chose upgrade over float16 to keep bf16 numerics. Deliberately breaks openvla-oft's torch==2.2.0 pin (only `pip check` complaint). |
| 2026-10-16 | `pip install "protobuf>=4.21.6,<5" "tensorflow-metadata>=1.15,<1.21" "wandb<0.19"` | 0b39156 | `import pnr.sim` ok: device mps, chunk 8 | tensorflow-metadata 1.21 needed protobuf 5 (breaks tf 2.15). Now protobuf 4.25.9, tensorflow-metadata 1.17.3, wandb 0.18.7. Added chunk==8 assert to pnr/sim.py. |
| 2026-10-16 | `python scripts/00_check_env.py` (attempt 1) | 0b39156 | FAIL in robosuite `get_joint_qpos_addr` AssertionError | mujoco 3.16.0 was pulled in (robosuite 1.4.1 does not pin it). Fixed with `pip install mujoco==2.3.7`; LIBERO task 0 env then builds (50 init states, sim state dim 123). |
| 2026-10-16 | `python scripts/00_check_env.py` (attempt 3) | 0b39156 + uncommitted pnr/sim.py | OK. policy device mps, loaded in 13s, 40-step dry run 26.8s (5 queries: 0,8,16,24,32), sim state dim 123 | Attempt 2 failed: proprio projector saved on CUDA; added torch.load map_location=cpu default in pnr/sim.py (no CUDA only). Memory, sampled every 15s: swap 3.4 GB at start, peak 7.0 GB during load, 4.2 GB at end; free memory fell to 20%. Over the "few GB swap" line in CLAUDE.md, so paused for Fahad. |
