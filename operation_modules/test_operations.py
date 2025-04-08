from operation_modify_timeStamp import modify_pe_timestamp
from operation_rename_random_section import rename_random_section
from operation_modify_timeStamp import getTimeStamp
def fun1(file):
    modify_pe_timestamp(file)
    rename_random_section(file)
    getTimeStamp(file)
if __name__=="__main__":
    fun1(r"D:\毕业设计\example1\source_file\sample1.exe")

