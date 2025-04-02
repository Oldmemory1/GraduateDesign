import pefile
import time
def modify_pe_timestamp(input_file, output_file, new_timestamp=None):
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