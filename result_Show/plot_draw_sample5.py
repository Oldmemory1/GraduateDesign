import matplotlib.pyplot as plt
import numpy as np

# 数据准备
software = ['ClamAV','360 antivirus with QVM', '360 antivirus without QVM', 'HuoRong']
before = [167, 292,291, 297]
after = [115, 218,32, 265]

# 设置柱状图参数
x = np.arange(len(software))  # 横坐标位置
width = 0.25  # 柱状图宽度

# 绘制柱状图
fig, ax = plt.subplots(figsize=(8, 6))
rects1 = ax.bar(x - width/2, before, width, label='before process', color='#1f77b4', edgecolor='black')
rects2 = ax.bar(x + width/2, after, width, label='after process', color='#ff7f0e', edgecolor='black')

# 添加标签和标题
ax.set_xlabel('antivirus software', fontsize=10,fontproperties='Times New Roman')
ax.set_ylabel('detect amount', fontsize=10,fontproperties='Times New Roman')
ax.set_title('sample5 detect amount compare', fontsize=10, pad=20,fontproperties='Times New Roman')
ax.set_xticks(x)
ax.set_xticklabels(software,fontproperties='Times New Roman')
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