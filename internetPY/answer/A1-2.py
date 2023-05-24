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
    
