import hashlib
import random

import lief

from init.clear_directory import clear_directory
from init.reset_test_enviroment import init_environment
from operation_modules.findAllSignatures import get_all_file_paths


def add_benign_data_overlay_depend_on_benign(input_bytez, benign_files_dir):
    benign_files = get_all_file_paths(benign_files_dir)
    select_file = random.randint(0,len(benign_files)-1)
    #print(benign_files[select_file])
    pe1 = lief.PE.parse(benign_files[select_file])
    benign_binary_section_content = pe1.get_section(
        ".text",
    ).content
    overlay = bytearray(benign_binary_section_content)
    output_bytez = input_bytez+overlay
    return output_bytez
if __name__ == "__main__":
    input_file1 = r"D:\graduate_design\example1\source_file\sample1.exe"
    output_file1=r"D:\graduate_design\example1\operation_modules\process_remaster\example_debug\debug_result\sample1_result.exe"
    init_environment()
    clear_directory(r"D:\graduate_design\example1\operation_modules\process_remaster\example_debug\debug_result")
    # use for testing/debugging actions
    with open(input_file1, "rb") as f:
        bytez = f.read()
    m = hashlib.sha256()
    m.update(bytez)
    print(f"original hash: {m.hexdigest()}")
    bytez1_ =add_benign_data_overlay_depend_on_benign(bytez,r"D:\graduate_design\example1\benign_software")
    m = hashlib.sha256()
    m.update(bytez1_)

    with open(output_file1, "wb+") as f1:
        f1.write(bytez1_)
    print(f"modified hash: {m.hexdigest()}")