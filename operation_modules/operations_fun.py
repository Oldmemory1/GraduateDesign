import time

from init.reset_test_enviroment import init_environment
from operation_modify_timeStamp import modify_pe_timestamp
from operation_modules.operation_insert_useless_data_to_end import append_to_pe
from operation_rename_random_section import rename_random_section
from operation_modify_timeStamp import getTimeStamp
from operation_modify_checksum import modify_pe_checksum
from operation_modify_checksum import getCheckSum
from string_generator.generated_strings.strings_length_64 import strings_64bytes
from string_generator.generated_strings.strings_length_128 import strings_128bytes
from string_generator.generated_strings.strings_length_256 import strings_256bytes
from string_generator.generated_strings.strings_length_512 import strings_512bytes
from string_generator.generated_strings.strings_length_1024 import strings_1024bytes
from string_generator.generated_strings.strings_length_2048 import strings_2048bytes
from string_generator.generated_strings.strings_length_4096 import strings_4096bytes
from string_generator.generated_strings.get_a_random_string_from_strings import get_random_string
from string2 import str2
def fun1(file):
    init_environment()
    modify_pe_timestamp(input_file=file)
    rename_random_section(input_file=file)
    getTimeStamp(input_file=file)
    modify_pe_checksum(input_file=file)
    getCheckSum(input_file=file)
    append_to_pe(input_file=file, append_data=get_random_string(string_list=strings_4096bytes))
if __name__=="__main__":
    fun1(r"D:\毕业设计\example1\source_file\sample1.exe")

