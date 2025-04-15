import logging
import os

import numpy as np

from actions.action_add_benign_data_overlay_1 import action_add_benign_data_overlay_1
from actions.action_add_bytes_to_section_cave_1 import action_add_bytes_to_section_cave_1
from actions.action_add_random_resources import action_add_random_resources
from actions.action_add_section_benign_data_1 import action_add_section_benign_data_1
from actions.action_break_optional_header_checksum_1 import action_break_optional_header_checksum_1
from actions.action_create_fake_signature import action_create_fake_signature
from actions.action_insert_useless_data_to_end import action_insert_useless_data_to_end
from actions.action_modify_checksum import action_modify_checksum
from actions.action_modify_optional_header_1 import action_modify_optional_header_1
from actions.action_modify_timestamp import action_modify_timestamp
from actions.action_modify_timestamp_1 import action_modify_timestamp_1
from actions.action_remove_debug import action_remove_debug
from actions.action_rename_random_section import action_rename_random_section
from actions.action_rename_section_1 import action_rename_section_1
from actions.action_upx_encryption import action_upx_encryption
from actions.actions_list import get_random_actions
from init.clear_directory import clear_directory
from operation_modules.findAllSignatures import get_all_file_paths
from string_generator.generated_strings.get_a_random_string_from_strings import get_random_string
from string_generator.generated_strings.strings_length_4096 import strings_4096bytes
from virus_scanner_module.clamScanner import clamScanner
logging.basicConfig(
    level=logging.DEBUG,       # 设置最低日志级别（DEBUG 及以上均输出）
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename=r"D:\graduate_design\example1\logs\sarsa_record.log",        # 输出到文件（不指定则默认输出到控制台）
    filemode="a"               # 文件写入模式（'a' 追加，'w' 覆盖）
)


def do_action(action_name,episode,enable_log_):
    if action_name == "action_create_fake_signature":
        action_create_fake_signature(input_file_=episode,
                                     enable_log=enable_log_)
    elif action_name == "action_insert_useless_data_to_end":
        action_insert_useless_data_to_end(input_file_=episode,
                                          string_list_=strings_4096bytes,
                                          enable_log=enable_log_)
    elif action_name == "action_modify_checksum":
        action_modify_checksum(input_file_=episode, new_checksum_=None, enable_log=enable_log_)
    elif action_name == "action_modify_timestamp":
        action_modify_timestamp(input_file_=episode, enable_log=enable_log_, new_timestamp_=None)
    elif action_name == "action_rename_random_section":
        action_rename_random_section(input_file_=episode, enable_log=enable_log_)
    elif action_name == "action_upx_encryption":
        action_upx_encryption(input_file_=episode, enable_log=enable_log_)
    elif action_name == "action_add_benign_data_overlay_1":
        action_add_benign_data_overlay_1(input_file_=episode,
                                         appended_data_=get_random_string(
                                             string_list=strings_4096bytes)*256,
                                         enable_log=enable_log_)
    elif action_name == "action_add_bytes_to_section_cave_1":
        action_add_bytes_to_section_cave_1(input_file_=episode, string_list_=strings_4096bytes,
                                           enable_log=enable_log_)
    elif action_name == "action_add_section_benign_data_1":
        action_add_section_benign_data_1(input_file_=episode, string_list_=strings_4096bytes,
                                         enable_log=enable_log_)
    elif action_name == "action_break_optional_header_checksum_1":
        action_break_optional_header_checksum_1(input_file_=episode, enable_log=enable_log_)
    elif action_name == "action_modify_optional_header_1":
        action_modify_optional_header_1(input_file_=episode, enable_log=enable_log_)
    elif action_name == "action_modify_timestamp_1":
        action_modify_timestamp_1(input_file_=episode, enable_log=enable_log_)
    elif action_name == "action_remove_debug":
        action_remove_debug(input_file_=episode, enable_log=enable_log_)
    elif action_name == "action_rename_section_1":
        action_rename_section_1(input_file_=episode, enable_log=enable_log_)
    elif action_name == "action_add_random_resources":
        action_add_random_resources(
            source_folder=r"D:\graduate_design\example1\operation_modules\resource_operations_remaster\source_data",
        destination_folder=r"D:\graduate_design\example1\operation_modules\resource_operations_remaster\destination_data",
        input_file=episode)

