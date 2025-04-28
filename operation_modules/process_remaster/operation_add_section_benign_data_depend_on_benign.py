import hashlib
import random
import string

import lief
import pefile

from init.clear_directory import clear_directory
from init.reset_test_enviroment import init_environment
from operation_modules.findAllSignatures import get_all_file_paths
from operation_modules.process_remaster.binary_to_bytez import binary_to_bytez
from operation_modules.process_remaster.commons import ALL_SECTION_NAMES
from string_generator.generated_strings.get_a_random_string_from_strings import get_random_string


def add_section_benign_data_depend_on_benign(input_bytez, benign_files_dir):
    benign_files = get_all_file_paths(benign_files_dir)
    select_file = random.randint(0,len(benign_files)-1)
    #print(benign_files[select_file])
    pe1 = lief.PE.parse(benign_files[select_file])
    benign_binary_section_content = pe1.get_section(
        ".text",
    ).content

    binary = lief.PE.parse(list(input_bytez))

    current_section_names = [section.name for section in binary.sections]
    available_section_names = list(
        set(ALL_SECTION_NAMES) - set(current_section_names),
    )

    if len(available_section_names) == 0:
        available_section_names = random.choice(string.ascii_lowercase)
    name1 = random.choice(available_section_names)
    #print(name1)
    section = lief.PE.Section(name1)

    section.content = benign_binary_section_content
    binary.add_section(section, lief.PE.SECTION_TYPES.DATA)

    bytez1 = binary_to_bytez(binary)
    return bytez1
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
    bytez1_ =add_section_benign_data_depend_on_benign(bytez,r"D:\graduate_design\example1\benign_software")
    m = hashlib.sha256()
    m.update(bytez1_)

    with open(output_file1, "wb+") as f1:
        f1.write(bytez1_)
    print(f"modified hash: {m.hexdigest()}")