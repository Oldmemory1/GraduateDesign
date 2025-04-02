import pefile


def modify_pe_machine(input_file, output_file, machine_value, magic_value=None):
    try:
        pe = pefile.PE(input_file)

        # 修改Machine字段
        pe.FILE_HEADER.Machine = machine_value

        # 可选：修改Magic值（例如64位架构使用0x20B）
        if magic_value is not None:
            pe.OPTIONAL_HEADER.Magic = magic_value

        # 保存修改后的文件
        pe.write(output_file)
        print(f"文件已成功保存为：{output_file}")

    except Exception as e:
        print(f"发生错误：{e}")

"""
# 示例：修改为AMD64（64位架构）
modify_pe_machine(
    input_file='input.exe',
    output_file='output_amd64.exe',
    machine_value=0x8664,
    magic_value=0x20B  # 确保Magic与架构匹配
)

# 示例：修改为ARM64（64位）
modify_pe_machine(
    input_file='input.exe',
    output_file='output_arm64.exe',
    machine_value=0xAA64,
    magic_value=0x20B
)
# 示例：修改为POWERPC（32位，Magic应为0x10B）
modify_pe_machine(
    input_file='input.exe',
    output_file='output_ppc.exe',
    machine_value=0x01F0,
    magic_value=0x10B
)
"""

if __name__ == "__main__":
    modify_pe_machine(
        input_file='HelloWorld1.exe',
        output_file='output_amd64.exe',
        machine_value=0x8664,
        magic_value=0x20B  # 确保Magic与架构匹配
    )
# 示例：修改为AMD64（64位架构）
