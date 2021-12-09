# Blue team
# Tip out Calc

import csv
import numpy as np
infile = 'Shifts_Closed_2021_12_02.csv'


def dataIn(infile):
    dataArray = []
    with open(infile, newline='') as csv_file:
        dataArray = list(csv.reader(csv_file))
        
    return dataArray

def newList(dataIn):
    
    dataList = []
    for column in range (len(dataIn[0])): 
        for row in range(len(dataIn)):
            dataList.append(dataIn[row][column])
    return dataList


def tipShareTotal(dataList):
    total = 0
    index = dataList.index('Tip Share Total')
    index +=1
    for i in range(index, len(dataList)):
        total = total + float(dataList[i])
    return total 


def main():
    dataArray = dataIn(infile)
    dataList = newList(dataArray)
    totalTipShare = tipShareTotal(dataList)
    print(totalTipShare)    

main()