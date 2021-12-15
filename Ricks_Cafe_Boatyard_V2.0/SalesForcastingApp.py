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
    def __init__(self, serverRec = 1000, busserRec = 10000, runnerRec=10000, barRec=9000, hostRec=9000):
        self.serverRec = serverRec
        self.busserRec = busserRec
        self.runnerRec = runnerRec
        self.barRec= barRec
        self.hostRec = hostRec
        
    
    
    def get_serverRec(self):
        return self.serverRec
    def set_serverRec(self, x):
        self.set_serverRec = x
    def get_busserRec(self):
        return self.busserRec
    def set_busserRec(self, x):
        self.set_busserRec
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

winterStaff = StaffRec(1700, 6000, 6000, 9000, 8000)
staff = StaffRec()
# STEP 1 define the layout
layout = [ 
            [sg.Text('Select the Month:'),sg.Combo(['January', 'February', 'March', 'April', 'May', 'June', 'July', 
            'August', 'September', 'October', 'November', 'December'], default_value='January', key='monthSelection')],        
            [sg.Text('Select the Day:'),sg.Combo(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],default_value='Monday', key='daySelection')],
            [sg.Text('Optionally, you may change staffing recommendation rates. Enter how much sales per one of each staff member.')],
            [sg.Text('Servers:'),sg.Input(staff.serverRec,key='serverIn',size=(6,1)), sg.Text('Bussers:'),sg.Input(staff.busserRec,key='busserIn',size=(6,1)), sg.Text('Runners:'),sg.Input(staff.runnerRec,key='runnerIn',size=(6,1))],
            [sg.Text('Bartenders:'),sg.Input(staff.barRec,key='barIn',size=(6,1)), sg.Text('Hosts:'),sg.Input(staff.hostRec,key='hostIn',size=(6,1))],
            [sg.Button('Calculate'), sg.Button('Exit')],
            [sg.Text("Estimated Sales:"), sg.Text('    ', key='-outputSales-')],
            [sg.Text("Recommended Staffing")],
            [sg.Text("Servers:"), sg.Text('                   ', key='-outputServers-'), sg.Text("Bussers:"), sg.Text('                    ', key='-outputBussers-')],
            
            [sg.Text("Runners:"), sg.Text('                    ', key='-outputRunners-'),sg.Text("Bartenders:"), sg.Text('                     ', key='-outputBars-')],
            
            [sg.Text("Hosts:"), sg.Text('                      ', key='-outputHosts-')],


         ]

#STEP 2 - create the window
window = sg.Window('Sales Forecasting', layout)

# STEP3 - the event loop
while True:
    
    event, values = window.read()   # Read the event that happened and the values dictionary
    
    
    if event == sg.WIN_CLOSED or event == 'Exit':     # If user closed window with X or if user clicked "Exit" button then exit
        break
    if event == 'Update Staff Levels':
        staff = StaffRec()
        staff.set_serverRec(values['serverIn'])
    if event == 'Calculate':
        #staff.serverRec = values['serverIn']
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
            sales = thisMonth.m
            serverNum = round(thisMonth.m / int(values['serverIn']))
            busserNum = round(thisMonth.m / int(values['busserIn']))
            runnerNum = round(thisMonth.m / int(values['runnerIn']))
            barNum = round(thisMonth.m / int(values['barIn']))
            hostNum = round(thisMonth.m / int(values['hostIn']))

        if myDay == "Tuesday":           
            sales = thisMonth.t
            serverNum = round(thisMonth.t / int(values['serverIn']))
            busserNum = round(thisMonth.t / int(values['busserIn']))
            runnerNum = round(thisMonth.t / int(values['runnerIn']))
            barNum = round(thisMonth.t / int(values['barIn']))
            hostNum = round(thisMonth.t / int(values['hostIn']))

        if myDay == "Wednesday":           
            sales = thisMonth.w
            serverNum = round(thisMonth.w / int(values['serverIn']))
            busserNum = round(thisMonth.w / int(values['busserIn']))
            runnerNum = round(thisMonth.w / int(values['runnerIn']))
            barNum = round(thisMonth.w / int(values['barIn']))
            hostNum = round(thisMonth.w / int(values['hostIn']))

        if myDay == "Thursday":          
            sales = thisMonth.th
            serverNum = round(thisMonth.th / int(values['serverIn']))
            busserNum = round(thisMonth.th / int(values['busserIn']))
            runnerNum = round(thisMonth.th / int(values['runnerIn']))
            barNum = round(thisMonth.th / int(values['barIn']))
            hostNum = round(thisMonth.th / int(values['hostIn']))

        if myDay == "Friday":            
            sales = thisMonth.f
            serverNum = round(thisMonth.f / int(values['serverIn']))
            busserNum = round(thisMonth.f / int(values['busserIn']))
            runnerNum = round(thisMonth.f / int(values['runnerIn']))
            barNum = round(thisMonth.f / int(values['barIn']))
            hostNum = round(thisMonth.f / int(values['hostIn']))

        if myDay == "Saturday": 
            sales = thisMonth.s
            serverNum = round(thisMonth.s / int(values['serverIn']))
            busserNum = round(thisMonth.s / int(values['busserIn']))
            runnerNum = round(thisMonth.s / int(values['runnerIn']))
            barNum = round(thisMonth.s / int(values['barIn']))
            hostNum = round(thisMonth.s / int(values['hostIn']))

        if myDay == "Sunday":
            sales = thisMonth.su
            serverNum = round(thisMonth.su / int(values['serverIn']))
            busserNum = round(thisMonth.su / int(values['busserIn']))
            runnerNum = round(thisMonth.su / int(values['runnerIn']))
            barNum = round(thisMonth.su / int(values['barIn']))
            hostNum = round(thisMonth.su / staff.hostRec)

        window['-outputSales-'].update("${:,.2f}".format(sales))
        window['-outputServers-'].update(serverNum)
        window['-outputBussers-'].update(busserNum)
        window['-outputRunners-'].update(runnerNum)
        window['-outputBars-'].update(barNum)
        window['-outputHosts-'].update(hostNum)
        

        
        
window.close()
