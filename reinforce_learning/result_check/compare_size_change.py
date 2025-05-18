import os.path

from operation_modules.findAllSignatures import get_all_file_paths
import numpy as np

def compare_size_change(directory1, directory2):
    before_file = get_all_file_paths(target_dir=directory1)
    after_file = get_all_file_paths(target_dir=directory2)
    print(len(before_file), len(after_file))
    list1=[]
    for i in range(0,len(before_file)):
        origin_file_size = os.path.getsize(before_file[i])
        after_file_size = os.path.getsize(after_file[i])
        change = after_file_size/origin_file_size
        list1.append(change)
    print(np.average(list1))
if __name__ == "__main__":
    compare_size_change(directory1=r"D:\graduate_design\example1\samples\origin\sample1\sample",directory2=r"D:\graduate_design\example1\samples\processed\sample1\sample")