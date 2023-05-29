#201
import requests
import re
url = 'https://www.codejudger.com/target/5201.html'
htmlfile = requests.get(url)

if htmlfile.status_code == 200:
    htmlfile.encoding='utf-8'
    s = input("請輸入欲搜尋的字串 : ")
    print (s+' 搜尋成功')
    n = len(re.findall(s, htmlfile.text))
    print (s,'出現', n,'次' )












#202
import pandas as pd

df = pd.read_html('read.html')
df = df[1]
df.to_csv('write.csv',index=False,encoding='utf-8',float_format='%.3f')

































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








#205
import requests
import json

url = 'https://www.codejudger.com/target/5205.json'
res = requests.get(url)
print('Content-Length:',len(res.content))
res = json.loads(res.text)

print()

print('新北市PM2.5相關資料：')
for record in res:
    if record['County'] == '新北市':
        print('%s：' % record['SiteName'])
        print('\tAQI：%s' % record['AQI'])
        print('\tPM2.5：%s' % record['PM2.5'])
        print('\tPM10：%s' % record['PM10'])
        print('\t資料更新時間：%s' % record['PublishTime'])
