import gymnasium as gym
from infrastructure.expert import pytorch_util as ptu
from infrastructure.expert import Expert
from infrastructure.replay_buffer import ReplayBuffer
from policies.MLP_policy import MLPPolicy

# 设置 device
# TODO
ptu.init_gpu(use_gpu=True, gpu_id=0)

# 设置环境
ENV_NAME = "CartPole-v1"
env = gym.make(ENV_NAME)

# 获取专家数据
expert = Expert(ENV_NAME)
expert_data = expert.get_data(batch_size=1000)

# 将数据 load 进 replay_buffer
replay_buffer = ReplayBuffer()
for state, action in expert_data:
    # TODO
    replay_buffer.add(state, action)

# 初始化 policy
# TODO
actor = MLPPolicy()

# BC 训练一次就可以了, 所以外层循环就不写了
OPT_TIM = 100
for _ in range(OPT_TIM):
    # 采样

    # gradient descent
    pass

env.close()