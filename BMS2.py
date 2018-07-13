import os, inspect, json, signal
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import *
from tkinter.font import *
import time, subprocess
import psutil, gc
from time import strftime, localtime

#Run SNMP
SNMPProcess = subprocess.Popen("sudo python3.6 .A.py", shell=True)
#os.system("sudo python3.6 .A.py")

def BeginModbusTask():
    global ModbusProcess
    ModbusProcess=subprocess.Popen('./M',shell=True, preexec_fn=os.setpgrp)
    #ModbusProcess=subprocess.Popen('python3.6 M2.py',shell=True, preexec_fn=os.setpgrp)

def get_process_memory():
    global ModbusProcess
    GUI = psutil.Process(os.getpid())
    SNMP = psutil.Process(SNMPProcess.pid)
    try:
        MPoll = psutil.Process(ModbusProcess.pid)
        return [GUI.memory_info().rss, SNMP.memory_info().rss, MPoll.memory_info().rss]
    except:
        return [GUI.memory_info().rss, SNMP.memory_info().rss]
        

FolderPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

def getSerial():
    #Extract serial from cpuinfo file
    cpuserial = "0000000000000000"
    try:
        f = open('/proc/cpuinfo', 'r')
        for line in f:
            if line[0:6] == 'Serial':
                cpuserial = line[10:26]
        f.close()
    except:
        cpuserial = "ERROR00000000000"

    return cpuserial

PiSN = getSerial()
print(PiSN)

#with open(FolderPath + '/serial.txt') as file:
#    _PiSN = str(file.read())
#print(_PiSN)


if PiSN != "0000000046cf5e37":
    #os.system('sudo rm /var/www/html/M')
    #os.system('sudo rm /var/www/html/.A.py')
    print('CPU Serial number is different')
else:
    print('CPU Serial number is correct')
    
print('CPU Serial number is already checked')


root = Tk()
root.title('PanasonicDCB105ZK - GSPE BMS')
#root.geometry('1500x1080')
root.geometry('800x480')
#root.attributes("-fullscreen", True)
root.configure()

f1 = Font(family='helvetica bold', size=-16)
f2 = Font(family='helvetica', size=-12)
f3 = Font(family='helvetica', size=-10)
s = ttk.Style()
s.configure('.', font=f1)
s.configure('My.TFrame', background='#ECECEC')
#print(s.theme_names())
#print(s.theme_use())
s.theme_settings( "default", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0], 'background':'black'} },
        "TNotebook.Tab": {
            "configure": {"padding": [70, 20], 'background':'#013474', 'foreground':'white'},
            "map": {'foreground':[("selected", 'black')], "background":[("selected", 'white')],
                    "expand": [("selected", [1,1,1,0])]}}})

root.option_add("*TCombobox*Listbox*Font", f2)


nb = ttk.Notebook(root)
nb.pack(fill='both', expand=1)

page1 = ttk.Frame(nb, style='My.TFrame')
nb.add(page1, text='Home')
page2 = ttk.Frame(nb, style='My.TFrame')
nb.add(page2, text='Overview')
page3 = ttk.Frame(nb, style='My.TFrame')
nb.add(page3, text='Module')

#------------------------------- page 1 -----------------------------------#
fr1 = ttk.Frame(page1, style='My.TFrame')
fr1.grid(row=0,column=0, sticky=N)
fr2 = ttk.Frame(page1, style='My.TFrame')
fr2.grid(row=0,column=1, padx = 10, sticky=N)
fr3 = ttk.Frame(page1, style='My.TFrame')
fr3.grid(row=0,column=2, padx = 10, sticky=N)

#---- Variable Name ----#
labelip = Label(fr1,text = "IP Address", font=f2, bg ='#ECECEC')
labelnetmask = Label(fr1,text = "Netmask", font=f2, bg ='#ECECEC')
labelgateway = Label(fr1,text = "Gateway", font=f2, bg ='#ECECEC')
labelsnmpver = Label(fr1,text = "SNMP Version", font=f2, bg ='#ECECEC')
labelsnmpcom = Label(fr1,text = "SNMP Community", font=f2, bg ='#ECECEC')
labelsnmpport = Label(fr1,text = "SNMP Port", font=f2, bg ='#ECECEC')
labelsysoid = Label(fr1,text = "Sys OID", font=f2, bg ='#ECECEC')

#---- Entry ----#
eip = Entry(fr1, font=f2)
enetmask = Entry(fr1, font=f2)
egateway = Entry(fr1, font=f2)
snmp_ver = tk.StringVar()
esnmpver = ttk.Combobox (fr1, textvariable = snmp_ver, height=5, width = 19, font=f2)
esnmpver ["values"] = ("1", "2")
esnmpver.current(0)

snmp_com = tk.StringVar()
esnmpcom = ttk.Combobox (fr1, textvariable = snmp_com, height=5, width = 19, font=f2)
esnmpcom ["values"] = ("public", "private")
esnmpcom.current(0)

#esnmpcom = Entry(fr1, font=f1)
esnmpport= Entry(fr1, font=f2)
esysoid  = Entry(fr1, font=f2)

#---- Grid ----#
labelip.grid (row=0,column=0,padx=3,pady=3)
labelnetmask.grid (row=1,column=0,padx=3,pady=3)
labelgateway.grid (row=2,column=0,padx=3,pady=3)
labelsnmpver.grid (row=3,column=0,padx=3,pady=3)
labelsnmpcom.grid (row=4,column=0,padx=3,pady=3)
labelsnmpport.grid (row=5,column=0,padx=3,pady=3)
labelsysoid.grid (row=6,column=0,padx=3,pady=3)

