import gymnasium as gym
from stable_baselines3 import PPO

class Expert:
    def __init__(self, ENV_NAME):
        self.env = gym.make(ENV_NAME)
        self.model = PPO('MlpPolicy', self.env, verbose=0)
        self.model.learn(total_timesteps=10000)  # 训练模型

    def expert_policy(self, state):
        action, _ = self.model.predict(state)
        return action

    def get_data(self, batch_size=100):
        state_action_pairs = []
        while len(state_action_pairs) < batch_size:
            state, _ = self.env.reset()
            done = False
            while not done and len(state_action_pairs) < batch_size:
                action = self.expert_policy(state)
                next_state, reward, done, truncated, _ = self.env.step(action)
                state_action_pairs.append((state, action))
                state = next_state
        return state_action_pairs

if __name__ == "__main__":
    expert = Expert()
    data = expert.get_data(batch_size=100)