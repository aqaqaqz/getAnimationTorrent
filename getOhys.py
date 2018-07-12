from urllib.request import urlopen
from urllib.request import Request  
import json
import urllib

 
url = "http://torrents.ohys.net/download/json.php?dir=new"
downUrl = "http://torrents.ohys.net/download/"
data = urllib.request.urlopen(url).read()
data = data.decode("utf-8-sig")

aniList = json.loads(data)
for ani in aniList:
    title = ani["t"]
    link = ani["a"]
    
    print(title)
    
    rq = Request(downUrl + link)
    res = urlopen(rq)
    pdf = open("c:/testfolder/temp/"+title, 'wb')
    pdf.write(res.read())
    pdf.close()

