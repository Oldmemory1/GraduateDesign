import os
from datetime import datetime

from copy_file import copy_file
import pefile
import time
#修改时间戳 但是最后会复制一个文件回来
def modify_pe_timestamp(input_file,new_timestamp=None):
    # 加载PE文件
    pe = pefile.PE(input_file)

    # 获取原始时间戳
    original_timestamp = pe.FILE_HEADER.TimeDateStamp
    # print(f"Original Timestamp: {original_timestamp} ({time.ctime(original_timestamp)})")

    # 设置新时间戳（如果未提供，使用当前时间）
    if new_timestamp is None:
        new_timestamp = int(time.time())
    pe.FILE_HEADER.TimeDateStamp = new_timestamp
    #print(new_timestamp)
    #获取文件名
    file_name = os.path.basename(input_file)
    temp_name=time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    #print(temp_name)
    temp_name= temp_name + "-modify_timestamp-" + file_name
    #print(temp_name)
    # 保存修改后的文件
    address1 = r"D:\毕业设计\example1\temp"+"\\"+temp_name
    #print(address1)
    pe.write(address1)
    pe.close()
    # 删除原有文件
    os.remove(input_file)
    # 复制过来新生成的文件
    copy_file(address1, input_file)
    os.remove(address1)
#修改时间戳 但是最后会放置在目标位置
def modify_pe_timestamp_and_output(input_file, output_file, new_timestamp=None):
    # 加载PE文件
    pe = pefile.PE(input_file)

    # 获取原始时间戳
    original_timestamp = pe.FILE_HEADER.TimeDateStamp
    #print(f"Original Timestamp: {original_timestamp} ({time.ctime(original_timestamp)})")

    # 设置新时间戳（如果未提供，使用当前时间）
    if new_timestamp is None:
        new_timestamp = int(time.time())
    pe.FILE_HEADER.TimeDateStamp = new_timestamp

    # 保存修改后的文件
    pe.write(output_file)
    pe.close()

    #print(f"New Timestamp: {new_timestamp} ({time.ctime(new_timestamp)})")
#获取一个文件的时间戳
def getTimeStamp(file):
    import pefile
    import datetime
    pe = pefile.PE(file)
    timestamp = pe.FILE_HEADER.TimeDateStamp
    print(f"Timestamp: {timestamp}")
if __name__=="__main__":
    custom_time = datetime(2000, 1, 1).timestamp()
    #getTimeStamp(r"D:\毕业设计\example1\source_file\sample1.exe")
    input_file1 = r"D:\毕业设计\example1\source_file\sample1.exe"
    modify_pe_timestamp(input_file=input_file1,new_timestamp=int(custom_time))
    #getTimeStamp(r"D:\毕业设计\example1\source_file\sample1.exe")