class SARSA:
    def __init__(self,actions_list,n_states, n_actions, alpha=0.1, gamma=0.9, epsilon=0.2,test_mode_=False):
        self.actions_list = actions_list
        self.n_actions = n_actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = np.zeros((n_states, n_actions))
        self.test_mode = test_mode_
    def choose_action(self, state):
        if self.test_mode==True or np.random.uniform() < self.epsilon:
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
    def train(self,train_dataset_dir,enable_log_):
        episodes = get_all_file_paths(target_dir=train_dataset_dir)
        print("episode count:"+str(len(episodes)))
        evasion = 0
        for episode in episodes:
            use_signature = False
            state = 0  # 初始状态（未成功次数为0）
            count = 0
            done = False
            reward = 0
            action = self.choose_action(state)
            action_name = self.actions_list[action]
            try:
                do_action(action_name=action_name, episode=episode, enable_log_=enable_log_)
            except Exception as e:
                print(e)
            if action_name =="action_create_fake_signature":
                count = 16
                use_signature = True
                # 防止签名被破坏
            elif action_name == "action_add_benign_data_overlay_1" or action_name == "action_add_bytes_to_section_cave_1" or action_name == "action_add_random_resources" or action_name =="add_section_benign_data_1" or action_name == "insert_useless_data_to_end":
                reward = 1
            print(os.path.basename(episode) + " choose action:" + action_name)
            total_reward = 0
            origin_file_size = os.path.getsize(episode)
            while not done:
                valid = True
                # 执行动作并获取结果
                # clamScanner反病毒软件扫描
                if clamScanner(episode):
                    valid = False
                elif not clamScanner(episode):
                    valid = True

                if valid:
                    evasion = evasion + 1
                    reward = reward + 100
                    now_file_size = os.path.getsize(episode)
                    discount = np.log(now_file_size / origin_file_size)
                    reward = reward / ((1 / 3) * discount + 1)
                    print("episode:" + os.path.basename(episode) + ","+ "reward:" + str(reward))
                    next_state = None
                    done = True
                else:
                    count += 1
                    if count >= 16:
                        reward = 0
                        if use_signature:
                            reward = 0
                        print("episode:" + os.path.basename(episode) +","+ "fail")
                        next_state = None
                        done = True
                    else:
                        # 失败继续工作
                        reward = reward + 0
                        next_state = count
                        done = False

                total_reward += reward

                # 更新Q表
                if done:
                    self.update(state, action, reward, next_state=None, done=True)
                else:
                    next_action = self.choose_action(next_state)
                    self.update(state, action, reward, next_state, next_action)
                    state = next_state
                    action = next_action
                    action_name_1 = self.actions_list[action]
                    try:
                        do_action(action_name=action_name_1, episode=episode, enable_log_=enable_log_)
                    except Exception as e:
                        print(e)

                    print(os.path.basename(episode) + " choose action:" + action_name_1)
                    if action_name_1 == "action_create_fake_signature":
                        count = 16
                        use_signature =True
                    elif action_name == "action_add_benign_data_overlay_1" or action_name == "action_add_bytes_to_section_cave_1" or action_name == "action_add_random_resources" or action_name == "add_section_benign_data_1" or action_name == "insert_useless_data_to_end":
                        reward = 1
                        # 防止签名被破坏

            print(f"Total Reward: {total_reward}")
        print("evasion count:"+str(evasion))

if __name__ == "__main__":
    n_states_ = 16  # 状态0-9（对应未成功次数）
    n_actions_ = 10  # 可用动作数量
    actions_list_ = get_random_actions(n_actions_)
    for i in actions_list_:
        print(i)
    num1 = input()
    a = int(num1)
    if a == 1:
        agent = SARSA(actions_list=actions_list_, n_states=n_states_, n_actions=n_actions_)

        agent.train(train_dataset_dir=r"D:\graduate_design\example1\samples\sample5\sample", enable_log_=False)
        # 打印训练后的Q表
        print("\nTrained Q-table:")
        print(agent.q_table)

        clear_directory(target_dir=r"D:\graduate_design\example1\operation_modules\resource_operations_remaster\temp")
        clear_directory(target_dir=r"D:\graduate_design\example1\operation_modules\process_remaster\example_debug\temp")







