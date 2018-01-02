from urllib.request import urlopen
from urllib.request import Request  
from bs4 import BeautifulSoup

import re
import datetime

url = "http://leopard-raws.org"
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")

list = soup.findAll(name="div", attrs={"class":"block-sceleton"})
pattern_date = re.compile("\d\d\d\d/\d\d/\d\d")

for ani in list:
    a_tag = ani.findChild("div", attrs={"class":"torrent_name"})
    info = ani.findChild("div", attrs={"class":"info"})
    title = a_tag.findChild("a").get_text()

    up_date = pattern_date.search( info.get_text().strip()).group(0).replace("/", "-") 
    today = datetime.date.today() - datetime.timedelta(4)

    if up_date == today.__str__():
        print(up_date + ",  " + today.__str__())
        rq = Request(url + a_tag.findChild("a")["href"].replace("./download", "/download"))
        res = urlopen(rq)
        pdf = open("c:/testfolder/temp/"+title+".torrent", 'wb')
        pdf.write(res.read())
        pdf.close()
    elif up_date < today.__str__():
        break;