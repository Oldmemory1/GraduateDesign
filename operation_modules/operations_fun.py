from init.reset_test_enviroment import init_environment
from operation_modify_timeStamp import modify_pe_timestamp
from operation_rename_random_section import rename_random_section
from operation_modify_timeStamp import getTimeStamp
from operation_modify_checksum import modify_pe_checksum
from operation_modify_checksum import getCheckSum

def fun1(file):
    init_environment()
    modify_pe_timestamp(file)
    rename_random_section(file)
    getTimeStamp(file)
    modify_pe_checksum(file)
    getCheckSum(file)
if __name__=="__main__":
    fun1(r"D:\毕业设计\example1\source_file\sample1.exe")

