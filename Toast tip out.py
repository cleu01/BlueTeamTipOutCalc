# Blue team
# Tip out Calc

import csv

shiftsClosed = 'Shifts_Closed_2021_12_02.csv'
timeEntries = 'TimeEntries_2021_12_02.csv'

def timeEntriesIn(timeEntries):
    TimeArray = []
    with open(timeEntries, newline='') as csv_file:
        TimeArray = list(csv.reader(csv_file))
        
    return TimeArray

def TimeList(TimeArray):
    
    TimeList = []
    for column in range (len(TimeArray[0])): 
        for row in range(len(TimeArray)):
            TimeList.append(TimeArray[row][column])
    return TimeList

def dataIn(shiftsClosed):
    dataArray = []
    with open(shiftsClosed, newline='') as csv_file:
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

def employeeList(TimeList):
    employeeIndex = TimeList.index('Employee')
    jobIDIndex = TimeList.index('Job Id')
    listEmployees = []
    for i in range (employeeIndex +1, jobIDIndex):
        listEmployees.append(TimeList[i])
    return listEmployees

def jobTitleList(TimeList):
    jobTitleIndex = TimeList.index('Job Title')
    inDateIndex = TimeList.index('In Date')
    listJobTitles = []
    for i in range (jobTitleIndex +1, inDateIndex):
        listJobTitles.append(TimeList[i])
    return listJobTitles

def JobTitleSearch(listOfJobTitles, key):
    indexes = []
    for i in range (len(listOfJobTitles)):
        if key == listOfJobTitles[i]:
            indexes.append(i)
    return indexes

def hoursWorked(TimeList):
    TotalHoursIndex = TimeList.index('Total Hours')
    breakTimeIndex = TimeList.index('Unpaid Break Time')
    listHoursWorked = []
    for i in range (TotalHoursIndex +1, breakTimeIndex):
        listHoursWorked.append(TimeList[i])
    return listHoursWorked

def hoursSearch(listHoursWorked, key):
    HoursList = []
    for i in range (len(listHoursWorked)):
        for j in range(len(key)):
            if key[j] == i:
                HoursList.append(listHoursWorked[i])
    return HoursList

def employeeNamebyHours(listOfEmployees, key):
    Name = []
    for i in range (len(listOfEmployees)):
        for j in range(len(key)):
            if key[j] == i:
                Name.append(listOfEmployees[i])
    return Name

def tipSharePerJobTitle(totalTipShare):
    thirdOfTotal = totalTipShare/3
    return thirdOfTotal

def tipSharePerHour(TipShare, HoursWorked):
    IntMap = map(float, HoursWorked)
    totalHours = sum(IntMap)
    tipshareperhour = TipShare/totalHours
    tipshareperhour = round(tipshareperhour, 2)
    return tipshareperhour

def tipSharePayPerPerson(HoursWorked, PerHourPay):
    IntMap = map(float, HoursWorked)
    IntList = list(IntMap)
    totalPay = []
    for i in range (len(IntList)):
        total = IntList[i]*PerHourPay
        total = round(total, 2)
        totalPay.append(total)
    return totalPay

def printNameAndPay(NameList, PayList, JobTitle):
    for i in range(len(NameList)):
        print(NameList[i], "is a ", JobTitle, "and got paid ", PayList[i])
    

def main():
    Bartender = 'Bartender'
    Host = 'Host'
    Busser = 'Busser'
    Runner = 'Runner'
    dataArray = dataIn(shiftsClosed)
    dataList = newList(dataArray)
    timeArray = timeEntriesIn(timeEntries)
    timeList = TimeList(timeArray)
    totalTipShare = tipShareTotal(dataList) 
    TipSharePerJobTitle = tipSharePerJobTitle(totalTipShare)
    listOfEmployees = employeeList(timeList)
    listOfJobTitles = jobTitleList(timeList)
    bartenderIndexes = JobTitleSearch(listOfJobTitles, Bartender)
    hostIndexes = JobTitleSearch(listOfJobTitles, Host)
    busserIndexes = JobTitleSearch(listOfJobTitles, Busser)
    runnerIndexes = JobTitleSearch(listOfJobTitles, Runner)
    HoursWorkedList = hoursWorked(timeList)
    HoursWorkedByBartender = hoursSearch(HoursWorkedList, bartenderIndexes)
    HoursWorkedByBusser = hoursSearch(HoursWorkedList, busserIndexes)
    HoursWorkedByRunner = hoursSearch(HoursWorkedList, runnerIndexes)
    BartenderNameByHours = employeeNamebyHours(listOfEmployees, bartenderIndexes)
    BusserNameByHours = employeeNamebyHours(listOfEmployees, busserIndexes)
    RunnerNameByHours = employeeNamebyHours(listOfEmployees, runnerIndexes)
    BartenderTipSharePerHour = tipSharePerHour(TipSharePerJobTitle, HoursWorkedByBartender)
    RunnerTipSharePerHour = tipSharePerHour(TipSharePerJobTitle, HoursWorkedByRunner)
    BusserTipSharePerHour = tipSharePerHour(TipSharePerJobTitle, HoursWorkedByBusser)
    BartenderTotalPayList = tipSharePayPerPerson(HoursWorkedByBartender, BartenderTipSharePerHour)
    RunnerTotalPayList = tipSharePayPerPerson(HoursWorkedByRunner, RunnerTipSharePerHour)
    BusserTotalPayList = tipSharePayPerPerson(HoursWorkedByBusser, BusserTipSharePerHour)
    
    printNameAndPay(BartenderNameByHours, BartenderTotalPayList, Bartender)
    printNameAndPay(RunnerNameByHours, RunnerTotalPayList, Runner)
    printNameAndPay(BusserNameByHours, BusserTotalPayList, Busser)

main()