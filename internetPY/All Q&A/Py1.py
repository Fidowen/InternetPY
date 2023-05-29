# 101
# 載入 json 與 csv 模組
import ___
import ___

# 讀取 json 檔案並指定編碼為 utf8
with ___("___", encoding='___') as file:
    data = json.load(file)

# 寫入 csv 檔案並指定編碼為 utf8
with ___("___", "___", encoding='___') as file:
    csv_file = csv.writer(file)
    # 寫入 title（活動名稱）、showUnit（演出單位）、startDate（活動起始日期）、endDate（活動結束日期）等四個欄位
    for item in data:
        csv_file.writerow([___['___'], ___['___'],
                           ___['___'], ___['___']])

#102
# 載入 xml.etree.ElementTree 模組並縮寫為 ET
import ___ as ___
# 載入 csv 模組
import ___

# 讀取 xml
tree = ___.___("___")
root = tree.getroot()

# 寫入 csv 檔案，編碼設定為 utf8
ubikefile = ___("___", "___", encoding='___')
csvwriter = csv.writer(ubikefile)

# 將其中 sno（站點代號）、sna（中文場站名稱）、tot（場站總停車格）等三個欄位寫出
for row in root:
    ubike = []
    sno = row.find('___').text
    ubike.append(___)
    sna = row.find('___').text
    ubike.append(___)
    tot = row.find('___').text
    ubike.append(___)
    csvwriter.writerow(ubike)
ubikefile.close()

#103
# 載入 yaml 與 json 模組
import ___
import ___

# 讀取 json 檔案
with ___("___", encoding='utf-8-sig') as file:
    data = ___.___(___)

# 寫入 yaml 檔案
with ___("___", "___", encoding="utf-8") as f:
    ___.___(data, f, default_flow_style=False, allow_unicode=True)


#104
# 載入 json 模組
import ___


# 建立資料
# 'id': '1'
# 'name': 'Peter'
# 'country': 'Taiwan'
#
# 'id': '2'
# 'name': 'Jack'
# 'country': 'USA'
#
# 'id': '3'
# 'name': 'Cindy'
# 'country': 'Japan'

# 將資料寫入json檔案
with ___('___', '___') as outfile:
    json.dump(___, ___)




#105
# 載入 sqlite3 模組
import ___

# 建立資料庫連結
con = ___.___('___')
# 建立cursor物件
___ = con.___

# 查詢Employee資料表
___.___("SELECT * FROM Employee")

# 印出查詢結果
for ___ in ___:
    print(___)

# 關閉與資料庫的連結
con.close()
