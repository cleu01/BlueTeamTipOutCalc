import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Combo, Output

sg.theme('Dark Amber')  # Let's set our own color theme

class Month:
    def __init__(self, mon, tues, wed, thurs, fri, sat, sun):
        self.m = mon
        self.t = tues
        self.w = wed
        self.th = thurs
        self.f = fri
        self.s = sat
        self.su = sun
class StaffRec:
    def __init__(self, serverRec, busserRec, runnerRec, barRec, hostRec, sales):
        self.serverRec = serverRec
        self.busserRec = busserRec
        self.runnerRec = runnerRec
        self.barRec= barRec
        self.hostRec = hostRec
        self.sales = sales
    def serverRecNum(self):
        self.serverRecNum = self.sales / self.serverRec
    def get_serverRecNum(self):
        return self.serverRecNum

dec = Month(5735.5, 7076.2, 8348, 9928, 10236, 12870.5, 10014.75)
jan = Month(4878, 5466, 6156, 7594, 13010, 15963, 9300)
feb = Month(3851, 5397.5, 6618.75, 7337.25, 15945.5, 25959, 11589.3)
mar = Month(11655.2, 12645.6, 14866.4, 1120.75, 22115, 37552, 25785.75)
apr = Month(19250, 21287.5, 12946, 16161.4, 38356.5, 37443.5, 32726)
may = Month(24834, 20117.75, 24369.25, 31328.25, 44232, 55200.4, 49653)
jun = Month(28522, 30172.6, 31349.2, 36913.25, 46486.75, 59819, 51945)
jul = Month(32221, 30227, 34833, 34614.6, 49747.6, 55546.8, 46121)
aug = Month(25423.8, 28361, 26758.5, 30797.25, 45502, 59934.5, 50337)
sept = Month(29570.25, 21639, 27085.4, 31867, 49392.25, 53766, 52189)
oct = Month(16101.25, 17642.5, 19582, 19165.5, 33507, 39613.2, 29497.2,)
nov = Month(9792.2, 13037.2, 14407, 10275.75, 29872, 30717.75, 21630.75,)

winterStaff = StaffRec(1700, 6000, 6000, 9000, 8000, dec.m)
staff = StaffRec(1500, 7000, 3000, 4000, 6000, dec.m)
# STEP 1 define the layout
layout = [ 
            [sg.Text('Select the Month:')],
            [sg.Combo(['January', 'February', 'March', 'April', 'May', 'June', 'July', 
            'August', 'September', 'October', 'November', 'December'], key='monthSelection')],
            [sg.Text('Select the Day:')],
            [sg.Combo(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], key='daySelection')],
            [sg.Button('Calculate'), sg.Button('Exit')],
            [sg.Text("Estimated Sales:"), sg.Text('                             ', key='-outputSales-')],
            [sg.Text("Recommended Staffing")],
            [sg.Text("Servers:"), sg.Text('                             ', key='-outputServers-')],
            [sg.Text("Bussers:"), sg.Text('                             ', key='-outputBussers-')],
            [sg.Text("Runners:"), sg.Text('                             ', key='-outputRunners-')],
            [sg.Text("Bartenders:"), sg.Text('                             ', key='-outputBars-')],
            [sg.Text("Hosts:"), sg.Text('                             ', key='-outputHosts-')],


         ]

#STEP 2 - create the window
window = sg.Window('My new window', layout)

