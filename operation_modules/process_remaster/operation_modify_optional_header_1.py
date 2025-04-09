import random

import lief

from operation_modules.process_remaster.binary_to_bytez import binary_to_bytez

# completed 已测试完成
def modify_optional_header(bytez):
    binary = lief.PE.parse(list(bytez))

    oh = {
        "major_linker_version": [2, 6, 7, 9, 11, 14],
        "minor_linker_version": [0, 16, 20, 22, 25],
        "major_operating_system_version": [4, 5, 6, 10],
        "minor_operating_system_version": [0, 1, 3],
        "major_image_version": [0, 1, 5, 6, 10],
        "minor_image_version": [0, 1, 3],
    }

    keys = list(oh.keys())
    key = keys[random.randint(0, len(keys) - 1)]

    modified_val = random.choice(oh[key])
    binary.optional_header.__setattr__(key, modified_val)

    bytez1 = binary_to_bytez(binary)
    return bytez1