import matplotlib.pyplot as plt

# 数据处理
data = [
    ['malware1-before-process', 60],
    ['malware1-after-process', 43],
    ['malware2-before-process', 59],
    ['malware2-after-process', 39],
    ['malware3-before-process', 58],
    ['malware3-after-process', 36],
    ['malware4-before-process', 61],
    ['malware4-after-process', 38],
    ['malware5-before-process', 52],
    ['malware5-after-process', 41],
    ['malware6-before-process', 59],
    ['malware6-after-process', 45],
    ['malware7-before-process', 56],
    ['malware7-after-process', 34],
    ['malware8-before-process', 58],
    ['malware8-after-process', 35],
    ['malware9-before-process', 55],
    ['malware9-after-process', 37]
]

malwares = []
before = []
after = []

for entry in data:
    malware_full, value = entry
    parts = malware_full.split('-')
    malware_name = parts[0]
    process_stage = parts[1]

    if process_stage == 'before':
        malwares.append(malware_name)
        before.append(value)
    else:
        after.append(value)

# 绘图设置
x = range(len(malwares))  # x轴位置
width = 0.35  # 柱子宽度

fig, ax = plt.subplots(figsize=(8, 8))
rects1 = ax.bar([i - width / 2 for i in x], before, width, label='Before Process', color='#1f77b4')
rects2 = ax.bar([i + width / 2 for i in x], after, width, label='After Process', color='#ff7f0e')

# 添加标签和标题
ax.set_xlabel('malwares', fontsize=12,fontproperties='Times New Roman')
ax.set_ylabel('Virus Total Engine Detection Amount', fontsize=12,fontproperties='Times New Roman')
ax.set_title('Detection Results Before and After Processing', fontsize=14, pad=20,fontproperties='Times New Roman')
ax.set_xticks(x)
ax.set_xticklabels(malwares, rotation=0, ha='right',fontproperties='Times New Roman')
ax.legend()


# 在柱子上方显示数值
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

# 调整布局和样式
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()