import random
import time
def generate_random_timestamp():
    # 获取当前时间戳
    current_ts = int(time.time())
    # 计算一年前的秒数（365天）
    one_year_ago = current_ts - 31536000
    # 生成随机时间戳
    random_ts = random.randint(one_year_ago, current_ts)



if __name__ == "__main__":
    print("随机时间戳（秒）:", random_ts)
    print("对应UTC时间:", time.gmtime(random_ts))
