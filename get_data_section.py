import pefile


def get_pe_data_section(file_path):
    try:
        # 加载PE文件
        pe = pefile.PE(file_path)

        # 遍历所有节
        for section in pe.sections:
            # 清理节名中的空字符和空格
            section_name = section.Name.decode().strip('\x00').strip()

            # 检查是否为.data节
            if section_name == '.data':
                data_content = section.get_data()
                # 返回数据内容（或根据需求处理）
                return data_content

        # 未找到.data节
        print("未找到.data节。")
        return None

    except pefile.PEFormatError as e:
        print(f"PE文件格式错误: {e}")
        return None
    except IOError as e:
        print(f"文件读取失败: {e}")
        return None
    except Exception as e:
        print(f"发生错误: {e}")
        return None

if __name__ == "__main__":
    # 使用示例
    file_path = r'D:\毕业设计\example1\vs_BuildTools.exe'  # 替换为实际路径
    data_section_content = get_pe_data_section(file_path)
    #print(data_section_content)
    if data_section_content is not None:
        # 示例：将数据保存到文件
        with open('data_section.bin', 'wb') as f:
            f.write(data_section_content)
        print("数据段内容已保存到 data_section.bin")
