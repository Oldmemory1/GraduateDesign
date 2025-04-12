import os.path

from operation_modules.findAllSignatures import get_all_file_paths
from virus_scanner_module.clamScanner import clamScanner


def sample_malicious_test(dir_):
    samples_file_name= get_all_file_paths(target_dir=dir_)
    print("file amount:" + str(len(samples_file_name)))
    evasion = 0
    for sample_file in samples_file_name:
        result = clamScanner(sample_file)
        print(os.path.basename(sample_file)+","+str(result))
        if not result:
            evasion = evasion + 1
            #os.remove(sample_file)
    print("evasion:" + str(evasion))
if __name__ == '__main__':
    sample_malicious_test(r"D:\graduate_design\example1\virus_share_processor\result")

    #sample_malicious_test(r"D:\graduate_design\example1\samples\sample2\sample")
    #sample_malicious_test(r"D:\graduate_design\example1\samples\sample3\sample")
