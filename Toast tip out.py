# Blue team
# Tip out Calc

import PySimpleGUI as sg
import csv



#imports time entry csv
def timeEntriesIn(timeEntries):
    TimeArray = []
    with open(timeEntries, newline='') as csv_file:
        TimeArray = list(csv.reader(csv_file))
        
    return TimeArray

#puts time list csv in an array, may be unneccessary but was a part of the process in my head
def TimeList(TimeArray):
    
    TimeList = []
    for column in range (len(TimeArray[0])): 
        for row in range(len(TimeArray)):
            TimeList.append(TimeArray[row][column])
    return TimeList

#imports shifts closed csv
def dataIn(shiftsClosed):
    dataArray = []
    with open(shiftsClosed, newline='') as csv_file:
        dataArray = list(csv.reader(csv_file))
        
    return dataArray

#puts shifts closed csv in a list
def newList(dataIn):
    
    dataList = []
    for column in range (len(dataIn[0])): 
        for row in range(len(dataIn)):
            dataList.append(dataIn[row][column])
    return dataList

#calculates Tip Share Total from shifts closed csv
def tipShareTotal(dataList):
    total = 0
    index = dataList.index('Tip Share Total')
    index +=1
    for i in range(index, len(dataList)):
        total = total + float(dataList[i])
    return total 

#Generates a list of employee's from time entries csv
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

#Temp Function to show possible outputs
def printNameAndPay(NameList, PayList, JobTitle):
    output = []
    for i in range(len(NameList)):
        output.append(NameList[i] + "is a " + JobTitle + " and got paid "+ str(PayList[i]))
    return output


def main():
    layout = [ 
            [sg.Text(size = (50,10), key='__OUTPUT0__')],
            [sg.Text(size = (50,10), key='__OUTPUT1__')],
            [sg.Text(size = (50,10), key='__OUTPUT2__')],
            [sg.Text('Shifts Closed CSV')],
            [sg.Input(), sg.FileBrowse()], 
            [sg.Text('Time Entries CSV')],
            [sg.Input(), sg.FileBrowse()],
            [sg.ReadButton('OPEN'), sg.Button('Exit')]
         ]
 

#create the window
    window = sg.Window('Tipout Calc', layout, size= (900, 800))

    while True:

        event, values = window.read() 
        value0 = event, ''.join(values[0])
        value1 = event, ''.join(values[1])  # Read the event that happened and the values dictionary
        
        if event == sg.WIN_CLOSED or event == 'Exit':     # If user closed window with X or if user clicked "Exit" button then exit
            break
        if event == 'OPEN':
            #I need to make these inputs from a UI
            shiftsClosed = value0[1]
            timeEntries = value1[1]

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
            
            display0 = printNameAndPay(BartenderNameByHours, BartenderTotalPayList, Bartender)
            display1 = printNameAndPay(RunnerNameByHours, RunnerTotalPayList, Runner)
            display2 = printNameAndPay(BusserNameByHours, BusserTotalPayList, Busser)

            window['__OUTPUT0__'].update(display0)
            window['__OUTPUT1__'].update(display1)
            window['__OUTPUT2__'].update(display2)
            
    window.close()

main()    