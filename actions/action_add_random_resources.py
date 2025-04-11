import hashlib
import logging

from init.reset_test_enviroment import init_environment
from operation_modules.resource_operations_remaster.add_random_resources import add_random_resources

logging.basicConfig(
    level=logging.DEBUG,       # 设置最低日志级别（DEBUG 及以上均输出）
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename=r"D:\graduate_design\example1\logs\record.log",        # 输出到文件（不指定则默认输出到控制台）
    filemode="a"               # 文件写入模式（'a' 追加，'w' 覆盖）
)
def action_add_random_resources(source_folder,destination_folder,input_file,enable_log=False):
    if enable_log:
        with open(input_file, "rb") as f1:
            bytez = f1.read()
        f1.close()
        m1 = hashlib.sha256()
        m1.update(bytez)
        logging.info("action_add_random_resources before file:" + m1.hexdigest())
    add_random_resources(source_folder_=source_folder,
                         destination_folder_=destination_folder,
                         input_file_=input_file)
    if enable_log:
        with open(input_file, "rb") as f2:
            bytez = f2.read()
        f2.close()
        m2 = hashlib.sha256()
        m2.update(bytez)
        logging.info("action_add_random_resources after file:" + m2.hexdigest())
if __name__ == "__main__":
    init_environment()
    source_folder_ = r"D:\graduate_design\example1\operation_modules\resource_operations_remaster\source_data",
    destination_folder_ = r"D:\graduate_design\example1\operation_modules\resource_operations_remaster\destination_data",
    input_file_ = r"D:\graduate_design\example1\operation_modules\test_sample\sample1.exe"
    action_add_random_resources(source_folder=source_folder_,
                                destination_folder=destination_folder_,
                                input_file=input_file_)