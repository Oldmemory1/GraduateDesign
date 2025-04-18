import os

def delete_unqualified_files(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        # 检查是否为文件（虽然题目说明没有子目录，但防止特殊情况下处理）
        if not os.path.isfile(filepath):
            continue
        # 获取文件扩展名并转为小写
        ext = os.path.splitext(filename)[1].lower()
        # 判断是否为可执行文件且大小不超过4096字节
        try:
            size = os.path.getsize(filepath)
        except OSError:
            continue  # 处理无法访问的文件
        if ext != '.exe' or size > 4096:
            try:
                os.remove(filepath)
                print(f"已删除文件：{filepath}")
            except Exception as e:
                print(f"删除{filepath}时出错：{e}")

# 使用示例
if __name__ == "__main__":
    directory_path = "./malicious"
    delete_unqualified_files(directory_path)
