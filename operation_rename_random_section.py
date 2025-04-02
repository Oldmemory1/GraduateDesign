import pefile
import random
import string


def generate_random_section_name():
    """生成8个字符的随机名称（字母和数字组合）"""
    characters = string.ascii_letters + string.digits  # 包含大小写字母和数字
    return ''.join(random.choices(characters, k=8))


def rename_random_section(input_file, output_file):
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

"""
if __name__ == "__main__":
    input_path = "HelloWorld1.exe"  # 输入PE文件路径
    output_path = "modified.exe"  # 输出文件路径
    rename_random_section(input_path, output_path)
"""
