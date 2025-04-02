import shutil
import os


def copy(source_file: str, destination_file: str) -> bool:
    """
    将源文件复制到目标绝对路径（支持自动创建目标目录）

    :param source_file: 源文件的绝对路径（例如 "/home/user/source.txt"）
    :param destination_file: 目标文件的绝对路径（例如 "/backup/target.txt" 或目录 "/backup/"）
    :return: 成功返回 True，失败返回 False
    """
    try:
        # 确保目标目录存在（自动创建父级目录）
        dest_dir = os.path.dirname(destination_file)
        os.makedirs(dest_dir, exist_ok=True)

        # 复制文件并保留元数据（使用 copy2）
        shutil.copy2(source_file, destination_file)
        return True
    except Exception as e:
        print(f"复制失败: {str(e)}")
        return False


# 示例用法
"""
if __name__ == "__main__":
    success = copy(
        source_file=r"D:\毕业设计\example1\source_file\HelloWorld1.exe",
        destination_file=r"D:\毕业设计\example1\destination_file\HelloWorld1.exe"
    )
    if success:
        print("文件复制成功！")
    else:
        print("文件复制失败。")
"""
