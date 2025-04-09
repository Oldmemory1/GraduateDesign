import os
import time

from operation_modules.copy_file import copy_file
import pefile
import random
import string

# completed
def generate_random_section_name():
    """生成8个字符的随机名称（字母和数字组合）"""
    characters = string.ascii_letters + string.digits  # 包含大小写字母和数字
    return ''.join(random.choices(characters, k=8))
#修改某个节的名字 但是最后会复制一个文件回来
def rename_random_section(input_file):
    # 加载PE文件
    pe = pefile.PE(input_file)

    # 获取所有节
    sections = pe.sections
    if not sections:
        print("There is no sections in file")
        return

    # 随机选择一个节
    selected_section = random.choice(sections)
    old_name = selected_section.Name.decode('utf-8').rstrip('\x00')  # 去除尾部空字符

    # 生成新名称并修改
    new_name = generate_random_section_name()
    selected_section.Name = new_name.encode('ascii')  # 确保名称编码为ASCII
    #print(new_name)
    #获取文件名
    file_name = os.path.basename(input_file)
    temp_name=time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    #print(temp_name)
    temp_name= temp_name + "-raname_random_section-" + file_name
    #print(temp_name)
    # 保存修改后的文件
    address1 = r"D:\毕业设计\example1\temp"+"\\"+temp_name
    #print(address1)
    pe.write(address1)
    pe.close()
    #删除原有文件
    os.remove(input_file)
    #复制过来新生成的文件
    copy_file(address1,input_file)
    os.remove(address1)
    # print(f"文件已保存为: {output_file}")
#修改某个节的名字 但是最后会放在目标位置
def rename_random_section_and_output(input_file, output_file):
    # 加载PE文件
    pe = pefile.PE(input_file)

    # 获取所有节
    sections = pe.sections
    if not sections:
        print("There is no sections in file")
        return

    # 随机选择一个节
    selected_section = random.choice(sections)
    old_name = selected_section.Name.decode('utf-8').rstrip('\x00')  # 去除尾部空字符

    # 生成新名称并修改
    new_name = generate_random_section_name()
    selected_section.Name = new_name.encode('ascii')  # 确保名称编码为ASCII

    # 输出信息
    #print(f"已将节名从 '{old_name}' 修改为 '{new_name}'")

    # 保存修改后的文件
    pe.write(output_file)
    pe.close()
    #print(f"文件已保存为: {output_file}")


if __name__ == "__main__":
    input_path = r"D:\毕业设计\example1\source_file\sample1.exe"  # 输入PE文件路径
    rename_random_section(input_path)

