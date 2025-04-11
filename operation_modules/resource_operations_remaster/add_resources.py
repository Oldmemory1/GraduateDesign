import os
import random
import string
import subprocess
import time

from operation_modules.copy_file import copy_file
from set_version_info import generate_random_string, set_version_info


def add_resources(input_file,icon_folder):
    input_file_name = os.path.basename(input_file)
    temp_name1 = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    # print(temp_name)
    temp_name1 = temp_name1 + "-add_random_resources-" + input_file_name
    # print(temp_name)
    # 保存修改后的文件
    address1 = r"D:\graduate_design\example1\operation_modules\resource_operations_remaster\temp" + "\\" + temp_name1
    #print(address1)
    #savaname = generate_random_string(15)
    icon_files = os.listdir(icon_folder)
    random_icon_files = random.sample(icon_files, 2)

    random_icon1 = random_icon_files[0]
    random_icon2 = random_icon_files[1]

    command1 = [
        "ResourceHacker.exe",
        "-open", input_file,
        "-save", address1,
        "-action", "addskip",
        "-res", f"{icon_folder}/{random_icon1}",
        "-mask", f"ICONGROUP,{random.choice(string.ascii_lowercase) + generate_random_string(15)}"
    ]
    subprocess.run(command1, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    time.sleep(2)


    temp_name2 = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    # print(temp_name)
    temp_name2 = temp_name2 + "-add_random_resources-" + input_file_name
    address2 = r"D:\graduate_design\example1\operation_modules\resource_operations_remaster\temp" + "\\" + temp_name2
    #print(address2)
    command2 = [
        "ResourceHacker.exe",
        "-open", address1,
        "-save", address2,
        "-action", "addskip",
        "-res", f"{icon_folder}/{random_icon2}",
        "-mask", f"ICONGROUP,{random.choice(string.ascii_lowercase) + generate_random_string(15)}"
    ]
    subprocess.run(command2, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    set_version_info(address2)
    #后面还要用copy_file
    os.remove(address1)
    #os.remove("output.exe")
    copy_file(source_address=address2, destination_address=input_file)
    os.remove(address2)
if __name__ == '__main__':
    add_resources(input_file=r"D:\graduate_design\example1\operation_modules\resource_operations_remaster\test_sample\sample1.exe", icon_folder=r"D:\graduate_design\example1\operation_modules\resource_operations_remaster\destination_data")