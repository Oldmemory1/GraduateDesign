import time

from init.reset_test_enviroment import init_environment
from operation_modify_timeStamp import modify_pe_timestamp
from operation_modules.operation_insert_useless_data_to_end import append_to_pe
from operation_rename_random_section import rename_random_section
from operation_modify_timeStamp import getTimeStamp
from operation_modify_checksum import modify_pe_checksum
from operation_modify_checksum import getCheckSum
from string2 import str2
def fun1(file):
    init_environment()
    modify_pe_timestamp(input_file=file)
    rename_random_section(input_file=file)
    getTimeStamp(input_file=file)
    modify_pe_checksum(input_file=file)
    getCheckSum(input_file=file)
    append_to_pe(input_file=file, append_data=str2*256)
if __name__=="__main__":
    fun1(r"D:\毕业设计\example1\source_file\sample1.exe")

