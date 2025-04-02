import os


def get_all_file_paths(target_dir):
    file_paths = []

    # 遍历目录树
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            # 拼接绝对路径
            abs_path = os.path.join(root, file)
            file_paths.append(abs_path)

    return file_paths

