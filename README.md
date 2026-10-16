# vla-pnr

Measures the point of no return (PNR) of OpenVLA-OFT failures on LIBERO-10 by simulator replay,
and lines it up with detector alarms and human onset labels.

Start here: `docs/SETUP.md` (VS Code + Claude Code on the MacBook; Grid later), then `docs/TODAY.md`.
Project context for Claude Code: `CLAUDE.md`.

Pipeline: `00_check_env` -> `01_collect` -> `02_replay_test` (must PASS) -> `03_pnr_scan` -> `04_analyze`.
Tests (no GPU needed): `python -m pytest -q tests`.
