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