#101
import pandas as pd
df = pd.read_json("read.json")
df = df[['title','showUnit','startDate','endDate']]
df.to_csv('write.csv',header=False,index=False)












#102
import csv
import xml.etree.ElementTree as et
tree = et.parse('read.xml')
root = tree.getroot()

ubikefile = open('write.csv','w',newline='',encoding="utf-8")
csvwriter = csv.writer(ubikefile)

for row in root:
    ubike = []
    sno = row.find('sno').text
    ubike.append(sno)
    sna = row.find('sna').text
    ubike.append(sna)
    tot = row.find('tot').text
    ubike.append(tot)
    csvwriter.writerow(ubike)
ubikefile.close()








#103
import yaml
import json

with open('read.json',encoding='utf-8-sig') as file:
    data = json.load(file)

with open ('write.yaml','w',encoding="utf-8")as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)




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