eip.grid(row=0,column=1,padx=15,pady=5,sticky=W)
enetmask.grid(row=1,column=1,padx=15,pady=5,sticky=W)
egateway.grid(row=2,column=1,padx=15,pady=5,sticky=W)
esnmpver.grid (row=3,column=1)
esnmpcom.grid(row=4,column=1,padx=15,pady=5,sticky=W)
esnmpport.grid(row=5,column=1,padx=15,pady=5,sticky=W)
esysoid.grid(row=6,column=1,padx=15,pady=5,sticky=W)

#---- Apply Button ----#
def apply():
    if askyesno('Verify', 'Device will be rebooted. Do you really want to change the settings?'):
        data = {
                'ipAddress': eip.get(),
                'netMask': enetmask.get(),
                'gateway': egateway.get(),
                'snmpVersion': int(esnmpver.get()),
                'snmpCommunity': esnmpcom.get(),
                'snmpPort': int(esnmpport.get()),
                'sysOID': esysoid.get()
                }
        print(data)
        
        with open(FolderPath + '/json/Comm.json', 'w') as file:
            file.write(json.dumps(data))

        os.system('cd /')
        os.system('cd var/www/html')
        os.system('./reboot')
        #os.system('sudo python3.6 reboot.py')
    
        
while (True):
    try:
        with open(FolderPath + '/json/Comm.json') as json_data:
            Comm = json.load(json_data)
        break
    except Exception as e:
        print(e)
        time.sleep(1)
        
eip.insert(0,Comm['ipAddress'])
enetmask.insert(0,Comm['netMask'])
egateway.insert(0,Comm['gateway'])
    
snmpVerIndex = int(Comm['snmpVersion'])-1
esnmpver.current(snmpVerIndex)

if Comm['snmpCommunity'] == 'public' or Comm['snmpCommunity'] == 'Public':
    esnmpcom.current(0)
elif Comm['snmpCommunity'] == 'private' or Comm['snmpCommunity'] == 'Private':
    esnmpcom.current(1)
else:
    esnmpcom ["values"] = ("public", "private", Comm['snmpCommunity'])
    esnmpcom.current(2)
    
#esnmpcom.insert(0,Comm['snmpCommunity'])

esnmpport.insert(0,Comm['snmpPort'])
esysoid.insert(0,Comm['sysOID'])

def Reset():
    if askyesno('Verify', 'Device will be rebooted. Do you really want to reset the settings?'):
        data = {
                'ipAddress': '192.168.2.100',
                'netMask': '255.255.255.0',
                'gateway': '192.168.2.1',
                'snmpVersion': 2,
                'snmpCommunity': 'public',
                'snmpPort': 161,
                'sysOID': '.1.3.6.1.4.1.10000.10.1',
                }
        print(data)
        
        with open(FolderPath + '/json/Comm.json', 'w') as file:
            file.write(json.dumps(data))

        os.system('cd /')
        os.system('cd var/www/html')
        os.system('./reboot')
        
        #os.system('sudo python3.6 reboot.py')
    
    
ButtonApply = tk.Button(fr1, text = "Apply" , font=f2, bg='white', width =1, command=apply)
ButtonApply.grid(row=7, column=1, sticky=NSEW)


def key0():
    widget = root.focus_get()
    if widget and hasattr(widget,"insert"):
        widget.insert(END, str(0))
def key1():
    widget = root.focus_get()
    if widget and hasattr(widget,"insert"):
        widget.insert(END, str(1))
def key2():
    widget = root.focus_get()
    if widget and hasattr(widget,"insert"):
        widget.insert(END, str(2))
def key3():
    widget = root.focus_get()
    if widget and hasattr(widget,"insert"):
        widget.insert(END, str(3))
def key4():
    widget = root.focus_get()
    if widget and hasattr(widget,"insert"):
        widget.insert(END, str(4))
def key5():
    widget = root.focus_get()
    if widget and hasattr(widget,"insert"):
        widget.insert(END, str(5))
def key6():
    widget = root.focus_get()
    if widget and hasattr(widget,"insert"):
        widget.insert(END, str(6))
def key7():
    widget = root.focus_get()
    if widget and hasattr(widget,"insert"):
        widget.insert(END, str(7))
def key8():
    widget = root.focus_get()
    if widget and hasattr(widget,"insert"):
        widget.insert(END, str(8))
def key9():
    widget = root.focus_get()
    if widget and hasattr(widget,"insert"):
        widget.insert(END, str(9))
def keyDot():
    widget = root.focus_get()
    if widget and hasattr(widget,"insert"):
        widget.insert(END, ".")
def keyBackSpace():
    widget = root.focus_get()
    if widget and hasattr(widget,"delete"):
        text = widget.get()
        widget.delete(0,END)
        widget.insert(END, text[:-1])

def keyUndo():
    
    while (True):
        try:
            with open(FolderPath + '/json/Comm.json') as json_data:
                Comm = json.load(json_data)
            break
        except Exception as e:
            print(e)
            time.sleep(1)
    eip.delete(0,END)     
    eip.insert(0,Comm['ipAddress'])
    enetmask.delete(0,END)     
    enetmask.insert(0,Comm['netMask'])
    egateway.delete(0,END)     
    egateway.insert(0,Comm['gateway'])
        
    snmpVerIndex = int(Comm['snmpVersion'])-1
    esnmpver.current(snmpVerIndex)


    if Comm['snmpCommunity'] == 'public' or Comm['snmpCommunity'] == 'Public':
        esnmpcom.current(0)
    elif Comm['snmpCommunity'] == 'private' or Comm['snmpCommunity'] == 'Private':
        esnmpcom.current(1)
    else:
        esnmpcom ["values"] = ("public", "private", Comm['snmpCommunity'])
        esnmpcom.current(2)
        
    #esnmpcom.insert(0,Comm['snmpCommunity'])
    esnmpport.delete(0,END)     
    esnmpport.insert(0,Comm['snmpPort'])
    esysoid.delete(0,END)     
    esysoid.insert(0,Comm['sysOID'])
        
