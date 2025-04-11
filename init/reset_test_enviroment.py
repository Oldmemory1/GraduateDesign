import os

from init.clear_directory import clear_directory
from operation_modules.copy_file import copy_file


def init_environment():
    """
    初始化环境 删除source_file下的全部内容
    并且拷贝过来一个用于测试的文件
    """

    clear_directory(target_dir=r"D:\graduate_design\example1\source_file")
    copy_file(source_address=r"D:\fushi\HelloWorld2\cmake-build-debug\sample1.exe",
             destination_address=r"D:\graduate_design\example1\source_file\sample1.exe")
if __name__=="__main__":
   init_environment()
