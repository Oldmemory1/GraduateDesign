import os.path
import warnings

from operation_modules.findAllSignatures import get_all_file_paths
from virus_scanner_module.clamScanner import clamScanner


def sample_malicious_test(dir_):
    warnings.warn("deprecated")
    samples_file_name= get_all_file_paths(target_dir=dir_)
    print("file amount:" + str(len(samples_file_name)))
    detect = 0
    for sample_file in samples_file_name:
        result = clamScanner(sample_file)
        print(os.path.basename(sample_file)+","+str(result))
        if result:
            detect = detect + 1
    return detect

if __name__ == '__main__':
    #before_evasion1 = sample_malicious_test(r"D:\毕业设计\malware\sample1\sample")
    #after_evasion1 = sample_malicious_test(r"D:\graduate_design\example1\samples\sample1\sample")
    #before_evasion2 = sample_malicious_test(r"D:\毕业设计\malware\sample2\sample")
    #after_evasion2 = sample_malicious_test(r"D:\graduate_design\example1\samples\sample2\sample")
    #before_evasion3 = sample_malicious_test(r"D:\毕业设计\malware\sample3\sample")
    #after_evasion3 = sample_malicious_test(r"D:\graduate_design\example1\samples\sample3\sample")
    #before_evasion4 = sample_malicious_test(r"D:\毕业设计\malware\sample4\sample")
    #after_evasion4 = sample_malicious_test(r"D:\graduate_design\example1\samples\sample4\sample")
    #print("before sample1 amount:"+str(len(get_all_file_paths(r"D:\毕业设计\malware\sample1\sample"))))
    #print("after sample1 amount:"+str(len(get_all_file_paths(r"D:\graduate_design\example1\samples\sample1\sample"))))
    #print("before1:"+str(before_evasion1))
    #print("after1:"+str(after_evasion1))
    #print("before sample2 amount:" + str(len(get_all_file_paths(r"D:\毕业设计\malware\sample2\sample"))))
    #print("after sample2 amount:"+str(len(get_all_file_paths(r"D:\graduate_design\example1\samples\sample2\sample"))))
    #print("before2:" + str(before_evasion2))
    #print("after2:" + str(after_evasion2))
    #print("before sample3 amount:" + str(len(get_all_file_paths(r"D:\毕业设计\malware\sample3\sample"))))
    #print("after sample3 amount:"+str(len(get_all_file_paths(r"D:\graduate_design\example1\samples\sample3\sample"))))

    #before_evasion4 = sample_malicious_test(r"D:\毕业设计\malware\sample4\sample")
    after_evasion1 = sample_malicious_test(r"D:\graduate_design\example1\samples\origin\sample1\sample")
    #print("before4:" + str(before_evasion4))
    print("detect amount:" + str(after_evasion1))
    #print("before sample4 amount:" + str(len(get_all_file_paths(r"D:\毕业设计\malware\sample4\sample"))))
    print("sample amount:"+str(len(get_all_file_paths(r"D:\graduate_design\example1\samples\origin\sample1\sample"))))