# STEP3 - the event loop
while True:
    
    event, values = window.read()   # Read the event that happened and the values dictionary
    
    
    if event == sg.WIN_CLOSED or event == 'Exit':     # If user closed window with X or if user clicked "Exit" button then exit
        break
    if event == 'Calculate':
        myMonth = values['monthSelection']
        myDay = values['daySelection']
        if myMonth == "December":   
            thisMonth = dec
        if myMonth == "January":
            thisMonth = jan
        if myMonth == "February":
            thisMonth = feb
        if myMonth == "March":
            thisMonth = mar
        if myMonth == "April":
            thisMonth = apr
        if myMonth == "May":
            thisMonth = may
        if myMonth == "June":
            thisMonth = jun
        if myMonth == "July":
            thisMonth = jul
        if myMonth == "August":
            thisMonth = aug
        if myMonth == "September":
            thisMonth = sept
        if myMonth == "October":
            thisMonth = oct
        if myMonth == "November":
            thisMonth = nov

        if myDay == "Monday":
            myString='on a Monday in', myMonth, 'you should expect', thisMonth.m, 'in sales, you should staff', thisMonth.m / winterStaff.serverRec, 'servers', thisMonth.m / winterStaff.busserRec, 'bussers,', thisMonth.m / winterStaff.runnerRec, 'runners,', thisMonth.m / winterStaff.barRec, 'bartenders, and', thisMonth.m / winterStaff.hostRec, 'hosts!'
            sales = thisMonth.m
            serverNum = thisMonth.m / staff.serverRec
            busserNum = thisMonth.m / staff.busserRec
            runnerNum = thisMonth.m / staff.runnerRec
            barNum = thisMonth.m / staff.barRec
            hostNum = thisMonth.m / staff.hostRec
        if myDay == "Tuesday":
            myString=("on a Tuesday in", myMonth, "you should expect", thisMonth.t, "in sales, you should staff", thisMonth.t / winterStaff.serverRec, "servers,", thisMonth.t / winterStaff.busserRec, "bussers,", thisMonth.t / winterStaff.runnerRec, "runners,", thisMonth.t / winterStaff.barRec, "bartenders, and", thisMonth.t / winterStaff.hostRec, "hosts!")
            sales = thisMonth.t
            serverNum = thisMonth.t / staff.serverRec
            busserNum = thisMonth.t / staff.busserRec
            runnerNum = thisMonth.t / staff.runnerRec
            barNum = thisMonth.t / staff.barRec
            hostNum = thisMonth.t / staff.hostRec
        if myDay == "Wednesday":
            myString=("on a Wednesday in", myMonth, "you should expect", thisMonth.w, "in sales, you should staff", thisMonth.w / winterStaff.serverRec, "servers,", thisMonth.w / winterStaff.busserRec, "bussers,", thisMonth.w / winterStaff.runnerRec, "runners,", thisMonth.w / winterStaff.barRec, "bartenders, and", thisMonth.w / winterStaff.hostRec, "hosts!")
            sales = thisMonth.w
            serverNum = thisMonth.w / staff.serverRec
            busserNum = thisMonth.w / staff.busserRec
            runnerNum = thisMonth.w / staff.runnerRec
            barNum = thisMonth.w / staff.barRec
            hostNum = thisMonth.w / staff.hostRec
        if myDay == "Thursday":
            myString=("on a Thursday in", myMonth, "you should expect", thisMonth.th, "in sales, you should staff", thisMonth.th / winterStaff.serverRec, "servers,", thisMonth.th / winterStaff.busserRec, "bussers,", thisMonth.th / winterStaff.runnerRec, "runners,", thisMonth.th / winterStaff.barRec, "bartenders, and", thisMonth.th / winterStaff.hostRec, "hosts!")
            sales = thisMonth.th
            serverNum = thisMonth.th / staff.serverRec
            busserNum = thisMonth.th / staff.busserRec
            runnerNum = thisMonth.th / staff.runnerRec
            barNum = thisMonth.th / staff.barRec
            hostNum = thisMonth.th / staff.hostRec
        if myDay == "Friday":
            myString=("on a Friday in", myMonth, "you should expect", thisMonth.f, "in sales, you should staff", thisMonth.f / winterStaff.serverRec, "servers,", thisMonth.f / winterStaff.busserRec, "bussers,", thisMonth.f / winterStaff.runnerRec, "runners,", thisMonth.f / winterStaff.barRec, "bartenders, and", thisMonth.f / winterStaff.hostRec, "hosts!")
            sales = thisMonth.f
            serverNum = thisMonth.f / staff.serverRec
            busserNum = thisMonth.f / staff.busserRec
            runnerNum = thisMonth.f / staff.runnerRec
            barNum = thisMonth.f / staff.barRec
            hostNum = thisMonth.f / staff.hostRec
        if myDay == "Saturday":
            myString=("on a Saturday in", myMonth, "you should expect", thisMonth.s, "in sales, you should staff", thisMonth.s / winterStaff.serverRec, "servers,", thisMonth.s / winterStaff.busserRec, "bussers,", thisMonth.s / winterStaff.runnerRec, "runners,", thisMonth.s / winterStaff.barRec, "bartenders, and", thisMonth.s / winterStaff.hostRec, "hosts!")
            sales = thisMonth.s
            serverNum = thisMonth.s / staff.serverRec
            busserNum = thisMonth.s / staff.busserRec
            runnerNum = thisMonth.s / staff.runnerRec
            barNum = thisMonth.s / staff.barRec
            hostNum = thisMonth.s / staff.hostRec
        if myDay == "Sunday":
            myString=("on a Sunday in", myMonth, "you should expect", thisMonth.su, "in sales, you should staff", thisMonth.su / winterStaff.serverRec, "servers,", thisMonth.su / winterStaff.busserRec, "bussers,", thisMonth.su / winterStaff.runnerRec, "runners,", thisMonth.su / winterStaff.barRec, "bartenders, and", thisMonth.su / winterStaff.hostRec, "hosts!")
            sales = thisMonth.su
            serverNum = thisMonth.su / staff.serverRec
            busserNum = thisMonth.su / staff.busserRec
            runnerNum = thisMonth.su / staff.runnerRec
            barNum = thisMonth.su / staff.barRec
            hostNum = thisMonth.su / staff.hostRec
        window['-outputSales-'].update(sales)
        window['-outputServers-'].update(serverNum)
        window['-outputBussers-'].update(busserNum)
        window['-outputRunners-'].update(runnerNum)
        window['-outputBars-'].update(barNum)
        window['-outputHosts-'].update(hostNum)
        

        
        
window.close()