def keyClear():
    widget = root.focus_get()
    if widget and hasattr(widget,"delete"):
        widget.delete(0,END)
        

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Keypad ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
Butt1 = tk.Button(fr2, text = "1" , font=f1, bg='white', height=2, width = 2, command=key1)
Butt1.grid(row=0,column=0, sticky=W)
Butt2= tk.Button(fr2, text = "2" , font=f1, bg='white', height=2, width = 2, command=key2)
Butt2.grid(row=0,column=1, sticky=W)
Butt3= tk.Button(fr2, text = "3" , font=f1, bg='white', height=2, width = 2, command=key3)
Butt3.grid(row=0,column=2, sticky=W)

Butt4 = tk.Button(fr2, text = "4" , font=f1, bg='white', height=2, width = 2, command=key4)
Butt4.grid(row=1,column=0, sticky=W)
Butt5= tk.Button(fr2, text = "5" , font=f1, bg='white', height=2, width = 2, command=key5)
Butt5.grid(row=1,column=1, sticky=W)
Butt6= tk.Button(fr2, text = "6" , font=f1, bg='white', height=2, width = 2, command=key6)
Butt6.grid(row=1,column=2, sticky=W)

Butt7 = tk.Button(fr2, text = "7" , font=f1, bg='white', height=2, width = 2, command=key7)
Butt7.grid(row=2,column=0, sticky=W)
Butt8= tk.Button(fr2, text = "8" , font=f1, bg='white', height=2, width = 2, command=key8)
Butt8.grid(row=2,column=1, sticky=W)
Butt9= tk.Button(fr2, text = "9" , font=f1, bg='white', height=2, width = 2, command=key9)
Butt9.grid(row=2,column=2, sticky=W)

ButtDot = tk.Button(fr2, text = "." , font=f1, bg='white', height=2, width = 2, command=keyDot)
ButtDot.grid(row=3,column=0, sticky=W)
Butt0= tk.Button(fr2, text = "0" , font=f1, bg='white', height=2, width = 2, command=key0)
Butt0.grid(row=3,column=1, sticky=W)
ButtBackSpace= tk.Button(fr2, text = "x" , font="Times 14 bold", bg='white', height=2, width = 2, command=keyBackSpace)
ButtBackSpace.grid(row=3,column=2, sticky=W)

ButtUndo= tk.Button(fr2, text = "Undo" , font=f1, bg='white', height=2, width = 2, command=keyUndo)
ButtUndo.grid(row=4,column=0, sticky=W)
ButtReset= tk.Button(fr2, text = "Reset" , font=f1, bg='white', height=2, width = 2, command=Reset)
ButtReset.grid(row=4,column=1, sticky=W)
ButtDel= tk.Button(fr2, text = "Clear" , font=f1, bg='white', height=2, width = 2, command=keyClear)
ButtDel.grid(row=4,column=2, sticky=W)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Modbus & SNMP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
Modbus = False
SNMP = False
def keyPoll():
    global Modbus
    Modbus = not Modbus
    print("Modbus >>", Modbus)
    if Modbus:
        BeginModbusTask()
        eModbus.delete(0,END)
        eModbus.insert(END,'Running.')
        ButtModbus.configure(bg="yellow")
        root.after(1000,refresh)
    else:
        global ModbusProcess
        os.kill(-ModbusProcess.pid, signal.SIGTERM)
        eModbus.delete(0,END)
        eModbus.insert(0,'Not Running.')
        ButtModbus.configure(bg="white")
        ClearAll()
    

ButtModbus= tk.Button(fr3, text = "Modbus" , font=f1, bg='white', height=2, width = 8, command=keyPoll)
ButtModbus.grid(row=0,column=0, sticky=W, padx =3)
eModbus = Entry(fr3, font=f1)
eModbus.grid(row=0,column=1, sticky=W)


#------------------------------- page 2 -----------------------------------#
fr1 = ttk.Frame(page2, style='My.TFrame')
fr1.grid(row=0,column=0, sticky=W)
fr2 = ttk.Frame(page2, style='My.TFrame')
fr2.grid(row=1,column=0, sticky=W)
fr3 = ttk.Frame(page2, style='My.TFrame')
fr3.grid(row=2,column=0, sticky=NE)

#---- Variable Name ----#
labelCV = Label(fr1,text = "CV", font=f3)
labelCCL = Label(fr1,text = "CCL", font=f3)
labelDCL = Label(fr1,text = "DCL", font=f3)
labelEDV = Label(fr1,text = "EDV", font=f3)
labelBV = Label(fr1,text = "BusVolt", font=f3)
labelBC = Label(fr1,text = "BusCurr", font=f3)
labelCap = Label(fr1,text = "Capacity", font=f3)
labelBT = Label(fr1,text = "Backup Time", font=f3)
labelDM = Label(fr1,text = "Detected_Mod", font=f3)
labelStat = Label(fr2,text = "Status", font=f3)
labelWarn = Label(fr2,text = "Warning", font=f3)
labelAlr = Label(fr2,text = "Alarm", font=f3)
labelErr = Label(fr2,text = "Error", font=f3)
labelOvTime = Label(fr3,text = "Latest Update:", font=f3, bg ='#ECECEC')

