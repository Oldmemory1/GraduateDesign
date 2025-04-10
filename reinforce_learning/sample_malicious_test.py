import os.path

from operation_modules.findAllSignatures import get_all_file_paths
from virus_scanner_module.clamScanner import clamScanner


def sample_malicious_test(dir_):
    samples_file_name= get_all_file_paths(target_dir=dir_)
    for sample_file in samples_file_name:
        result = clamScanner(sample_file)
        print(os.path.basename(sample_file)+","+str(result))
        if not result:
            os.remove(sample_file)
if __name__ == '__main__':
    sample_malicious_test(r"D:\毕业设计\example1\sample")
