import os
import shutil

def clear_directory(target_dir):
    """
    删除目标目录下的所有文件和子目录，保留目标目录本身
    :param target_dir: 要清空的目录绝对路径
    """
    # 验证路径是否存在且为目录
    if not os.path.isdir(target_dir):
        raise NotADirectoryError(f"路径 '{target_dir}' 不存在或不是目录")

    # 遍历目录内容
    for entry in os.listdir(target_dir):
        entry_path = os.path.join(target_dir, entry)
        try:
            if os.path.isfile(entry_path) or os.path.islink(entry_path):
                os.unlink(entry_path)  # 删除文件或符号链接
            else:
                shutil.rmtree(entry_path)  # 删除子目录
        except Exception as e:
            print(f"⚠️ 删除失败: {entry_path} - 原因: {e}")

if __name__ == "__main__":
    clear_directory(r"D:\毕业设计\example1\sample")