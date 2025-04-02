import subprocess

# 执行命令并捕获输出
result = subprocess.run(
    ['ipconfig'],         # 命令及参数（列表形式）
    shell=True,            # 通过shell执行（Windows需要）
    text=True,             # 以文本形式返回输出（Python 3.7+）
    capture_output=True    # 捕获stdout和stderr
)

# 打印命令输出
print("标准输出：", result.stdout)
if result.stderr:
    print("错误信息：", result.stderr)