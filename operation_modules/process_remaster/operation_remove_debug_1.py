import lief

from operation_modules.process_remaster.binary_to_bytez import binary_to_bytez

# completed 已测试完成
# 删除调试信息 可能因为没有调试信息导致操作无效
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