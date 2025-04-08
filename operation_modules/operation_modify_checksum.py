import os
import pefile
import time
from operation_modules.copy_file import copy_file
# completed
def getCheckSum(input_file):
    pe = pefile.PE(input_file)
    # 获取原始校验和
    original_checksum = pe.OPTIONAL_HEADER.CheckSum
    pe.close()
    print("Checksum:%s" %original_checksum)
# 修改校验和 但是最后会复制一个文件回来
def modify_pe_checksum(input_file,new_checksum=None):
    # 加载PE文件
    pe = pefile.PE(input_file)

    # 获取原始校验和
    original_checksum = pe.OPTIONAL_HEADER.CheckSum

    # 设置新校验和（如果未提供，使用当前时间）
    if new_checksum is None:
        new_checksum = 0
    pe.OPTIONAL_HEADER.CheckSum = new_checksum
     #获取文件名
    file_name = os.path.basename(input_file)
    temp_name=time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    #print(temp_name)
    temp_name= temp_name + "-modify_checksum-" + file_name
    #print(temp_name)
    # 保存修改后的文件
    address1 = r"D:\毕业设计\example1\temp"+"\\"+temp_name
    #print(address1)
    pe.write(address1)
    pe.close()
    # 删除原有文件
    os.remove(input_file)
    # 复制过来新生成的文件
    copy_file(source_address=address1, destination_address=input_file)
    os.remove(address1)
# 修改校验和 但是最后会放置在目标位置
def modify_pe_checksum_and_output(input_file, output_file, new_checksum=None):
    # 加载PE文件
    pe = pefile.PE(input_file)

    # 获取原始校验和
    original_checksum = pe.OPTIONAL_HEADER.CheckSum

    # 设置新校验和（如果未提供，使用当前时间）
    if new_checksum is None:
        new_checksum = 0
    pe.OPTIONAL_HEADER.CheckSum = new_checksum
    # 保存文件
    pe.write(output_file)
    pe.close()


if __name__ == "__main__":
   modify_pe_checksum(input_file=r"D:\毕业设计\example1\source_file\sample1.exe")
   getCheckSum(r"D:\毕业设计\example1\source_file\sample1.exe")