#---- Entry ----#
eCV = Entry(fr1, font=f3)
eCCL = Entry(fr1, font=f3)
eDCL = Entry(fr1, font=f3)
eEDV = Entry(fr1, font=f3)
eBV = Entry(fr1, font=f3)
eBC = Entry(fr1, font=f3)
eCap   = Entry(fr1, font=f3)
eBT = Entry(fr1, font=f3)
eDM    = Entry(fr1, font=f3)
eStat = Text(fr2, font=f3, height= 4, width = 50, undo=False)
eWarn = Text(fr2, font=f3, height= 4, width = 50, undo=False)
eAlr = Text(fr2, font=f3, height= 4, width = 50, undo=False)
eErr = Text(fr2, font=f3, height= 4, width = 50, undo=False)
eOvTime = Entry(fr3, font=f3, width = 20)
#---- Unit ----#
unitCV = Label(fr1,text = "Volt", font=f2)
unitCCL = Label(fr1,text = "Ampere", font=f2)
unitDCL = Label(fr1,text = "Ampere", font=f2)
unitEDV = Label(fr1,text = "Volt", font=f2)
unitBV = Label(fr1,text = "Volt", font=f2)
unitBC = Label(fr1,text = "Ampere", font=f2)
unitCap = Label(fr1,text = "Ah", font=f2)
unitDM = Label(fr1,text = "Module", font=f2)


#---- Grid ----#
labelCV.grid (row=0,column=0,padx=3,pady=3, sticky=W)
labelCCL.grid (row=1,column=0,padx=3,pady=3, sticky=W)
labelDCL.grid (row=2,column=0,padx=3,pady=3, sticky=W)
labelEDV.grid (row=3,column=0,padx=3,pady=3, sticky=W)
labelBV.grid (row=0,column=3,padx=3,pady=3, sticky=W)
labelBC.grid (row=1,column=3,padx=3,pady=3, sticky=W)
labelCap.grid (row=2,column=3,padx=3,pady=3, sticky=W)
labelBT.grid (row=3,column=3,padx=3,pady=3, sticky=W)
labelDM.grid (row=4,column=3,padx=3,pady=3, sticky=W)
labelStat.grid (row=9,column=0,padx=3,pady=3, sticky=W)
labelWarn.grid (row=10,column=0,padx=3,pady=3, sticky=W)
labelAlr.grid (row=11,column=0,padx=3,pady=3, sticky=W)
labelErr.grid (row=12,column=0,padx=3,pady=3, sticky=W)
labelOvTime.grid (row=0,column=0, sticky=NE)

eCV.grid(row=0,column=1, sticky=W)
eCCL.grid(row=1,column=1, sticky=W)
eDCL.grid(row=2,column=1, sticky=W)
eEDV.grid(row=3,column=1, sticky=W)
eBV.grid(row=0,column=4, sticky=W)
eBC.grid(row=1,column=4, sticky=W)
eCap.grid(row=2,column=4, sticky=W)
eBT.grid(row=3,column=4, sticky=W)
eDM.grid(row=4,column=4, sticky=W)
eStat.grid(row=9,column=1, sticky=W)
eWarn.grid(row=10,column=1, sticky=W)
eAlr.grid(row=11,column=1, sticky=W)
eErr.grid(row=12,column=1, sticky=W)
eOvTime.grid (row=0,column=1, sticky=NE)

unitCV.grid (row=0,column=2,padx=3,pady=3, sticky=W)
unitCCL.grid (row=1,column=2,padx=3,pady=3, sticky=W)
unitDCL.grid (row=2,column=2,padx=3,pady=3, sticky=W)
unitEDV.grid (row=3,column=2,padx=3,pady=3, sticky=W)
unitBV.grid (row=0,column=5,padx=3,pady=3, sticky=W)
unitBC.grid (row=1,column=5,padx=3,pady=3, sticky=W)
unitCap.grid (row=2,column=5,padx=3,pady=3, sticky=W)
unitDM.grid (row=4,column=5,padx=3,pady=3, sticky=W)

#------------------------------- page 3 -----------------------------------#
fr1 = ttk.Frame(page3, style='My.TFrame')
fr1.grid(row=0,column=0, sticky=W)
fr2 = ttk.Frame(page3, style='My.TFrame')
fr2.grid(row=1,column=0, sticky=W)
fr3 = ttk.Frame(page3, style='My.TFrame')
fr3.grid(row=2,column=0, sticky=W)
fr4 = ttk.Frame(page3, style='My.TFrame')
fr4.grid(row=3,column=0, sticky=NE)

labelmodul = Label(fr1,text = "Select Battery Module:", font= f1, bg ='#ECECEC').grid(row=0,column=0, sticky=W)

mod_value = tk.IntVar()
modul = ttk.Combobox(fr1, textvariable= mod_value, font = f1)
modul.grid(row=0,column=1, sticky=W, padx=5, pady =5)
modul ["values"] = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
modul.current(0)

def prevMod():
    q = mod_value.get()-1
    if q < 1:
        q = 1
    #print(q)
    modul.current(q-1)
    

def nextMod():
    q = mod_value.get()+1
    if q > 16:
        q = 16
    #print(q)
    modul.current(q-1)
    
prevButt = tk.Button(fr1, text = "prev" , font=f1, bg='white', height=1, width = 3, command=prevMod)
prevButt.grid(row=0,column=2, sticky=W)
nextButt = tk.Button(fr1, text = "next" , font=f1, bg='white', height=1, width = 3, command=nextMod)
nextButt.grid(row=0,column=3, sticky=W)

#----------------- General -----------------#
LabFr_General = ttk.Labelframe(fr2, text='General', width=700, height=300, style='My.TFrame', borderwidth=2)
LabFr_General.grid(row=0,column=0, padx=0, pady =0, ipadx=3, ipady =3, sticky='ne')

