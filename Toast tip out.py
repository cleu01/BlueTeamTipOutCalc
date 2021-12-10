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

def employeeList(dataList):
    employeeIndex = dataList.index('Employee')
    jobTitleIndex = dataList.index('Job Title')
    listEmployees = []
    for i in range (employeeIndex +1, jobTitleIndex):
        listEmployees.append(dataList[i])
    return listEmployees

def jobTitleList(dataList):
    jobTitleIndex = dataList.index('Job Title')
    inDateIndex = dataList.index('In Date')
    listJobTitles = []
    for i in range (jobTitleIndex +1, inDateIndex):
        listJobTitles.append(dataList[i])
    return listJobTitles

def JobTitleSearch(listOfJobTitles, key):
    indexes = []
    for i in range (len(listOfJobTitles)):
        if key == listOfJobTitles[i]:
            indexes.append(i)
    return indexes

def main():
    Bartender = 'Bartender'
    dataArray = dataIn(infile)
    dataList = newList(dataArray)
    totalTipShare = tipShareTotal(dataList) 
    listOfEmployees = employeeList(dataList)
    listOfJobTitles = jobTitleList(dataList)
    bartenderIndexes = JobTitleSearch(listOfJobTitles, Bartender)
    

main()