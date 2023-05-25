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