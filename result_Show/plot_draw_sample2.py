import matplotlib.pyplot as plt
import numpy as np

# 数据准备
software = ['ClamAV','360杀毒-开启QVM2杀毒引擎', '360杀毒-不开启QVM2杀毒引擎', '火绒']
before = [163, 436,436, 439]
after = [96, 295,34, 399]

# 设置柱状图参数
x = np.arange(len(software))  # 横坐标位置
width = 0.35  # 柱状图宽度

# 绘制柱状图
fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, before, width, label='before process', color='#1f77b4', edgecolor='black')
rects2 = ax.bar(x + width/2, after, width, label='after process', color='#ff7f0e', edgecolor='black')

# 添加标签和标题
ax.set_xlabel('杀毒软件', fontsize=12,fontproperties='FangSong')
ax.set_ylabel('样本查杀数量', fontsize=12,fontproperties='FangSong')
ax.set_title('样本集sample2免杀处理前后的查杀数量', fontsize=14, pad=20,fontproperties='FangSong')
ax.set_xticks(x)
ax.set_xticklabels(software,fontproperties='FangSong')
ax.legend()

# 在柱子上方显示数值
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width()/2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)

# 调整布局
plt.tight_layout()
plt.show()