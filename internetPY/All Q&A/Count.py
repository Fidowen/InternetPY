#104
import json

data = {
'people' :
[{  
    'id': '1',
    'name': 'Peter',
    'country': 'Taiwan'
},
{  
    'id': '2',
    'name': 'Jack',
    'country': 'USA'
},
{  
    'id': '3',
    'name': 'Cindy',
    'country': 'Japan'
}]
}
with open ('write.json','w') as outfile:
    json.dump(data,outfile)

#105
import sqlite3

con = sqlite3.connect('read.db')
# 建立cursor物件
c = con.cursor()

# 查詢Employee資料表
data=c.execute("SELECT * FROM Employee")

# 印出查詢結果
for i in data.fetchall():
    print(i)

# 關閉與資料庫的連結
con.close()


#------------------------------------------------------------------------------------------
#203
import bs4
import requests

url = 'https://www.codejudger.com/target/5203.html'
r = requests.get(url)

soup = bs4.BeautifulSoup(r.text,'lxml')
dataTag = soup.select('.contents_box02')

balls = dataTag[2].find_all('div',{'class':'ball_tx ball_yellow'})
print("大樂透開獎 : ")
print('-------------')

print("開出順序 : ", end='')
for i in range(6):
    print(balls[i].text, end='   ')


print("\n大小順序 : ", end='')
for i in range(6, len(balls)):
    print(balls[i].text, end='   ')


redball = dataTag[2].find_all('div', {'class': 'ball_red'})
print("\n特別號   :", redball[0].text)



#204
import requests
import json

url ='https://www.codejudger.com/target/5204.json'
res = requests.get(url)

data = json.loads(res.text)

print('新北市大專院校名單：\n')
for record in data:
    if record['type'] == '大專院校':
        print('名稱：%s' % record['name'])
        print('地址：%s' % record['address'])
        print('聯絡電話：%s' % record['tel'])
        print('網站：%s' % record['website'])
        print('資料更新時間：%s' % record['update_date'])
        print()



#------------------------------------------------------------------------------------------
#303
# 載入 pandas 模組縮寫為 pd
import pandas as pd

#　建構資料
datas = [[9, 203674, 13.2, 18894],
       [11.7, 180785, 12.3, 54894],
       [10.1, 127802, 14.7, 18563],
       [11.8, 28604, 14.9, 21963],
       [13.2, 600, 13.1, 900],
       [6.9, 38071, 9.6, 3555],
       [12.1, 35660, 10.6, 9005],
       [12, 15000, 13, 12000],
       [11.7, 48770, 9.1, 14370],
       [9.84, 6100, 11.89, 8980]]
indexs = ["三重市", "台中市", "台北一", "台北二", "台東市", "板橋區", "高雄市", "嘉義市", "鳳山區", "豐原區"]
columns = ["西瓜價", "西瓜量", "香瓜價", "香瓜量"]

df = pd.DataFrame(datas, columns=columns,  index=indexs)
print('西瓜與香瓜之拍賣行情價量表')
print(df)
print()  # 使用print分隔


df1 = df.sort_values(by="西瓜價", ascending=False)
print('以西瓜價遞減排序')
print(df1['西瓜價'])
print()  # 使用print分隔

# 計算台北一市場西瓜/香瓜價量的行情並輸出
df.loc["台北一"]
print('台北一市場的行情')
print(df.loc["台北一"])
print()  # 使用print分隔

indexs[0] = "三重區"
df.index = indexs
columns[2] = "洋香瓜價"
columns[3] = "洋香瓜量"
df.columns = columns
print('全體市場行情')
print(df)


#304
import numpy as np

import pandas  as pd

data = pd.read_csv('read.csv')
data = np.array(data['data'])


# 判斷資料型態
print('資料型態：%s' % type(data))
# 計算平均數
print('平均值：%.2f' % np.mean(data))
# 計算中位數
print('中位數：%.2f' % np.median(data))
# 計算標準差
print('標準差：%.2f' % np.std(data))
# 計算變異數
print('變異數：%.2f' % np.var(data))
# 計算極差值
print('極差值：%.2f' % np.ptp(data))

#------------------------------------------------------------------------------------------
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