#---- Variable Name ----#
labelVoltage = Label(LabFr_General,text = "Voltage", font=f3, bg ='#ECECEC')
labelCurrent = Label(LabFr_General,text = "Current", font=f3, bg ='#ECECEC')
labelDC = Label(LabFr_General,text = "DC", font=f3, bg ='#ECECEC')
labelFCC = Label(LabFr_General,text = "FCC", font=f3, bg ='#ECECEC')
labelRC = Label(LabFr_General,text = "RC", font=f3, bg ='#ECECEC')
labelSOC = Label(LabFr_General,text = "SOC", font=f3, bg ='#ECECEC')
labelSOH = Label(LabFr_General,text = "SOH", font=f3, bg ='#ECECEC')
labelCycleCount = Label(LabFr_General,text = "Cycle Count", font=f3, bg ='#ECECEC')

#---- Entry ----#
eVoltage = Entry(LabFr_General, font=f3, width=6)
eCurrent = Entry(LabFr_General, font=f3, width=6)
eDC = Entry(LabFr_General, font=f3, width=6)
eFCC = Entry(LabFr_General, font=f3, width=6)
eRC = Entry(LabFr_General, font=f3, width=6)
eSOC = Entry(LabFr_General, font=f3, width=6)
eSOH = Entry(LabFr_General, font=f3, width=6)
eCycleCount = Entry(LabFr_General, font=f3, width=6)

#---- Unit ----#
unitVoltage = Label(LabFr_General,text = "Volt", font=f3, bg ='#ECECEC')
unitCurrent = Label(LabFr_General,text = "Ampere", font=f3, bg ='#ECECEC')
unitDC = Label(LabFr_General,text = "%", font=f3, bg ='#ECECEC')
unitFCC = Label(LabFr_General,text = "%", font=f3, bg ='#ECECEC')
unitRC = Label(LabFr_General,text = "%", font=f3, bg ='#ECECEC')
unitSOC = Label(LabFr_General,text = "%", font=f3, bg ='#ECECEC')
unitSOH = Label(LabFr_General,text = "%", font=f3, bg ='#ECECEC')
unitCycleCount = Label(LabFr_General,text = "Cycle", font=f3, bg ='#ECECEC')

#---- Grid ----#
labelVoltage.grid (row=0,column=0, padx=3,pady=3, sticky=W)
labelCurrent.grid (row=1,column=0, padx=3,pady=3, sticky=W)
labelDC.grid (row=2,column=0 ,padx=3,pady=3, sticky=W)
labelFCC.grid (row=3,column=0 ,padx=3,pady=3, sticky=W)
labelRC.grid (row=4,column=0 ,padx=3,pady=3, sticky=W)
labelSOC.grid (row=5,column=0 ,padx=3,pady=3, sticky=W)
labelSOH.grid (row=6,column=0 ,padx=3,pady=3, sticky=W)
labelCycleCount.grid (row=7,column=0 ,padx=3,pady=3, sticky=W)

eVoltage.grid(row=0,column=1, sticky=W)
eCurrent.grid(row=1,column=1, sticky=W)
eDC.grid(row=2,column=1, sticky=W)
eFCC.grid(row=3,column=1, sticky=W)
eRC.grid(row=4,column=1, sticky=W)
eSOC.grid(row=5,column=1, sticky=W)
eSOH.grid(row=6,column=1, sticky=W)
eCycleCount.grid(row=7,column=1, sticky=W)

unitVoltage.grid (row=0,column=3,padx=3,pady=3, sticky=W)
unitCurrent.grid (row=1,column=3,padx=3,pady=3, sticky=W)
unitDC.grid (row=2,column=3,padx=3,pady=3, sticky=W)
unitFCC.grid (row=3,column=3,padx=3,pady=3, sticky=W)
unitRC.grid (row=4,column=3,padx=3,pady=3, sticky=W)
unitSOC.grid (row=5,column=3,padx=3,pady=3, sticky=W)
unitSOH.grid (row=6,column=3,padx=3,pady=3, sticky=W)
unitCycleCount.grid (row=7,column=3,padx=3,pady=3, sticky=W)

#----------------- Temperatures -----------------#
LabFr_Temperatures = ttk.Labelframe(fr2, text='Temperatures (Celcius)', width=700, height=300, style='My.TFrame', borderwidth=2)
LabFr_Temperatures.grid(row=0,column=1, padx=0, pady =0, ipadx=3, ipady =3, sticky='nw')

#---- Variable Name ----#
labelMaxCT = Label(LabFr_Temperatures,text = "Max Cell Temp", font=f3, bg ='#ECECEC')
labelMinCT = Label(LabFr_Temperatures,text = "Min Cell Temp", font=f3, bg ='#ECECEC')
labelMaxFET = Label(LabFr_Temperatures,text = "Max FET Temp", font=f3, bg ='#ECECEC')
labelMaxPCB = Label(LabFr_Temperatures,text = "Max PCB Parts Temp", font=f3, bg ='#ECECEC')
labelCT1 = Label(LabFr_Temperatures,text = "Cell Temp 1", font=f3, bg ='#ECECEC')
labelCT2 = Label(LabFr_Temperatures,text = "Cell Temp 2", font=f3, bg ='#ECECEC')
labelCT3 = Label(LabFr_Temperatures,text = "Cell Temp 3", font=f3, bg ='#ECECEC')
labelFET = Label(LabFr_Temperatures,text = "FET Temp", font=f3, bg ='#ECECEC')
labelPCB = Label(LabFr_Temperatures,text = "PCB Parts Temp", font=f3, bg ='#ECECEC')

#---- Entry ----#
eMaxCT = Entry(LabFr_Temperatures, font=f3, width=6)
eMinCT = Entry(LabFr_Temperatures, font=f3, width=6)
eMaxFET = Entry(LabFr_Temperatures, font=f3, width=6)
eMaxPCB = Entry(LabFr_Temperatures, font=f3, width=6)
eCT1 = Entry(LabFr_Temperatures, font=f3, width=6)
eCT2 = Entry(LabFr_Temperatures, font=f3, width=6)
eCT3 = Entry(LabFr_Temperatures, font=f3, width=6)
eFET = Entry(LabFr_Temperatures, font=f3, width=6)
ePCB = Entry(LabFr_Temperatures, font=f3, width=6)

