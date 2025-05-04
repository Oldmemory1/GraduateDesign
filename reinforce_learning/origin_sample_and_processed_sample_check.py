from operation_modules.findAllSignatures import get_all_file_paths
from reinforce_learning.result_check.after_malicious_detect_count import get_after_malicious_detect_count
from reinforce_learning.result_check.before_malicious_detect_count import get_before_malicious_detect_count


def origin_sample_and_processed_check(origin_dir,processed_dir):
    origin_detect_amount = get_before_malicious_detect_count(origin_dir)
    processed_detect_amount = get_after_malicious_detect_count(processed_dir)
    print("origin sample amount:" + str(len(get_all_file_paths(origin_dir))))
    print("origin sample detect amount:" + str(origin_detect_amount))
    print("processed sample amount:" + str(len(get_all_file_paths(processed_dir))))
    print("processed sample detect amount:" + str(processed_detect_amount))
if __name__ == '__main__':
    origin_dir_=r"D:\graduate_design\example1\samples\origin\sample1\sample"
    processed_dir_=r"D:\graduate_design\example1\samples\processed\sample1\sample"
    origin_sample_and_processed_check(origin_dir=origin_dir_,processed_dir=processed_dir_)