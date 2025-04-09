import numpy as np


class SARSA:
    def __init__(self, n_states, n_actions, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.n_actions = n_actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = np.zeros((n_states, n_actions))

    def choose_action(self, state):
        if np.random.uniform() < self.epsilon:
            return np.random.choice(self.n_actions)
        else:
            return np.argmax(self.q_table[state])

    def update(self, state, action, reward, next_state, next_action=None, done=False):
        current_q = self.q_table[state, action]
        if done:
            target = reward
        else:
            target = reward + self.gamma * self.q_table[next_state, next_action]
        self.q_table[state, action] += self.alpha * (target - current_q)


def is_valid(state, action):
    # 示例成功条件：当执行动作2时总是成功
    return action == 2


def train_sarsa(agent, episodes):
    for episode in range(episodes):
        state = 0  # 初始状态（未成功次数为0）
        count = 0
        done = False
        action = agent.choose_action(state)
        total_reward = 0

        while not done:
            # 执行动作并获取结果
            valid = is_valid(state, action)
            if valid:
                reward = 100
                next_state = None
                done = True
            else:
                count += 1
                if count >= 10:
                    reward = -100
                    next_state = None
                    done = True
                else:
                    reward = -1
                    next_state = count
                    done = False

            total_reward += reward

            # 更新Q表
            if done:
                agent.update(state, action, reward, next_state=None, done=True)
            else:
                next_action = agent.choose_action(next_state)
                agent.update(state, action, reward, next_state, next_action)
                state = next_state
                action = next_action

        # 输出训练进度
        if (episode + 1) % 100 == 0:
            print(f"Episode: {episode + 1}, Total Reward: {total_reward}")

"""
if __name__ == "__main__":
    n_states = 10  # 状态0-9（对应未成功次数）
    n_actions = 5  # 可用动作数量

    agent = SARSA(n_states, n_actions)
    train_sarsa(agent, episodes=1000)

    # 打印训练后的Q表
    print("\nTrained Q-table:")
    print(agent.q_table)

"""