#---- Grid ----#
labelMaxCT.grid (row=0,column=0, padx=3,pady=3, sticky=W)
labelMinCT.grid (row=1,column=0, padx=3,pady=3, sticky=W)
labelMaxFET.grid (row=2,column=0, padx=3,pady=3, sticky=W)
labelMaxPCB.grid (row=3,column=0, padx=3,pady=3, sticky=W)
labelCT1.grid (row=4,column=0, padx=3,pady=3, sticky=W)
labelCT2.grid (row=5,column=0, padx=3,pady=3, sticky=W)
labelCT3.grid (row=6,column=0, padx=3,pady=3, sticky=W)
labelFET.grid (row=7,column=0, padx=3,pady=3, sticky=W)
labelPCB.grid (row=8,column=0, padx=3,pady=3, sticky=W)


eMaxCT.grid (row=0,column=1, padx=3,pady=3, sticky=W)
eMinCT.grid (row=1,column=1, padx=3,pady=3, sticky=W)
eMaxFET.grid (row=2,column=1, padx=3,pady=3, sticky=W)
eMaxPCB.grid (row=3,column=1, padx=3,pady=3, sticky=W)
eCT1.grid (row=4,column=1, padx=3,pady=3, sticky=W)
eCT2.grid (row=5,column=1, padx=3,pady=3, sticky=W)
eCT3.grid (row=6,column=1, padx=3,pady=3, sticky=W)
eFET.grid (row=7,column=1, padx=3,pady=3, sticky=W)
ePCB.grid (row=8,column=1, padx=3,pady=3, sticky=W)

#---- Notification ----#
LabFr_Notf = ttk.Labelframe(fr2, text='Notification', width=600, height=100, style='My.TFrame')
LabFr_Notf.grid(row=0,column=2, padx=0, pady =0, ipadx=3, ipady =3, sticky='nw')
eNotf = Text(LabFr_Notf, font=f3, height= 7, width = 32, undo=False)
eNotf.grid (row=0,column=0, padx=1,pady=1, sticky=W)

labelProfile = Label(LabFr_Notf,text = "Profile", font=f1, bg ='#ECECEC')
labelProfile.grid (row=1,column=0, padx=1,pady=1, sticky=W)

"""
labelManuName = Label(LabFr_Notf,text = "Manufacture Name:", font=f3, bg ='#ECECEC')
labelManuName.grid (row=2,column=0, padx=1,pady=1, sticky=W)
eManuName = Text(LabFr_Notf, font=f3, height= 1, width = 10)
eManuName.grid (row=3,column=0, padx=1,pady=1, sticky=W)

labelDevName = Label(LabFr_Notf,text = "Device Name:", font=f3, bg ='#ECECEC')
labelDevName.grid (row=4,column=0, padx=1,pady=1, sticky=W)
eDevName = Text(LabFr_Notf, font=f3, height= 1, width = 10)
eDevName.grid (row=5,column=0, padx=1,pady=1, sticky=W)
"""

labelSN = Label(LabFr_Notf,text = "Serial Number:", font=f3, bg ='#ECECEC')
labelSN.grid (row=6,column=0, padx=1,pady=1, sticky=W)
eSN = Entry(LabFr_Notf, font=f3, width=10)
eSN.grid (row=7,column=0, padx=1,pady=1, sticky=W)

labelBarcode = Label(LabFr_Notf,text = "Barcode:", font=f3, bg ='#ECECEC')
labelBarcode.grid (row=8,column=0, padx=1,pady=1, sticky=W)
eBarcode = Entry(LabFr_Notf, font=f3, width=20)
eBarcode.grid (row=9,column=0, padx=1,pady=1, sticky=W)
"""
## Status
labelModStat = Label(LabFr_Notf,text = "Module Status:", font=f3, bg ='#ECECEC')
labelModStat.grid (row=0,column=0, padx=3,pady=3, sticky=W)
eModStat = Text(LabFr_Notf, font=f3, height= 4, width = 20)
eModStat.grid (row=1,column=0, padx=3,pady=3, sticky=W)

## Warning
labelModWarn = Label(LabFr_Notf,text = "Module Warning:", font=f3, bg ='#ECECEC')
labelModWarn.grid (row=2,column=0, padx=3,pady=3, sticky=W)
eModWarn = Text(LabFr_Notf, font=f3, height= 4, width = 20)
eModWarn.grid (row=3,column=0, padx=3,pady=3, sticky=W)

## Alarm
labelModAlr = Label(LabFr_Notf,text = "Module Alarm:", font=f3, bg ='#ECECEC')
labelModAlr.grid (row=4,column=0, padx=3,pady=3, sticky=W)
eModAlr = Text(LabFr_Notf, font=f3, height= 4, width = 20)
eModAlr.grid (row=5,column=0, padx=3,pady=3, sticky=W)

## Error
labelModErr = Label(LabFr_Notf,text = "Module Error:", font=f3, bg ='#ECECEC')
labelModErr.grid (row=6,column=0, padx=3,pady=3, sticky=W)
eModErr = Text(LabFr_Notf, font=f3, height= 4, width = 20)
eModErr.grid (row=7,column=0, padx=3,pady=3, sticky=W)
"""

#----------------- Cell Voltage -----------------#
LabFr_CV = ttk.Labelframe(fr3, text='Cell Voltage (Volt)', width=700, height=100, style='My.TFrame')
LabFr_CV.grid(row=0,column=0, padx=0, pady =0, ipadx=5, ipady =5, sticky='ne')

