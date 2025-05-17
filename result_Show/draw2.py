import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['FangSong']
matplotlib.rcParams['axes.unicode_minus'] = False
import seaborn as sns
from matplotlib import pyplot as plt
sns.set(font='FangSong')
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 定义数据
rows = [
    ("样本集1-处理前-ClamAV", 211), ("样本集1-处理后-ClamAV", 139),
    ("样本集1-处理前-360杀毒开启QVM", 669), ("样本集1-处理后-360杀毒开启QVM", 511),
    ("样本集1-处理前-360杀毒不开启QVM", 668), ("样本集1-处理后-360杀毒不开启QVM", 28),
    ("样本集1-处理前-火绒杀毒", 670), ("样本集1-处理后-火绒杀毒", 608),
    ("样本集2-处理前-ClamAV", 163), ("样本集2-处理后-ClamAV", 96),
    ("样本集2-处理前-360杀毒开启QVM", 436), ("样本集2-处理后-360杀毒开启QVM", 295),
    ("样本集2-处理前-360杀毒不开启QVM", 436), ("样本集2-处理后-360杀毒不开启QVM", 34),
    ("样本集2-处理前-火绒杀毒", 439), ("样本集2-处理后-火绒杀毒", 399),
    ("样本集3-处理前-ClamAV", 130), ("样本集3-处理后-ClamAV", 85),
    ("样本集3-处理前-360杀毒开启QVM", 438), ("样本集3-处理后-360杀毒开启QVM", 349),
    ("样本集3-处理前-360杀毒不开启QVM", 438), ("样本集3-处理后-360杀毒不开启QVM", 146),
    ("样本集3-处理前-火绒杀毒", 431), ("样本集3-处理后-火绒杀毒", 416),
    ("样本集4-处理前-ClamAV", 183), ("样本集4-处理后-ClamAV", 123),
    ("样本集4-处理前-360杀毒开启QVM", 408), ("样本集4-处理后-360杀毒开启QVM", 285),
    ("样本集4-处理前-360杀毒不开启QVM", 407), ("样本集4-处理后-360杀毒不开启QVM", 25),
    ("样本集4-处理前-火绒杀毒", 405), ("样本集4-处理后-火绒杀毒", 305),
    ("样本集5-处理前-ClamAV", 167), ("样本集5-处理后-ClamAV", 115),
    ("样本集5-处理前-360杀毒开启QVM", 292), ("样本集5-处理后-360杀毒开启QVM", 218),
    ("样本集5-处理前-360杀毒不开启QVM", 291), ("样本集5-处理后-360杀毒不开启QVM", 32),
    ("样本集5-处理前-火绒杀毒", 297), ("样本集5-处理后-火绒杀毒", 265)
]

# 解析数据
cases_order = [
    ('处理前', 'ClamAV'), ('处理后', 'ClamAV'),
    ('处理前', '360杀毒开启QVM'), ('处理后', '360杀毒开启QVM'),
    ('处理前', '360杀毒不开启QVM'), ('处理后', '360杀毒不开启QVM'),
    ('处理前', '火绒杀毒'), ('处理后', '火绒杀毒')
]

sample_data = defaultdict(dict)
for key, value in rows:
    parts = key.split('-')
    sample_set = parts[0]
    process = parts[1]
    antivirus = parts[2]
    sample_data[sample_set][(process, antivirus)] = value

sample_sets = ['样本集1', '样本集2', '样本集3', '样本集4', '样本集5']
data_matrix = []
for sample_set in sample_sets:
    row = []
    for case in cases_order:
        process, antivirus = case
        value = sample_data[sample_set].get((process, antivirus), 0)
        row.append(value)
    data_matrix.append(row)

# 设置绘图参数
plt.figure(figsize=(18, 10))
colors = plt.cm.tab20(np.linspace(0, 1, 8))  # 使用8种不同颜色

# 绘制条形图
bar_width = 0.08
for i in range(5):  # 遍历每个样本集
    for k in range(8):  # 遍历每种情况
        x = i + (k - 3.5) * bar_width * 1.2  # 计算x坐标
        value = data_matrix[i][k]
        plt.bar(x, value, width=bar_width, color=colors[k])
        plt.text(x, value, f'{value}', ha='center', va='bottom', fontsize=8,fontproperties='FangSong')

# 设置坐标轴和标签
plt.xticks(range(5), sample_sets, fontsize=12,fontproperties='FangSong')
plt.ylabel('样本查杀数量', fontsize=14,fontproperties='FangSong')
plt.title('各样本集查杀数量统计', fontsize=16,fontproperties='FangSong')

# 创建图例
legend_labels = [
    'ClamAV-处理前', 'ClamAV-处理后',
    '360杀毒开启QVM-处理前', '360杀毒开启QVM-处理后',
    '360杀毒不开启QVM-处理前', '360杀毒不开启QVM-处理后',
    '火绒-处理前', '火绒-处理后'
]
plt.legend(legend_labels, title='检测方式', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()