import pefile
from string1 import str1
from string2 import str2

def append_to_pe(input_file, output_file, append_data):
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
        input_file='HelloWorld2.exe',
        output_file='HelloWorld3.exe',
        append_data=str2*128  # 要附加的字符串
    )

