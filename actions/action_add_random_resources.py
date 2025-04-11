import logging

from operation_modules.resource_operations_remaster.add_random_resources import add_random_resources

logging.basicConfig(
    level=logging.DEBUG,       # 设置最低日志级别（DEBUG 及以上均输出）
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename=r"D:\graduate_design\example1\logs\record.log",        # 输出到文件（不指定则默认输出到控制台）
    filemode="a"               # 文件写入模式（'a' 追加，'w' 覆盖）
)

def action_add_random_resources(source_folder,destination_folder,input_file):

    add_random_resources(source_folder_=source_folder,
                         destination_folder_=destination_folder,
                         input_file_=input_file)

if __name__ == "__main__":
    action_add_random_resources(
        source_folder=r"D:\graduate_design\example1\operation_modules\resource_operations_remaster\source_data",
        destination_folder=r"D:\graduate_design\example1\operation_modules\resource_operations_remaster\destination_data",
        input_file=r"D:\graduate_design\example1\operation_modules\resource_operations_remaster\test_sample\sample1.exe",
        )
