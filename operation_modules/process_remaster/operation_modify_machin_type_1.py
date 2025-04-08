import random

import lief

from operation_modules.process_remaster.binary_to_bytez import binary_to_bytez


def modify_machine_type(bytez):
    candidate = [
        lief.PE.MACHINE_TYPES.AMD64,
        lief.PE.MACHINE_TYPES.IA64,
        lief.PE.MACHINE_TYPES.ARM64,
        lief.PE.MACHINE_TYPES.POWERPC,
    ]

    binary = lief.PE.parse(list(bytez))

    binary.header.machine = candidate[random.randint(0, len(candidate))]

    bytez1 = binary_to_bytez(binary)

    return bytez1