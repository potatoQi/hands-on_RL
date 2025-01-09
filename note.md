需要安装的东西如下，直接 pip 即可：
> tqdm  
> matplotlib  
> gymnasium  
> gymnasium[classic-control]  
> swig  
> gymnasium[box2d]  
> stable-baselines3  

还需要安装 pytorch, 用 conda 安装：
> conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

[stable-baselines3](https://stable-baselines3.readthedocs.io/en/master/)是 RL 算法的集成库, 方便自己写的算法与 baselines 进行比较

## 环境介绍
- 官方文档：[链接](https://gymnasium.farama.org/)
- Classic control
  - Acrobot-v1: 双摆
  - [CartPole-v1](https://gymnasium.farama.org/environments/classic_control/cart_pole/)
  - MountaiCar-v0: 爬山车
  - MountainCarContinuous-v0: 爬山车(连续)
  - Pendulum-v1: 倒立摆
- [Box2D](https://gymnasium.farama.org/environments/box2d/)
  - BipedalWalker-v3
  - CarRacing-v3
  - [LunarLander-v3](https://gymnasium.farama.org/environments/box2d/lunar_lander/)
- [Toy Text](https://gymnasium.farama.org/environments/toy_text/)
  - [Blackjack](https://gymnasium.farama.org/environments/toy_text/blackjack/)
  - [Taxi](https://gymnasium.farama.org/environments/toy_text/taxi/)
  - [Cliff Walking](https://gymnasium.farama.org/environments/toy_text/taxi/)
  - [Frozen Lake](https://gymnasium.farama.org/environments/toy_text/taxi/)

## 核心使用
- 常用操作
```python
# 导入包
import gymnasium as gym

# 查看 gymnasium 支持的环境
gym.pprint_registry()

# 创建环境
env = gym.make('CartPole-v1')

# 创建可视化环境
env = gym.make('CartPole-v1', render_mode='human')

# 初始化环境
ob, info = env.reset(seed=42) # 返回的是一个类型为 numpy 的 observation

# 查看环境的 observation space 和 action space, 输出结果即为文档的表格中内容
print(env.observation_space)
print(env.action_space)

# 随机从 observation / action space 中采样一个 action
ob = env.obsercation_space.sample()
action = env.action_space.sample()

# 下一步(done是机器人崩溃或完成任务, truncated是达到了轨迹长度)
nxt_ob, rw, done, truncated, info = env.step(action)

# 释放资源
env.close()
```