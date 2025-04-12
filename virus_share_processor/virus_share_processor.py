import os

from operation_modules.copy_file import copy_file
from operation_modules.findAllSignatures import get_all_file_paths
# D:\graduate_design\example1\virus_share_processor\result

def virus_share_processor(input_dir,output_dir):
    samples_files = get_all_file_paths(target_dir=input_dir)
    for sample in samples_files:
        sample_name = os.path.basename(sample)
        output_sample_dir = output_dir + "\\" +sample_name +".exe"
        copy_file(source_address=sample, destination_address=output_sample_dir)
if __name__ == "__main__":
    virus_share_processor(
        input_dir=r"D:\graduate_design\example1\virus_share_processor\VirusShare_x86-64_WinEXE_20130711_samples",
        output_dir=r"D:\graduate_design\example1\virus_share_processor\result"
    )


