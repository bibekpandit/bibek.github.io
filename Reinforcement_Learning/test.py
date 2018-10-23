import gym
import numpy as np
env = gym.make("FrozenLake-v0")
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())
