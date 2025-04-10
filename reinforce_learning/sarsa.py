import os

import numpy as np

from actions.action_create_fake_signature import action_create_fake_signature
from actions.action_insert_useless_data_to_end import action_insert_useless_data_to_end
from actions.action_modify_checksum import action_modify_checksum
from actions.action_modify_timestamp import action_modify_timestamp
from operation_modules.findAllSignatures import get_all_file_paths
from string_generator.generated_strings.strings_length_4096 import strings_4096bytes
from virus_scanner_module.clamScanner import clamScanner


class SARSA:
    def __init__(self,actions_list,n_states, n_actions, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.actions_list = actions_list
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




# 训练sarsa 模型 episodes为文件列表
def train_sarsa(agent, train_dataset_dir,enable_log_):
    episodes = get_all_file_paths(target_dir=train_dataset_dir)
    for episode in episodes:
        state = 0  # 初始状态（未成功次数为0）
        count = 0
        done = False

        action = agent.choose_action(state)
        action_name = agent.actions[action]
        if action_name == "action_create_fake_signature":
            action_create_fake_signature(input_file_=episode,
                                         enable_log=enable_log_)
        elif action_name == "action_insert_useless_data_to_end":
            action_insert_useless_data_to_end(input_file_=episode,
                                              string_list_=strings_4096bytes,
                                              enable_log=enable_log_)
        elif action_name == "action_modify_checksum":
            action_modify_checksum(input_file_=episode,new_checksum_=None,enable_log=enable_log_)
        elif action_name == "action_modify_timestamp":
            action_modify_timestamp(input_file_=episode,enable_log=enable_log_,new_timestamp_=None)




        total_reward = 0
        origin_file_size = os.path.getsize(episode)
        while not done:
            valid = True
            # 执行动作并获取结果
            # clamScanner反病毒软件扫描
            if clamScanner(episode):
                valid=False
            elif not clamScanner(episode):
                valid = True
            if valid:
                reward = 100
                now_file_size = os.path.getsize(episode)
                discount = np.log(now_file_size/origin_file_size)
                reward = reward/((1/3)*discount+1)
                print("episode:"+os.path.basename(episode)+" reward:"+str(reward))
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
