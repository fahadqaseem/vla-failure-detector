"""Pi0 / Pi0.5 + LIBERO, with the same interface as pnr/sim.py (Track 2, Oct 23 2026). Select with PNR_POLICY=pi0 or
PNR_POLICY=pi05 (pnr/policy.py); runs in the separate env ~/envs/pi (slurm/t2_env.sbatch, slurm/common_pi.sh).

Policy: the LeRobot PyTorch ports lerobot/pi0_libero_finetuned_v044 and lerobot/pi05_libero_finetuned_v044 (LIBERO
fine-tuned, from the openpi checkpoints). Observation and action processing are LeRobot's own, as in lerobot-eval:
LiberoEnv._format_raw_obs -> preprocess_observation -> LiberoProcessorStep (images rotated 180 deg, state = eef pos,
axis-angle, gripper qpos) -> the checkpoint's preprocessor; actions -> the checkpoint's postprocessor -> env.step.
Differences from lerobot-eval (decided Oct 23, so checkpoints sit at query boundaries every 8 steps as for OFT):
  - the policy is re-queried every 8 steps (n_action_steps 8 instead of 50; the model still predicts 50);
  - the flow matching noise is seeded at every query from (flow_seed, step), so a replay with the episode's own
    flow_seed reproduces it (replay gate) and a replay with a new flow_seed is a new sample of the policy (scans).
Features (SAFE, Gu et al. 2025, App. B.1, for pi0: last layer, the vectors before the velocity-field projection):
the input of action_out_proj at each of the 10 flow steps, mean over the 50 chunk positions -> (10, width) per query;
features_mean = mean over the flow steps.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import List, Optional

import numpy as np
import torch
from libero.libero import benchmark
from lerobot.envs.libero import LiberoEnv, get_libero_dummy_action
from lerobot.envs.utils import preprocess_observation
from lerobot.policies.factory import make_pre_post_processors
from lerobot.processor import PolicyProcessorPipeline
from lerobot.processor.env_processor import LiberoProcessorStep

KIND = os.environ.get("PNR_POLICY", "pi0")
CHECKPOINT = {"pi0": "lerobot/pi0_libero_finetuned_v044", "pi05": "lerobot/pi05_libero_finetuned_v044"}[KIND]
SUITE = "libero_10"
CHUNK = 8
WAIT_STEPS = 10
MAX_STEPS = 520  # lerobot TASK_SUITE_MAX_STEPS["libero_10"], same as openvla-oft
DETERMINISTIC = os.environ.get("PNR_DETERMINISTIC", "1") == "1"
if DETERMINISTIC and torch.cuda.is_available():
    os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
    torch.use_deterministic_algorithms(True, warn_only=True)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
REPLAY_START = "restore_query"


class Policy:
    """Loads Pi0 / Pi0.5 once; act() returns 8 env actions per query and keeps the query's features."""

    def __init__(self):
        if KIND == "pi0":
            from lerobot.policies.pi0.modeling_pi0 import PI0Policy as Cls
        else:
            from lerobot.policies.pi05.modeling_pi05 import PI05Policy as Cls
        from lerobot.configs.policies import PreTrainedConfig
        config = PreTrainedConfig.from_pretrained(CHECKPOINT)
        config.compile_model = False  # the pi0 checkpoint sets true; torch.compile needs a gcc build that fails on Grid
        self.model = Cls.from_pretrained(CHECKPOINT, config=config).to("cuda").eval()
        self.model.config.n_action_steps = CHUNK
        self.pre, self.post = make_pre_post_processors(self.model.config, pretrained_path=CHECKPOINT)
        self.env_step = PolicyProcessorPipeline(steps=[LiberoProcessorStep()])  # as make_env_pre_post_processors
        self._flow = []  # inputs of action_out_proj during one query, one per flow step
        self.model.model.action_out_proj.register_forward_pre_hook(
            lambda mod, inp: self._flow.append(inp[0].detach().float().mean(1)[0].cpu().numpy()))
        self.last_hidden = None

    def act(self, formatted_obs, description: str, seed: int) -> list:
        obs = preprocess_observation(_batch(formatted_obs))
        obs["task"] = [description]
        obs = self.pre(self.env_step(obs))
        torch.manual_seed(seed)
        self._flow = []
        with torch.inference_mode():
            chunk = self.model.predict_action_chunk(obs)[:, :CHUNK]  # (1, 8, action dim)
        self.last_hidden = np.stack(self._flow)  # (flow steps, width)
        return [self.post(chunk[:, i]).float().cpu().numpy()[0] for i in range(CHUNK)]

    def last_features(self) -> np.ndarray:
        return self.last_hidden


def _batch(d):
    """Add the batch dimension a gym vector env would add (nested dicts of arrays)."""
    return {k: _batch(v) if isinstance(v, dict) else np.asarray(v)[None] for k, v in d.items()}


def make_task(task_id: int):
    """Returns (env, task_description, initial_states[50]). env is the raw LIBERO OffScreenRenderEnv (as in pnr/sim.py);
    env.lerobot is LeRobot's LiberoEnv around it, used only to format observations."""
    suite = benchmark.get_benchmark_dict()[SUITE]()
    wrapper = LiberoEnv(task_suite=suite, task_id=task_id, task_suite_name=SUITE, obs_type="pixels_agent_pos",
                        init_states=False)
    env = wrapper._env
    env.lerobot = wrapper
    return env, wrapper.task_description, suite.get_task_init_states(task_id)


def max_steps() -> int:
    return MAX_STEPS


