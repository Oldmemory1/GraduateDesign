import random
import random
import string

import lief

from operation_modules.process_remaster.binary_to_bytez import binary_to_bytez
from operation_modules.process_remaster.commons import ALL_SECTION_NAMES
from string1 import str1
from string_generator.generated_strings.get_a_random_string_from_strings import get_random_string

# completed 已测试完成
def add_section_benign_data(bytez,string_list):

    s1 = get_random_string(string_list=string_list)
    benign_binary_section_content = bytearray(s1, encoding="utf-8")

    binary = lief.PE.parse(list(bytez))

    current_section_names = [section.name for section in binary.sections]
    available_section_names = list(
        set(ALL_SECTION_NAMES) - set(current_section_names),
    )

    if len(available_section_names) == 0:
        available_section_names = random.choice(string.ascii_lowercase)

    section = lief.PE.Section(random.choice(available_section_names))
    section.content = benign_binary_section_content
    binary.add_section(section, lief.PE.SECTION_TYPES.DATA)

    bytez1 = binary_to_bytez(binary)
    return bytez1