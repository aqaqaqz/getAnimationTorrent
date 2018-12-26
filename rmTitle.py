import os
import glob
import shutil
import re
import pickle
import datetime

readF = open('./list.txt', 'rb')

list = [[0 for col in range(100)] for row in range(50)]
list = pickle.load(readF)
print(list)
readF.close()

def getQuarterIndex(q):
    index = 0
    for season in list:
        if(season[0] == q):
            return index
        index += 1
    return -1

def rmTitle(q, t):
    #해당분기 타이틀 삭제
    qIndex = getQuarterIndex(q)
    tIndex = 0
    for title in list[qIndex]:
        if(title == t):
            list[qIndex][tIndex] = None;
            return
        tIndex += 1
        
def mainRun():
    print("mainRun");
    
    quarterNm = '2018-1'
    rmTitle(quarterNm, 'Strike the Blood III')
    
    writeF = open('./list.txt', 'wb')
    print("리스트 갱신")
    print(list)
    pickle.dump(list, writeF)
    writeF.close()
            

mainRun()
