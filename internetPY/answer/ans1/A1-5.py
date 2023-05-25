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