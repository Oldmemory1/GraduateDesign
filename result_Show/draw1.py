import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 数据准备
labels = ['样本集1', '样本集2', '样本集3', '样本集4', '样本集5']
original = [211, 163, 130, 183, 167]
rl_model = [139, 96, 85, 123, 115]
psp_mal = [182, 140, 105, 170, 141]

x = np.arange(len(labels))  # 样本集位置
width = 0.22  # 条形宽度

# 创建图形
fig, ax = plt.subplots(figsize=(14, 7))

# 绘制条形图
rects1 = ax.bar(x - width, original, width, label='不采用模型的原始样本', color='#1f77b4')
rects2 = ax.bar(x, rl_model, width, label='使用本实验的强化学习模型处理', color='#ff7f0e')
rects3 = ax.bar(x + width, psp_mal, width, label='使用psp-mal模型处理', color='#2ca02c')

# 添加标签、标题和图例
ax.set_xlabel('选用样本集', fontsize=12,fontproperties='FangSong')
ax.set_ylabel('样本查杀数量', fontsize=12,fontproperties='FangSong')
ax.set_title('不同样本集和模型类型的样本查杀数量统计', fontsize=14, pad=20,fontproperties='FangSong')
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=10,fontproperties='FangSong')
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
                    fontsize=8,fontproperties='FangSong')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

# 调整布局
plt.tight_layout()
plt.show()