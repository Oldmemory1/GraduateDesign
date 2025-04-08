# 添加无害的数据
# 可以从生成的字符串数组中随机取出一个
def append_benign_data_overlay(bytez,appended_data):
    # print
    s1 = appended_data
    overlay = bytearray(s1, encoding="utf-8")
    # print(overlay)
    bytez1 = bytez + overlay
    return bytez1