#---- Variable Name ----#
labelC1V = Label(LabFr_CV,text = "1", font=f3, bg ='#ECECEC')
labelC2V = Label(LabFr_CV,text = "2", font=f3, bg ='#ECECEC')
labelC3V = Label(LabFr_CV,text = "3", font=f3, bg ='#ECECEC')
labelC4V = Label(LabFr_CV,text = "4", font=f3, bg ='#ECECEC')
labelC5V = Label(LabFr_CV,text = "5", font=f3, bg ='#ECECEC')
labelC6V = Label(LabFr_CV,text = "6", font=f3, bg ='#ECECEC')
labelC7V = Label(LabFr_CV,text = "7", font=f3, bg ='#ECECEC')
labelC8V = Label(LabFr_CV,text = "8", font=f3, bg ='#ECECEC')
labelC9V = Label(LabFr_CV,text = "9", font=f3, bg ='#ECECEC')
labelC10V = Label(LabFr_CV,text = "10", font=f3, bg ='#ECECEC')
labelC11V = Label(LabFr_CV,text = "11", font=f3, bg ='#ECECEC')
labelC12V = Label(LabFr_CV,text = "12", font=f3, bg ='#ECECEC')
labelC13V = Label(LabFr_CV,text = "13", font=f3, bg ='#ECECEC')
labelMaxCV = Label(LabFr_CV,text = "Max", font=f3, bg ='#ECECEC')
labelMinCV = Label(LabFr_CV,text = "Min", font=f3, bg ='#ECECEC')

#---- Entry ----#
eC1V = Entry(LabFr_CV, font=f3, width=5)
eC2V = Entry(LabFr_CV, font=f3, width=5)
eC3V = Entry(LabFr_CV, font=f3, width=5)
eC4V = Entry(LabFr_CV, font=f3, width=5)
eC5V = Entry(LabFr_CV, font=f3, width=5)
eC6V = Entry(LabFr_CV, font=f3, width=5)
eC7V = Entry(LabFr_CV, font=f3, width=5)
eC8V = Entry(LabFr_CV, font=f3, width=5)
eC9V = Entry(LabFr_CV, font=f3, width=5)
eC10V = Entry(LabFr_CV, font=f3, width=5)
eC11V = Entry(LabFr_CV, font=f3, width=5)
eC12V = Entry(LabFr_CV, font=f3, width=5)
eC13V = Entry(LabFr_CV, font=f3, width=5)
eMaxCV = Entry(LabFr_CV, font=f3, width=5)
eMinCV = Entry(LabFr_CV, font=f3, width=5)

#---- Grid ----#
labelC1V.grid (row=0,column=0, padx=1,pady=1, sticky='nsew')
labelC2V.grid (row=0,column=1, padx=1,pady=1, sticky='nsew')
labelC3V.grid (row=0,column=2, padx=1,pady=1, sticky='nsew')
labelC4V.grid (row=0,column=3, padx=1,pady=1, sticky='nsew')
labelC5V.grid (row=0,column=4, padx=1,pady=1, sticky='nsew')
labelC6V.grid (row=0,column=5, padx=1,pady=1, sticky='nsew')
labelC7V.grid (row=0,column=6, padx=1,pady=1, sticky='nsew')
labelC8V.grid (row=0,column=7, padx=1,pady=1, sticky='nsew')
labelC9V.grid (row=0,column=8, padx=1,pady=1, sticky='nsew')
labelC10V.grid (row=0,column=9, padx=1,pady=1, sticky='nsew')
labelC11V.grid (row=0,column=10, padx=1,pady=1, sticky='nsew')
labelC12V.grid (row=0,column=11, padx=1,pady=1, sticky='nsew')
labelC13V.grid (row=0,column=12, padx=1,pady=1, sticky='nsew')
labelMaxCV.grid (row=0,column=13, padx=1,pady=1, sticky='nsew')
labelMinCV.grid (row=0,column=14, padx=1,pady=1, sticky='nsew')

eC1V.grid (row=1,column=0, padx=1,pady=1, sticky=W)
eC2V.grid (row=1,column=1, padx=1,pady=1, sticky=W)
eC3V.grid (row=1,column=2, padx=1,pady=1, sticky=W)
eC4V.grid (row=1,column=3, padx=1,pady=1, sticky=W)
eC5V.grid (row=1,column=4, padx=1,pady=1, sticky=W)
eC6V.grid (row=1,column=5, padx=1,pady=1, sticky=W)
eC7V.grid (row=1,column=6, padx=1,pady=1, sticky=W)
eC8V.grid (row=1,column=7, padx=1,pady=1, sticky=W)
eC9V.grid (row=1,column=8, padx=1,pady=1, sticky=W)
eC10V.grid (row=1,column=9, padx=1,pady=1, sticky=W)
eC11V.grid (row=1,column=10, padx=1,pady=1, sticky=W)
eC12V.grid (row=1,column=11, padx=1,pady=1, sticky=W)
eC13V.grid (row=1,column=12, padx=1,pady=1, sticky=W)
eMaxCV.grid (row=1,column=13, padx=1,pady=1, sticky=W)
eMinCV.grid (row=1,column=14, padx=1,pady=1, sticky=W)

#---- Timestamp ----#
labelModTime = Label(fr4,text = "Latest Update:", font=f3, bg ='#ECECEC')
eModTime = Entry(fr4, font=f3, width=20)

labelModTime.grid (row=1,column=0, sticky=W)
eModTime.grid (row=1,column=1,sticky=W)

