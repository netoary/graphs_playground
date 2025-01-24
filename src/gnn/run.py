from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.utils import safe_mean
from env import GraphDecompositionEnv
from sb3_contrib import MaskablePPO
import numpy as np
import time
import os

model_type = f"GNN-{int(time.time())}"
models_dir = f"models/{model_type}"
logdir = "logs"

env = GraphDecompositionEnv()

# Verificar o ambiente
check_env(env)

if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(logdir):
    os.makedirs(logdir)


# MultiInputPolicy
# MlpPolicy
# CnnPolicy
model = MaskablePPO("MlpPolicy", env, verbose=1, tensorboard_log=logdir)
# model = MaskablePPO(MaskableActorCriticPolicy, env2, verbose=1, tensorboard_log=logdir)
# model.learn(total_timesteps=145)
TIMESTEPS = 10_000
max_rew = -np.inf
for step in range(1, 1500):
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name=model_type)
    save_model = False
    ep_rew_mean = safe_mean([ep_info["r"] for ep_info in model.ep_info_buffer])
    if (ep_rew_mean > max_rew):
        save_model = True
        max_rew = ep_rew_mean
    if save_model:
        model.save(f"{models_dir}/{TIMESTEPS*step}")
model.save(f"{models_dir}/{TIMESTEPS*step+1}")

# Testar o modelo treinado
obs = env.reset()
done = False
total_reward = 0

while not done:
    action, _ = model.predict(obs)
    obs, reward, done, info = env.step(action)
    total_reward += reward
    env.render()

print(f"Recompensa total: {total_reward}")
