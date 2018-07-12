from urllib.request import urlopen
from urllib.request import Request  
import json
import urllib
import os
import re

f = open("recent.txt", "r")
recentTitle = f.readline()
recentListTitle = ""
f.close()

 
url = "http://torrents.ohys.net/download/json.php?dir=new"
downUrl = "http://torrents.ohys.net/download/"
data = urllib.request.urlopen(url).read()
data = data.decode("utf-8-sig")

aniList = json.loads(data)
cnt = 0

for ani in aniList:	
	title = ani["t"]
	link = ani["a"]
	
	if cnt == 0 :
		recentListTitle = title

	if title == recentTitle :
		break
	
	cnt = cnt+1

	print(title)
    
	rq = Request(downUrl + link)
	res = urlopen(rq)
	pdf = open("/media/lsh/MGTEC/torrent/"+title, 'wb')
	pdf.write(res.read())
	pdf.close()

f = open("recent.txt", "w")
f.write(recentListTitle)
f.close()
