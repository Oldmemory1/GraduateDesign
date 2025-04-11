import time

from add_resources import add_resources
from create_ico import create_ico


def add_random_resources(source_folder_,destination_folder_,input_file_):
    create_ico(source_folder=source_folder_,destination_folder=destination_folder_)
    time.sleep(1)
    add_resources(input_file=input_file_,icon_folder=destination_folder_)

if __name__ == '__main__':
    add_random_resources(source_folder_=r"D:\graduate_design\example1\operation_modules\resource_operations_remaster\source_data",
                         destination_folder_=r"D:\graduate_design\example1\operation_modules\resource_operations_remaster\destination_data",
                         input_file_=r"D:\graduate_design\example1\operation_modules\test_sample\sample1.exe")