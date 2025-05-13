import os

from operation_modules.findAllSignatures import get_all_file_paths
from reinforce_learning.result_check.util.utils import print_result, check_result
from virus_scanner_module.clamScanner import clamScanner


def get_after_malicious_detect_count(directory1):
    samples_file_name = get_all_file_paths(target_dir=directory1)
    detect = 0
    for sample_file in samples_file_name:
        result = (clamScanner(sample_file))
        print_result(os.path.basename(sample_file), result)
        if result:
            detect = detect + 1
    return detect
if __name__ == '__main__':
    detect_amount = get_after_malicious_detect_count(r"D:\graduate_design\example1\samples\origin\sample2\sample")
    print("processed sample amount:" + str(len(get_all_file_paths(r"D:\graduate_design\example1\samples\origin\sample2\sample"))))
    print("processed sample detect amount:" + str(detect_amount))