@dataclass
class Rollout:
    success: bool
    t_end: int
    flow_seed: int = 0
    query_steps: List[int] = field(default_factory=list)
    query_states: List[np.ndarray] = field(default_factory=list)
    query_grippers: List[np.ndarray] = field(default_factory=list)
    actions: List[np.ndarray] = field(default_factory=list)
    eef: List[np.ndarray] = field(default_factory=list)
    features: List[np.ndarray] = field(default_factory=list)  # (flow steps, width) float16 at each query
    frames: List[np.ndarray] = field(default_factory=list)


def restore(env, state, gripper):
    """Same as pnr/sim.py restore (controller refresh + gripper counter)."""
    env.reset()
    obs = env.set_init_state(state)
    robot = env.env.robots[0]
    robot.controller.update(force=True)
    robot.gripper.current_action = np.array(gripper, dtype=np.float64).copy()
    return obs


def restore_query(env, ep, qi):
    """Same as pnr/sim.py restore_query: restore query qi - 1, replay its 8 recorded actions, put the exact state of qi
    back, so the observation is built the normal way. Objects are never moved."""
    if qi == 0:
        env.reset()
        obs = env.set_init_state(ep["init_state"])
        for _ in range(WAIT_STEPS):
            obs, _, _, _ = env.step(get_libero_dummy_action())
        return obs
    restore(env, ep["query_states"][qi - 1], ep["query_grippers"][qi - 1])
    for t in range(int(ep["query_steps"][qi - 1]), int(ep["query_steps"][qi])):
        obs, _, _, _ = env.step(ep["actions"][t].tolist())
    e = env.env
    e.sim.set_state_from_flattened(ep["query_states"][qi])
    e.sim.forward()
    e.robots[0].controller.update(force=True)
    e.robots[0].gripper.current_action = np.array(ep["query_grippers"][qi], dtype=np.float64).copy()
    return obs


def query_seed(flow_seed: int, step: int) -> int:
    return int(np.random.SeedSequence([flow_seed, step]).generate_state(1)[0])


def rollout(env, policy: Policy, description: str, *, init_state=None, episode=None, query: Optional[int] = None,
            noise_std: float = 0.0, rng: Optional[np.random.Generator] = None,
            record_states: bool = True, save_frames: bool = False, limit: Optional[int] = None,
            horizon: Optional[int] = None) -> Rollout:
    """As pnr/sim.py rollout. Randomness = the flow matching noise: flow_seed comes from rng, or, for a replay without
    rng (replay gate), from the recorded episode, which then reproduces it. noise_std > 0 adds action noise as for OFT
    (only if replays turn out identical; Oct 23)."""
    assert (init_state is None) != (episode is None), "pass exactly one of init_state / episode"
    if rng is None and episode is not None:
        flow_seed = int(episode["flow_seed"])
    else:
        rng = rng or np.random.default_rng()
        flow_seed = int(rng.integers(2 ** 31))
    if episode is not None:
        raw = restore_query(env, episode, query)
        t = int(episode["query_steps"][query])
    else:
        env.reset()
        raw = env.set_init_state(init_state)
        for _ in range(WAIT_STEPS):
            raw, _, _, _ = env.step(get_libero_dummy_action())
        t = 0
    out = Rollout(success=False, t_end=t, flow_seed=flow_seed)
    queue: list = []
    end = MAX_STEPS if horizon is None else horizon
    stop_at = end if limit is None else min(end, t + limit)
    while t < stop_at:
        if not queue:
            if record_states:
                out.query_steps.append(t)
                out.query_states.append(env.get_sim_state().copy())
                out.query_grippers.append(np.array(env.env.robots[0].gripper.current_action, dtype=np.float64))
            queue = policy.act(env.lerobot._format_raw_obs(raw), description, query_seed(flow_seed, t))
            if record_states:
                out.features.append(policy.last_features().astype(np.float16))
        action = np.array(queue.pop(0), dtype=np.float64)
        if noise_std > 0:
            action[:6] = np.clip(action[:6] + rng.normal(0.0, noise_std, size=6), -1.0, 1.0)
        raw, _, done, _ = env.step(action.tolist())
        t += 1
        out.actions.append(action.copy())
        out.eef.append(np.array(raw["robot0_eef_pos"], dtype=np.float64))
        if save_frames:
            out.frames.append(raw["agentview_image"][::-1, ::-1].copy())
        if done or env.check_success():
            out.success = True
            break
    out.t_end = t
    return out


def save_episode(path: str, r: Rollout, *, task_id: int, episode_idx: int, description: str,
                 init_state, noise_std: float, seed: int, **extra) -> None:
    """Same fields as pnr/sim.py save_episode, plus flow_seed and the policy name."""
    feats = np.stack(r.features) if r.features else np.zeros((0, 10, 1024), dtype=np.float16)
    np.savez_compressed(
        path, **extra, policy=KIND, checkpoint=CHECKPOINT, flow_seed=r.flow_seed,
        task_id=task_id, episode_idx=episode_idx, description=description,
        success=r.success, t_end=r.t_end, noise_std=noise_std, seed=seed, induced=bool(noise_std > 0),
        init_state=np.asarray(init_state),
        query_steps=np.asarray(r.query_steps, dtype=np.int64),
        query_states=np.stack(r.query_states) if r.query_states else np.zeros((0,)),
        query_grippers=np.stack(r.query_grippers) if r.query_grippers else np.zeros((0, 2)),
        actions=np.stack(r.actions) if r.actions else np.zeros((0, 7)),
        eef=np.stack(r.eef) if r.eef else np.zeros((0, 3)),
        features=feats, features_mean=feats.astype(np.float32).mean(axis=1),
    )
