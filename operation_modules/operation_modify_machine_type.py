import warnings

import pefile

def modify_pe_machine(input_file, output_file, new_machine):
    warnings.warn("deprecated because it broken the pe file!",DeprecationWarning)
    # 加载 PE 文件
    pe = pefile.PE(input_file)

    # 修改 Machine 类型
    pe.FILE_HEADER.Machine = new_machine

    # 根据 Machine 类型调整 Magic 字段
    if new_machine == 0x8664:  # x64
        pe.OPTIONAL_HEADER.Magic = 0x20b
    elif new_machine == 0x14c:  # x86
        pe.OPTIONAL_HEADER.Magic = 0x10b

    # 保存修改后的文件
    pe.write(output_file)
    pe.close()

# 示例：将文件改为 x64 架构
modify_pe_machine(
    input_file="../HelloWorld1.exe",
    output_file="output.exe",
    new_machine=0x8664  # x64 的 Machine 类型
)