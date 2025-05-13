import os

import lief

from operation_modules.findAllSignatures import get_all_file_paths


def dll_swift(benign_files_dir):
    has_text = 0
    benign_files = get_all_file_paths(benign_files_dir)
    for benign_file in benign_files:
        pe1 =lief.PE.parse(benign_file)
        text_section = pe1.get_section(
        ".text",
        ).content
        if text_section is None:
            os.remove(benign_file)
        else:
            has_text = has_text + 1
    print(f"hashed text: {has_text}")
if __name__ == '__main__':
    dll_swift(r"D:\graduate_design\example1\benign_software")