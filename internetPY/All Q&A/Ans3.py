#301
import pandas  as pd

datas = [[75, 62, 85, 73, 60], [91, 53, 56, 63, 65],
         [71, 88, 51, 69, 87], [69, 53, 87, 74, 70]]
indexs = ["小林", "小黃", "小陳", "小美"]
columns = ["國語", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)

print('行標題為科目，列題標為個人的所有學生成績')
print(df)
print()


print('後二位的成績')
print(df[-2:])
print()

df1 = df.sort_values(by="自然", ascending=False)
print('以自然遞減排序')
print(df1['自然'])
print()

df.loc["小黃", "英文"] = 80
print('小黃的成績')
print(df.loc['小黃'])

#302
set_seed = 123

import numpy as np

x = np.random.RandomState(set_seed).randint(low=5, high=16, size=15)
print('隨機正整數：', x)

x = x.reshape(3, 5)
print('X矩陣內容：')
print(x)
print('最大：', np.max(x))
print('最小：', np.min(x))
print('總和：', np.sum(x))
print('四個角落元素：')
print(x[np.ix_([0, -1], [0, -1])])

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


#305
import pandas as pd

# 讀取csv檔
df1 = pd.read_csv('read.csv', encoding="utf-8", sep=",", header=0)

# 居住縣市病例人數，並按遞減順序顯示
df_county = df1.groupby("居住縣市")["居住縣市"].count()
print(df_county.sort_values(ascending = False))

# 顯示感染病例人數最多的5個國家，並按遞減順序顯示
df_country = df1.groupby("感染國家")["感染國家"].count()
print(df_country.sort_values(ascending = False).head())

# 台北市各區病例人數
df_taipei = df1[df1.居住縣市 == "台北市"]
print(df_taipei.groupby("居住鄉鎮")["居住鄉鎮"].count())

# 台北市最近病例的日期
print("發病日: " + df_taipei.發病日.max())
