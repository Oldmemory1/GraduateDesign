import os
import time

import pefile

from operation_modules.copy_file import copy_file
from string2 import str2
# completed
# 尾部添加无用字节 但是最后会复制一个文件回来
def append_to_pe(input_file,append_data):
    file_name = os.path.basename(input_file)
    temp_name = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    # print(temp_name)
    temp_name = temp_name + "-insert_useless_data_to_end-" + file_name
    # print(temp_name)
    # 保存修改后的文件
    address1 = r"D:\毕业设计\example1\temp" + "\\" + temp_name
    pe = pefile.PE(input_file)

    # 将原始PE内容写入新文件
    pe_data = pe.write()

    with open(address1, 'wb') as f:
        f.write(pe_data)
        # 在文件末尾附加数据
        f.write(append_data.encode('utf-8'))

    pe.close()

    f.close()

    os.remove(input_file)
    # 复制过来新生成的文件
    copy_file(source_address=address1, destination_address=input_file)
    os.remove(address1)
# 尾部添加无用字节 但是最后会放置在目标位置
def append_to_pe_and_output(input_file, output_file, append_data):
    # 加载PE文件
    pe = pefile.PE(input_file)

    # 将原始PE内容写入新文件
    pe_data = pe.write()

    with open(output_file, 'wb') as f:
        f.write(pe_data)
        # 在文件末尾附加数据
        f.write(append_data.encode('utf-8'))


if __name__ == "__main__":
    # 示例用法
    append_to_pe(
        input_file=r"D:\毕业设计\example1\source_file\sample1.exe",
        append_data=str2*128  # 要附加的字符串
    )

