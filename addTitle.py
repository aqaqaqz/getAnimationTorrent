import os
import glob
import shutil
import re
import pickle
import datetime

readF = open('./list.txt', 'rb')

list = [[0 for col in range(60)] for row in range(10)]
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

def addTitle(q, t):
    #해당분기 마지막에 타이틀 추가
    qIndex = getQuarterIndex(q)
    tIndex = 0
    for title in list[qIndex]:
        if(title == 0):
            list[qIndex][tIndex] = t;
            return
        tIndex += 1
        
def mainRun():
    print("mainRun");
    
    #quarterNm = '2018-2'
    #addTitle(quarterNm, 'Amanchu!')
    
    writeF = open('./list.txt', 'wb')
    print("리스트 갱신")
    print(list)
    pickle.dump(list, writeF)
    writeF.close()
            

mainRun()
