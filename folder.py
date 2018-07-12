import os
import glob
import shutil
import re
import pickle
import datetime

readF = open('./list.txt', 'rb')
add = False

list = [[0 for col in range(100)] for row in range(50)]
list = pickle.load(readF)
#print(list)

readF.close()

def makeDir(nm):
    check = True
    for f in os.listdir("./"):
        if f == nm:
            check = False
 
    return check

def getQuarterNm(fNm):
    for season in list:
        for title in season:
            if(title == fNm):   
                return season[0]
    return "etc"

def getQuarterIndex(q):
    index = 0
    for season in list:
        if(season[0] == q):
            return index
        index += 1
    return -1

def addQuarter(q):
    index = getQuarterIndex(0)
    list[index][0] = q
    
def addTitle(q, t):
    qIndex = getQuarterIndex(q)
    tIndex = 0
    for title in list[qIndex]:
        if(title == 0):
            list[qIndex][tIndex] = t;
            return
        tIndex += 1
        
def getQuarter():
    v_year = datetime.date.today().timetuple().tm_year
    v_month = datetime.date.today().timetuple().tm_mon
    v_quarter = str(v_year)
    if(v_month==12 or v_month==1 or v_month == 2):
        v_quarter += "-1"
    elif(v_month >= 3 and v_month <=5):
        v_quarter += "-2"
    elif(v_month >= 6 and v_month <=8):
        v_quarter += "-3"
    elif(v_month >= 9 and v_month <=11):
        v_quarter += "-4"

    index = getQuarterIndex(v_quarter)
    if(index == -1):
        addQuarter(v_quarter)
    
    return v_quarter
    
    
def mainRun():
    print("mainRun");
    
    pattern = re.compile(" - \d\d.*")
    episodePattern = re.compile("[\d]+")
    for f in files:
        fNm = f
        fNm = fNm.replace("[Leopard-Raws]", "")
	fNm = fNm.replace("[Ohys-Raws]", "")
        episodeNum = episodePattern.search(pattern.search(fNm).group(0)).group(0)
        
        fNm = fNm.replace(pattern.search(fNm).group(0), "")
        fNm = fNm.replace(".", "")
        fNm = fNm.strip()
        quarterNm = getQuarterNm(fNm)

        if(quarterNm == "etc" and (episodeNum=="00" or episodeNum=="01" or episodeNum=="02" or episodeNum=="03")):
            quarterNm = getQuarter()
            addTitle(quarterNm, fNm)
            
            writeF = open('./list.txt', 'wb')
            print("list update")
            #print(list)
            pickle.dump(list, writeF)
            writeF.close()
            
        print(quarterNm + ", " + fNm)
        if(makeDir(quarterNm)):
            os.mkdir(quarterNm)
        os.chdir(quarterNm)
        
        if( makeDir(fNm) ):
            os.mkdir(fNm)
        os.chdir("../")   
        shutil.move(f, "./"+quarterNm + "/" + fNm)

files = glob.glob("*.mp4")
mainRun()
