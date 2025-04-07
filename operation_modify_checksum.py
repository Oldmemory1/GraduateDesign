import pefile
import time
def modify_pe_checksum(input_file, output_file, new_checksum=None):
    # 加载PE文件
    pe = pefile.PE(input_file)

    # 获取原始校验和
    original_checksum = pe.OPTIONAL_HEADER.CheckSum

    # 设置新校验和（如果未提供，使用当前时间）
    if new_checksum is None:
        new_checksum = 0
    pe.OPTIONAL_HEADER.CheckSum = new_checksum
    """

    # 保存修改后的文件
    """
    pe.write(output_file)
    pe.close()
    """
    print(original_checksum)
    """

if __name__ == "__main__":

    modify_pe_checksum("HelloWorld2.exe","modifiedHello2.exe",0)