#401
# -*- coding: utf-8 -*-
# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
# --結束--批改評分使用，請勿變動

# 載入 matplotlib.pyplot 並縮寫為 plt
import ___ as ___

data1 = [1, 4, 9, 16, 25, 36, 49, 64]
data2 = [1, 2, 3, 6, 9, 15, 24, 39]
seq = [1, 2, 3, 4, 5, 6, 7, 8]

# 數據及線條設定
plt.plot(seq, ___, ___, seq, ___, ___, ___)
# 軸刻度
plt.axis(___)
# 圖表標題
plt.title(___)
# X軸標題
plt.xlabel(___)
# Y軸標題
plt.ylabel(___)

# 輸出圖片檔案
plt.savefig('___')
plt.close()


#402
# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
# --結束--批改評分使用，請勿變動

# 載入 matplotlib.pyplot 並縮寫為 plt
import ___ as ___
# 載入 csv 模組
import ___

x = []
y = []

# 讀入 read.csv
with open('___', 'r', encoding='utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(float(row[1]))

x_ticks = range(1, len(x) + 1)
plt.___(x_ticks, y, label=___)
plt.xticks(x_ticks, x)
plt.xlabel(___)
plt.ylabel(___)
plt.ylim(___)
# 添加圖表標題 title()
plt.___('Market Average Price')
plt.legend()
# 使用 savefig() 函數
plt.___('chart.png')
plt.close()


#403
# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
# --結束--批改評分使用，請勿變動

# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

# 四個月份
labels = [__, __, __, __]
sizes = [20, 30, 40, 10]
# 圓餅圖顏色
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

# 長條圖 位置
plt.subplot(1, 2, ___)
xticks = range(1, len(labels) + 1)
# 長條圖以labels為X軸，sizes為Y軸，各長條顏色為藍色（blue）
plt.xticks(xticks, ___)
plt.bar(___, ___, color=___)

# 圓餅圖 位置
plt.subplot(1, 2, ___)
# 圓餅圖以labels為圖標，sizes為各項所占百分比
# 圓餅圖colors為各項顏色，突顯「Aug」
# 圓餅圖顯示各項百分比到小數點第1位
explode = (0, 0, 0.1, 0)
plt.pie(___, explode=___, labels=___,
        colors=___, autopct='___')
# 長寬比為1:1
plt.axis('___')

plt.savefig('chart.png')
plt.close()


#404
# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
# --結束--批改評分使用，請勿變動

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# 讀取學生分數資料
# 讀取 read.csv
df = ___(___)
scores = df["___"].values

# range_count[0]: range0~19
# range_count[1]: range20~39
# range_count[2]: range40~59
# range_count[3]: range60~79
# range_count[4]: range80~100
# 以0初始化計數串列
range_count = [0] * 5

# 計數過程
for score in scores:
    if score < 20:
        range_count[0] += 1
    elif score < 40:
        range_count[1] += 1
    elif score < 60:
        range_count[2] += 1
    elif score < 80:
        range_count[3] += 1
    else:
        range_count[4] += 1

# y軸標籤
index = np.arange(___, ___, ___)
# X軸刻度
labels = [___, ___, '40~59', ___, '80~100']
# 畫出長條圖
plt.bar(___, range_count, ___)
# 設定X軸名稱
plt.xlabel('___', fontsize=___)
# 設定Y軸名稱
plt.ylabel('___', fontsize=___)
# 設定x軸標籤
plt.xticks(index, labels)
# 設定y軸標籤
plt.yticks(index)
# 設定圖名稱
plt.title('___', fontsize=___)
# 輸出圖片檔案
plt.___('___')
plt.close()


#405
# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
set_seed = 123
# --結束--批改評分使用，請勿變動

# 載入 numpy 模組並縮寫為 np
import ___ as ___
# 載入 matplotlib.pyplot 並縮寫為 plt
import ___ as ___

samples_1 = np.random.RandomState(set_seed).normal(loc=1, scale=.5, size=1000)
samples_2 = np.random.RandomState(set_seed).standard_t(df=10, size=1000)
bins = np.linspace(___, ___, ___)

# 第一個子圖
plt.subplot(___, ___, ___)
plt.hist(___, bins=___, alpha=___, label='___')
plt.hist(___, bins=___, alpha=___, label='___')
# 在左上角 upper left 放置圖例 legend
plt.___(loc='___')

# 第二個子圖
plt.subplot(___, ___, ___)
plt.scatter(___, ___, alpha=___)

plt.savefig(___)
plt.close()
