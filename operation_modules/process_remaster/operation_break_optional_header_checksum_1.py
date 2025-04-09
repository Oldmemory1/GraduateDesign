import lief

from operation_modules.process_remaster.binary_to_bytez import binary_to_bytez


def break_optional_header_checksum(bytez):
    binary = lief.PE.parse(list(bytez))
    binary.optional_header.checksum = 0
    bytez1 = binary_to_bytez(binary)
    return bytez1