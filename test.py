import gymnasium as gym
from infrastructure.expert import Expert
from 
import random, torch

env = gym.make("CartPole-v1")

# 获取专家数据
expert = Expert()
expert_data = expert.get_data(batch_size=1000)

# 将数据 load 进 replay_buffer

# BC 训练一次就可以了, 所以外层循环就不写了
opt_tim = 100
for _ in range(opt_tim):
    pass

env.close()