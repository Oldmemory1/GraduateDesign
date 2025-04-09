import random
import warnings

import lief

from operation_modules.process_remaster.binary_to_bytez import binary_to_bytez

# completed 已测试完成
def modify_machine_type(bytez):
    warnings.warn("temporarily deprecated because it may break the pe file!", DeprecationWarning)
    candidate = [
        lief.PE.MACHINE_TYPES.AMD64,
        lief.PE.MACHINE_TYPES.IA64,
        lief.PE.MACHINE_TYPES.ARM64,
        lief.PE.MACHINE_TYPES.POWERPC,
    ]

    binary = lief.PE.parse(list(bytez))

    binary.header.machine = candidate[random.randint(0, len(candidate)-1)]

    bytez1 = binary_to_bytez(binary)

    return bytez1