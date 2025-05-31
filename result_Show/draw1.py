import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 数据准备
labels = ['sample1', 'sample2', 'sample3', 'sample4', 'sample5']
original = [211, 163, 130, 183, 167]
rl_model = [139, 96, 85, 123, 115]
psp_mal = [182, 140, 105, 170, 141]

x = np.arange(len(labels))  # 样本集位置
width = 0.20  # 条形宽度

# 创建图形
fig, ax = plt.subplots(figsize=(8, 8))

# 绘制条形图
rects1 = ax.bar(x - width, original, width, label='origin', color='#1f77b4')
rects2 = ax.bar(x, rl_model, width, label='this lab', color='#ff7f0e')
rects3 = ax.bar(x + width, psp_mal, width, label='psp-mal', color='#2ca02c')

# 添加标签、标题和图例
ax.set_xlabel('samples', fontsize=12,fontproperties='Times New Roman')
ax.set_ylabel('detect amount', fontsize=12,fontproperties='Times New Roman')
ax.set_title('detect amount of different models', fontsize=14, pad=20,fontproperties='Times New Roman')
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=10,fontproperties='Times New Roman')
ax.legend(fontsize=10)

# 在条形顶部显示数值
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 垂直偏移3点
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=10,fontproperties='Times New Roman')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

# 调整布局
plt.tight_layout()
plt.show()