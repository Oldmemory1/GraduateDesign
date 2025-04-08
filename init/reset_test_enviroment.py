from init.clear_directory import clear_directory
from operation_modules.copy_file import copy_file


def init_environment():
   clear_directory(r"D:\毕业设计\example1\source_file")
   copy_file(r"D:\fushi\HelloWorld2\cmake-build-debug\sample1.exe",r"D:\毕业设计\example1\source_file\sample1.exe")
   
