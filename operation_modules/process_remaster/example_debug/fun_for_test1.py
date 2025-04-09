import hashlib
import os
import time

from init.clear_directory import clear_directory
from init.reset_test_enviroment import init_environment
from operation_modules.copy_file import copy_file
from operation_modules.process_remaster.operation_add_bytes_to_section_cave_1 import add_bytes_to_section_cave
from operation_modules.process_remaster.operation_add_imports_1 import add_imports
from operation_modules.process_remaster.operation_add_section_benign_data_1 import add_section_benign_data
from operation_modules.process_remaster.operation_break_optional_header_checksum_1 import break_optional_header_checksum
from operation_modules.process_remaster.operation_modify_machine_type_1 import modify_machine_type
from operation_modules.process_remaster.operation_modify_optional_header_1 import modify_optional_header
from operation_modules.process_remaster.operation_modify_timestamp_1 import modify_timestamp
from operation_modules.process_remaster.operation_remove_debug_1 import remove_debug
from operation_modules.process_remaster.operation_rename_section_1 import rename_section
from string_generator.generated_strings.strings_length_4096 import strings_4096bytes


def fun_test_and_output(input_file,output_file):
    init_environment()
    clear_directory(r"D:\毕业设计\example1\operation_modules\process_remaster\example_debug\debug_result")
    # use for testing/debugging actions
    with open(input_file, "rb") as f:
        bytez = f.read()

    m = hashlib.sha256()
    m.update(bytez)
    print(f"original hash: {m.hexdigest()}")
    bytez1 =add_bytes_to_section_cave(bytez,string_list=strings_4096bytes)
    m = hashlib.sha256()
    m.update(bytez1)

    with open(output_file, "wb+") as f1:
        f1.write(bytez1)
    print(f"modified hash: {m.hexdigest()}")
def fun_test(input_file):
    init_environment()
    clear_directory(r"D:\毕业设计\example1\operation_modules\process_remaster\example_debug\debug_result")
    # use for testing/debugging actions
    with open(input_file, "rb") as f:
        bytez = f.read()

    m = hashlib.sha256()
    m.update(bytez)
    print(f"original hash: {m.hexdigest()}")
    #bytez1 = append_benign_data_overlay(bytez, get_random_string(string_list=strings_4096bytes))
    #bytez1=add_bytes_to_section_cave(bytez,string_list=strings_4096bytes)
    #bytez1=add_imports(bytez)
    #bytez1=add_section_benign_data(bytez,string_list=strings_4096bytes)
    #bytez1 = break_optional_header_checksum(bytez)
    #bytez1 = modify_machine_type(bytez)
    #bytez1 = modify_optional_header(bytez)
    #bytez1 = modify_timestamp(bytez)
    #bytez1 = remove_debug(bytez)
    bytez1 = rename_section(bytez)
    m = hashlib.sha256()
    m.update(bytez1)

    file_name = os.path.basename(input_file)
    temp_name = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    # print(temp_name)
    temp_name = temp_name + "-modified-" + file_name
    # print(temp_name)
    # 保存修改后的文件
    address1 = r"D:\毕业设计\example1\operation_modules\process_remaster\example_debug\temp" + "\\" + temp_name

    with open(address1, "wb+") as f1:
        f1.write(bytez1)
    f1.close()
    os.remove(input_file)
    copy_file(source_address=address1, destination_address=input_file)
    #os.remove(address1)
    print(f"modified hash: {m.hexdigest()}")
if __name__ == "__main__":
    input_file1 = r"D:\毕业设计\example1\source_file\sample1.exe"
    output_file1=r"D:\毕业设计\example1\operation_modules\process_remaster\example_debug\debug_result\sample1_result.exe"
    """
    fun_test_and_output(input_file=input_file1,
                        output_file=output_file1)
    """
    fun_test(input_file=input_file1)