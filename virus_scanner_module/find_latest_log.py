import os


def read_largest_filename_file(folder_path_):
    # 获取所有文件的文件名（排除目录）
    with os.scandir(folder_path_) as entries:
        file_names = [entry.name for entry in entries if entry.is_file()]

    if not file_names:
        raise FileNotFoundError("指定目录中没有文件。")

    max_filename = max(file_names)  # 按字典序获取最大文件名
    max_filepath = os.path.join(folder_path_, max_filename)

    # 读取文件内容
    return max_filepath

if __name__ == '__main__':
    # 示例用法
    folder_path = r"C:\Program Files\360\360sd\Log\VirusScanLog"
    try:
        path_ = read_largest_filename_file(folder_path_=folder_path)
        print("文件位置：", path_)
    except FileNotFoundError as e:
        print(e)
