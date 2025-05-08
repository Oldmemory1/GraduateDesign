import os

from operation_modules.findAllSignatures import get_all_file_paths
from reinforce_learning.result_check.util.utils import check_result, print_result, print_result1
from virus_scanner_module.clamScanner import clamScanner


def get_before_malicious_detect_count(directory1):
    samples_file_name = get_all_file_paths(target_dir=directory1)
    detect = 0
    for sample_file in samples_file_name:
        result = check_result(clamScanner(sample_file))
        print_result1(os.path.basename(sample_file),result)
        if result:
            detect = detect + 1
    return detect
if __name__ == '__main__':
    detect_amount = get_before_malicious_detect_count(r"D:\graduate_design\example1\samples\origin\sample5\sample")
    print("origin sample amount:" + str(len(get_all_file_paths(r"D:\graduate_design\example1\samples\origin\sample5\sample"))))
    print("origin sample detect amount:" + str(detect_amount))
