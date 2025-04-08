import random

import lief

from operation_modules.process_remaster.binary_to_bytez import binary_to_bytez
from operation_modules.process_remaster.commons import COMMON_SECTION_NAMES


def rename_section(bytez):
    binary = lief.PE.parse(list(bytez))
    targeted_section = random.choice(binary.sections)
    # targeted_section.name = random.choice(COMMON_SECTION_NAMES)[:5]
    targeted_section.name = COMMON_SECTION_NAMES[random.randint(0, len(COMMON_SECTION_NAMES) - 1)]
    bytez1 = binary_to_bytez(binary)
    return bytez1