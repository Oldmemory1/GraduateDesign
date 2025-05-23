import hashlib
import logging
import os
import time

from init.reset_test_enviroment import init_environment
from operation_modules.copy_file import copy_file
from operation_modules.process_remaster.operation_add_benign_data_overlay_1 import append_benign_data_overlay
from operation_modules.process_remaster.operation_add_benign_data_overlay_depend_on_benign import \
    add_benign_data_overlay_depend_on_benign
from string_generator.generated_strings.get_a_random_string_from_strings import get_random_string
from string_generator.generated_strings.strings_length_4096 import strings_4096bytes

logging.basicConfig(
    level=logging.DEBUG,       # 设置最低日志级别（DEBUG 及以上均输出）
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename=r"D:\graduate_design\example1\logs\record.log",        # 输出到文件（不指定则默认输出到控制台）
    filemode="a"               # 文件写入模式（'a' 追加，'w' 覆盖）
)
def action_add_benign_data_overlay_1(input_file_,benign_files_dir_,enable_log = False):
    # use for testing/debugging actions
    with open(input_file_, "rb") as f1:
        bytez = f1.read()
    f1.close()
    if enable_log:
        m1 = hashlib.sha256()
        m1.update(bytez)
        logging.info("action_add_benign_data_overlay_1 before file:" + m1.hexdigest())
    bytez1 = add_benign_data_overlay_depend_on_benign(input_bytez=bytez, benign_files_dir= benign_files_dir_)
    file_name = os.path.basename(input_file_)
    temp_name = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    temp_name = temp_name + "-action_add_benign_data_overlay_1-" + file_name
    address1 = r"D:\graduate_design\example1\operation_modules\process_remaster\example_debug\temp" + "\\" + temp_name
    with open(address1, "wb+") as f2:
        f2.write(bytez1)
    f2.close()
    os.remove(input_file_)
    copy_file(source_address=address1, destination_address=input_file_)
    #os.remove(address1)
    if enable_log:
        m2 = hashlib.sha256()
        m2.update(bytez1)
        logging.info("action_add_benign_data_overlay_1 after file:" + m2.hexdigest())
if __name__ == "__main__":
        init_environment()
        input_file = r"D:\graduate_design\example1\source_file\sample1.exe"
        action_add_benign_data_overlay_1(input_file_=input_file,
                                         benign_files_dir_=r"D:\graduate_design\example1\benign_software",
                                         enable_log=True)