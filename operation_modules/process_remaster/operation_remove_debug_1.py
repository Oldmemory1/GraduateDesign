import lief

from operation_modules.process_remaster.binary_to_bytez import binary_to_bytez


def remove_debug(bytez):
    bytez1 = bytez
    binary = lief.PE.parse(list(bytez))
    if binary.has_debug:
        for i, e in enumerate(binary.data_directories):
            if e.type == lief.PE.DATA_DIRECTORY.DEBUG:
                e.rva = 0
                e.size = 0
                bytez1 = binary_to_bytez(binary)
                return bytez1
    # no debug found
    return bytez1