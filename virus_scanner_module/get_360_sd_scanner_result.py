# 逐行读取版本（适合大文件）
from virus_scanner_module.find_latest_log import read_largest_filename_file


def check_large_file_contains_string(file_path, target_string, encoding='gbk'):
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            for line in file:
                if target_string in line:
                    return True
            return False
    except:
        return False
if __name__ == '__main__':
    folder_path = r"C:\Program Files\360\360sd\Log\VirusScanLog"
    target_str="未发现威胁文件"
    path1_ = r"C:\Program Files\360\360sd\Log\VirusScanLog\20250411103903.log"
    path_ = read_largest_filename_file(folder_path_=folder_path)
    print(check_large_file_contains_string(file_path=path_,target_string=target_str))
