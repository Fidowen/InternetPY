#201
# 載入模組
import ___
import ___

url = '___'

# 使用 GET 請求
htmlfile = requests.___(___)
# 驗證HTTP Status Code
if htmlfile.status_code == ___:
    # 欲搜尋的字串
    ___ = input("請輸入欲搜尋的字串 : ")
    ___ = re.findall(___, htmlfile.text)
    if ___ in htmlfile.text:
        print(___, "搜尋成功")
        print(___, "出現 %d 次" % len(___))
    else:
        print(___, "搜尋失敗")
        print(___, "出現 0 次")
else:
    print("網頁下載失敗")


#202
# 載入 csv 模組
import csv
# 自 urllib.request 模組載入 urlopen 函數
from ___ import ___
# 自 bs4 模組載入 BeautifulSoup 函數
from ___ import ___


# 將資料寫入csv檔案，編碼為 utf8
file_name = "___"
f = open(file_name, "w", encoding='___')
# 以 csv 模組的 writer 函數初始化寫檔
w = ___.___(f)

# 爬取的目標網頁
htmlname = "___"
# urlopen 函數讀取 html 檔案
html = urlopen(___)
# 指定 BeautifulSoup 的解析器為 lxml
bsObj = BeautifulSoup(html, "___")

count = 0
# 將其中日期、NTD/USD 兩個欄位的名稱與資料轉存為csv
# 資料位置
for single_tr in bsObj.find("___", {"class": "___"}).findAll("___"):
    if count == 0:
        # 擷取資料位置
        cell = single_tr.findAll("___")
    else:
        # 擷取資料位置
        cell = single_tr.findAll("___")
    F0 = cell[0].text
    F1 = cell[1].text
    data = [[F0, F1]]
    w.writerows(data)
    count = count + 1
f.close()

#203
# -*- coding: utf-8 -*-

import ___
import requests

url = '___'
# GET 請求
html = requests.___(___)

# 使用 lxml 解析器
objSoup = bs4.BeautifulSoup(html.text, '___')

dataTag = objSoup.select('.contents_box02')

balls = dataTag[2].find_all('___', {'class': '___'})
print("大樂透開獎 : ")
print('-------------')

# 開出順序
print("開出順序 : ", end='')
for i in range(6):
    print(____.____, end='   ')

# 大小順序
print("\n大小順序 : ", end='')
for i in range(6, len(balls)):
    print(____.____, end='   ')

# 特別號：資料位於 <div class="ball_red"></div>
redball = dataTag[2].find_all('___', {'class': '___'})
print("\n特別號   :", ____)


#204
# 載入 requests 模組
import ___
# 載入 json 模組
import ___

# 開放資料連結
url = '____'
# 以 requests 模組發出 HTTP GET 請求
res = ___.___(url)

# 將回傳結果轉換成標準JSON格式
data = json.loads(res.text)

# 輸出新北市大專院校名單
print('新北市大專院校名單：\n')
for record in data:
    if record['type'] == '大專院校':
        print('名稱：%s' % record['___'])
        print('地址：%s' % record['___'])
        print('聯絡電話：%s' % record['___'])
        print('網站：%s' % record['___'])
        print('資料更新時間：%s' % record['___'])
        print()


#205
# 載入 requests 與 json 模組
import ___
import ___

# 開放資料Json格式連結
url = ___
# 發出Get請求
response = ___
# 回傳內容長度
print(___, ___)
# 將取得的回傳內容轉換成Json格式
response = ___

print()

# 顯示新北市每一個地區的PM2.5相關資料
print('新北市PM2.5相關資料：')
for record in response:
    if record['County'] == '___':
        print('%s：' % record['___'])
        print('AQI：%s' % record['___'])
        print('PM2.5：%s' % record['___'])
        print('PM10：%s' % record['___'])
        print('資料更新時間：%s' % record['___'])
