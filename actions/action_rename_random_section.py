import hashlib
import logging

from init.reset_test_enviroment import init_environment
from operation_modules.operation_rename_random_section import rename_random_section

logging.basicConfig(
    level=logging.DEBUG,       # 设置最低日志级别（DEBUG 及以上均输出）
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename=r"D:\毕业设计\example1\logs\record.log",        # 输出到文件（不指定则默认输出到控制台）
    filemode="a"               # 文件写入模式（'a' 追加，'w' 覆盖）
)
def action_rename_random_section(input_file_,enable_log=False):
    if enable_log:
        with open(input_file_, "rb") as f1:
            bytez = f1.read()
        f1.close()
        m1 = hashlib.sha256()
        m1.update(bytez)
        logging.info("action_rename_random_section before file:" + m1.hexdigest())

    rename_random_section(input_file=input_file_)

    if enable_log:
        with open(input_file_, "rb") as f2:
            bytez = f2.read()
        f2.close()
        m2 = hashlib.sha256()
        m2.update(bytez)
        logging.info("action_rename_random_section after file:" + m2.hexdigest())
    if __name__ == "__main__":
        init_environment()
        input_file = r"D:\毕业设计\example1\source_file\sample1.exe"
        action_rename_random_section(input_file_=input_file, enable_log=True)