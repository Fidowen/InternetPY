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