def refresh():
    try:
        with open(FolderPath + '/json/GenData.json') as json_data:
            GenDat = json.load(json_data)
        mod = mod_value.get()
        with open(FolderPath + '/json/mod%s.json' %mod) as json_data:
            Mod = json.load(json_data)

        ClearAll()
        
        eCV.insert(0,GenDat['CV'])
        eCCL.insert(0,GenDat['CCL'])
        eDCL.insert(0,GenDat['DCL'])
        eEDV.insert(0,GenDat['EDV'])
        eBV.insert(0,GenDat['Bus_Volt'])
        eBC.insert(0,GenDat['Bus_Curr'])
        eCap.insert(0,GenDat['Capacity'])
        eBT.insert(0,GenDat['BackupTime'])
        eDM.insert(0,GenDat['Detected_Mod'])
        eStat.insert('0.0',GenDat['Status'])
        eWarn.insert('0.0',GenDat['Warning'])
        eAlr.insert('0.0',GenDat['Alarm'])
        eErr.insert('0.0',GenDat['Error'])
        eOvTime.insert(0,GenDat['Timestamp'])
        
        eVoltage.insert(0,Mod['Voltage'])
        eCurrent.insert(0,Mod['Current'])
        eDC.insert(0,Mod['DC'])
        eFCC.insert(0,Mod['FCC'])
        eRC.insert(0,Mod['RC'])
        eSOC.insert(0,Mod['SOC'])
        eSOH.insert(0,Mod['SOH'])
        eCycleCount.insert(0,Mod['Cycle_Count'])
        eMaxCT.insert(0,Mod['Max_Cell_Temp'])
        eMinCT.insert(0,Mod['Min_Cell_Temp'])
        eMaxFET.insert(0,Mod['Max_FET_Temp'])
        eMaxPCB.insert(0,Mod['Max_PCB_Parts_Temp'])
        eCT1.insert(0,Mod['Cell_Temp1'])
        eCT2.insert(0,Mod['Cell_Temp2'])
        eCT3.insert(0,Mod['Cell_Temp3'])
        eFET.insert(0,Mod['FET_Temp'])
        ePCB.insert(0,Mod['PCB_Parts_Temp'])
        eC1V.insert(0,Mod['C1V'])
        eC2V.insert(0,Mod['C2V'])
        eC3V.insert(0,Mod['C3V'])
        eC4V.insert(0,Mod['C4V'])
        eC5V.insert(0,Mod['C5V'])
        eC6V.insert(0,Mod['C6V'])
        eC7V.insert(0,Mod['C7V'])
        eC8V.insert(0,Mod['C8V'])
        eC9V.insert(0,Mod['C9V'])
        eC10V.insert(0,Mod['C10V'])
        eC11V.insert(0,Mod['C11V'])
        eC12V.insert(0,Mod['C12V'])
        eC13V.insert(0,Mod['C13V'])
        eMaxCV.insert(0,Mod['Max_Cell_Voltage'])
        eMinCV.insert(0,Mod['Min_Cell_Voltage'])
        Notf = Mod['Status'] + Mod['Warning'] + Mod['Alarm'] + Mod['Error']
        eNotf.insert('0.0',Notf)
        eSN.insert(0,Mod['Serial_Number'])
        eBarcode.insert(0,Mod['BarCode'])
        eModTime.insert(0,Mod['Timestamp'])
        
    except Exception as e:
        print(e)
        pass

    gc.collect()    

    if Modbus:
        root.after(1000,refresh)

def printMem():
    try:
        memlog = 'GUI: '+ str(get_process_memory()[0]) + ' B|| SNMP: ' + str( get_process_memory()[1]) + ' B || Modbus: '+ str( get_process_memory()[2]) + ' B'
    except:
        memlog = 'GUI: '+ str(get_process_memory()[0]) + ' B|| SNMP: ' + str( get_process_memory()[1]) + ' B || Modbus: 0 B'
    currentTime = strftime("%Y-%m-%d %H:%M:%S", localtime())
    memlog = currentTime + " >>>> " + memlog + "\n"
    print(memlog)
    with open(FolderPath + '/json/memory.json', 'a') as file:
        file.write(memlog)

    root.after(60000,printMem)
    #root.after(1200000, printMem)
    #root.after(1000,printMem)

    
def ClearAll():
    eCV.delete(0,END)
    eCCL.delete(0,END)
    eDCL.delete(0,END)
    eEDV.delete(0,END)
    eBV.delete(0,END)
    eBC.delete(0,END)
    eCap.delete(0,END)
    eBT.delete(0,END)
    eDM.delete(0,END)
    eStat.delete('0.0',END)
    eWarn.delete('0.0',END)
    eAlr.delete('0.0',END)
    eErr.delete('0.0',END)
    eOvTime.delete(0,END)
    
    eVoltage.delete(0,END)
    eCurrent.delete(0,END)
    eDC.delete(0,END)
    eFCC.delete(0,END)
    eRC.delete(0,END)
    eSOC.delete(0,END)
    eSOH.delete(0,END)
    eCycleCount.delete(0,END)
    eMaxCT.delete(0,END)
    eMinCT.delete(0,END)
    eMaxFET.delete(0,END)
    eMaxPCB.delete(0,END)
    eCT1.delete(0,END)
    eCT2.delete(0,END)
    eCT3.delete(0,END)
    eFET.delete(0,END)
    ePCB.delete(0,END)
    eC1V.delete(0,END)
    eC2V.delete(0,END)
    eC3V.delete(0,END)
    eC4V.delete(0,END)
    eC5V.delete(0,END)
    eC6V.delete(0,END)
    eC7V.delete(0,END)
    eC8V.delete(0,END)
    eC9V.delete(0,END)
    eC10V.delete(0,END)
    eC11V.delete(0,END)
    eC12V.delete(0,END)
    eC13V.delete(0,END)
    eMaxCV.delete(0,END)
    eMinCV.delete(0,END)
    eNotf.delete('0.0',END)
    eSN.delete(0,END)
    eBarcode.delete(0,END)
    eModTime.delete(0,END)

    if not Modbus:
        root.after(1000,ClearAll)

printMem()    
mainloop()
