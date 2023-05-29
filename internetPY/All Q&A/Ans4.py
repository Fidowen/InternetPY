#401
import matplotlib as mpl
mpl.use('Agg')
# --結束--批改評分使用，請勿變動

# 載入 matplotlib.pyplot 並縮寫為 plt
import matplotlib.pyplot as plt

data1 = [1, 4, 9, 16, 25, 36, 49, 64]
data2 = [1, 2, 3, 6, 9, 15, 24, 39]
seq = [1, 2, 3, 4, 5, 6, 7, 8]

# 數據及線條設定
plt.plot(seq, data1, 'bo--', seq, data2, 'ro--', ms =3,lw =1)
# 軸刻度
plt.axis([0,8,0,70])
# 圖表標題
plt.title('Figure',fontsize = 24)
# X軸標題
plt.xlabel('x-Value',fontsize = 16)
# Y軸標題
plt.ylabel('y-Value',fontsize = 16)

# 輸出圖片檔案
plt.savefig('chart.png')
plt.close()




#402
# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
# --結束--批改評分使用，請勿變動

# 載入 matplotlib.pyplot 並縮寫為 plt
import matplotlib.pyplot as plt
# 載入 csv 模組
import csv

x = []
y = []

# 讀入 read.csv
with open('read.csv', 'r', encoding='utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(float(row[1]))

x_ticks = range(1, len(x) + 1)
plt.plot(x_ticks, y, label= 'banana')
plt.xticks(x_ticks, x)
plt.xlabel('date')
plt.ylabel('NT$')
plt.ylim(15,25)
# 添加圖表標題 title()
plt.title('Market Average Price')
plt.legend()
# 使用 savefig() 函數
plt.savefig('chart.png')
plt.close()


#403
# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
# --結束--批改評分使用，請勿變動

# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

# 四個月份
labels = ['Jun', 'Jul', 'Aug', 'Sep']
sizes = [20, 30, 40, 10]
# 圓餅圖顏色
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

# 長條圖 位置
plt.subplot(1, 2, 1)
xticks = range(1, len(labels) + 1)
# 長條圖以labels為X軸，sizes為Y軸，各長條顏色為藍色（blue）
plt.xticks(xticks,labels)
plt.bar(xticks, sizes, color='blue')

# 圓餅圖 位置
plt.subplot(1, 2, 2)
# 圓餅圖以labels為圖標，sizes為各項所占百分比
# 圓餅圖colors為各項顏色，突顯「Aug」
# 圓餅圖顯示各項百分比到小數點第1位
explode = (0, 0, 0.1, 0)
plt.pie(sizes, explode=explode, labels=labels,
        colors=colors, autopct='%2.1f%%')
# 長寬比為1:1
plt.axis('equal')

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
df = pd.read_csv('read.csv')
scores = df["scores"].values

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
index = np.arange(0, 25, 5)
# X軸刻度
labels = ['0~19', '20~39', '40~59', '60~79', '80~100']
# 畫出長條圖
plt.bar(index, range_count, width=2)
# 設定X軸名稱
plt.xlabel('Range', fontsize=14)
# 設定Y軸名稱
plt.ylabel('Quantity', fontsize=14)
# 設定x軸標籤
plt.xticks(index, labels)
# 設定y軸標籤
plt.yticks(index)
# 設定圖名稱
plt.title('Score ranges count', fontsize=20)
# 輸出圖片檔案
plt.savefig('chart.png')
plt.close()


#405
# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
set_seed = 123
# --結束--批改評分使用，請勿變動

# 載入 numpy 模組並縮寫為 np
import numpy as np
# 載入 matplotlib.pyplot 並縮寫為 plt
import matplotlib.pyplot as plt

samples_1 = np.random.RandomState(set_seed).normal(loc=1, scale=.5, size=1000)
samples_2 = np.random.RandomState(set_seed).standard_t(df=10, size=1000)
bins = np.linspace(-3, 3, 100)

# 第一個子圖
plt.subplot(2, 2, 1)
plt.hist(samples_1, bins=bins, alpha=0.5, label='samples 1')
plt.hist(samples_2, bins=bins, alpha=0.5, label='samples 2')
# 在左上角 upper left 放置圖例 legend
plt.legend(loc='upper left')

# 第二個子圖
plt.subplot(1, 2, 2)
plt.scatter(samples_1, samples_2, alpha=0.2)

plt.savefig('chart.png')
plt.close()
