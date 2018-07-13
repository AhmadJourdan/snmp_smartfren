import DB, psutil, gc
import time
from time import strftime, localtime
from GSPE_DCB105ZK import *
import json
from RegOID import Regs_Label,BitPos1_Label, BitPos2_Label, BitPos3_Label, BitPos4_Label
import os, inspect
import numpy as np

def get_process_memory():
    process = psutil.Process(os.getpid())
    return [process.memory_info().rss,process.memory_full_info().rss]

ModNum = 16

FolderPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

#Connecting to Database
db = DB.DataBase()

#Data Logging Interval (20 minutes)
Interval = 1200

GENDAT0 = {"CV": 0, "CCL": 0, "DCL": 0, "EDV": 0, "Status": "", "Warning": "",
           "Alarm": "", "Error": "", "Detected_Mod": 0, "Bus_Volt": 0,
           "Bus_Curr": 0, "Capacity": 0, "BackupTime": 0, "Timestamp": ""}

print('Working')
print('...')


t0 = time.time()
isDataAlreadyLogged = False

try:
    while 1:
        if isDataAlreadyLogged == True:
            t0 = time.time()
        
        Detected_Mod = 0
        battVolts = []
        battCurrs = []
        battSOCs = []
        status = []
        warning = []
        alarm = []
        error = []

        SNList = []

        for i in range(1,ModNum+1):
            while(True):
                try:
                    m = module('/dev/ttyUSB0',i)
                    #m = module('COM9',i)
                    #print('port opened')
                    break
                except Exception as e:
                    #print(e)
                    #print('Battery is not connected')
                    time.sleep(15)
                
            command = """currentTime%d"""%i + """ = strftime("%Y-%m-%d %H:%M:%S", localtime())"""
            exec(command)
            
            if i == 1:
                try:
                    command = """[GenDat, Data%d, StatVal%d, WarnVal%d, AlrVal%d, ErrVal%d ] = m.readAll()""" %(i,i,i,i,i)
                    exec(command)
                    #print(i, 'data reading==>success')
                    command = """battVolts.append(Data%d['Voltage'])"""%i
                    exec(command)
                    command = """battCurrs.append(Data%d['Current'])"""%i
                    exec(command)
                    command = """battSOCs.append(Data%d['SOC'])"""%i
                    exec(command)
                    command = """status.append(StatVal%d)"""%i
                    exec(command)
                    command = """warning.append(WarnVal%d)"""%i
                    exec(command)
                    command = """alarm.append(AlrVal%d)"""%i
                    exec(command)
                    command = """error.append(ErrVal%d)"""%i
                    exec(command)
                    command = """SNList.append(Data%d['Serial_Number'])"""%i
                    exec(command)
                    Detected_Mod +=1
                except Exception as e:
                    #print(e)
                    command = """Data%d = {key : 0 for key in Regs_Label[4:]}"""%i
                    exec(command)
                    #print(i, 'data reading==>failed')
            else:
                try:
                    command = """[Data%d, StatVal%d, WarnVal%d, AlrVal%d, ErrVal%d ] = m.readAll()""" %(i,i,i,i,i)
                    exec(command)
                    #print(i, 'data reading==>success')
                    command = """battVolts.append(Data%d['Voltage'])"""%i
                    exec(command)
                    command = """battCurrs.append(Data%d['Current'])"""%i
                    exec(command)
                    command = """battSOCs.append(Data%d['SOC'])"""%i
                    exec(command)
                    command = """status.append(StatVal%d)"""%i
                    exec(command)
                    command = """warning.append(WarnVal%d)"""%i
                    exec(command)
                    command = """alarm.append(AlrVal%d)"""%i
                    exec(command)
                    command = """error.append(ErrVal%d)"""%i
                    exec(command)
                    command = """SNList.append(Data%d['Serial_Number'])"""%i
                    exec(command)
                    Detected_Mod +=1
                except Exception as e:
                    #print(e)
                    command = """Data%d = {key : 0 for key in Regs_Label[4:]}"""%i
                    exec(command)
                    #print(i, 'data reading==>failed')

            _Data = {}
            command = """_Data.update(Data%d)"""%i
            exec(command)

            command = """_Data['Timestamp'] = currentTime%d"""%i
            exec(command)
            
            command = """
with open(FolderPath + '/json/mod%d.json', 'w') as file:
    file.write(json.dumps(_Data))""" %i

            exec(command)
            
            if i == ModNum:
                #print("Module :", Detected_Mod)
                if Detected_Mod ==  0:
                    GenDat = GENDAT0
                if GenDat != GENDAT0:
                    #transpose matrix
                    status = list(map(list, zip(*status)))
                    warning = list(map(list, zip(*warning)))
                    alarm = list(map(list, zip(*alarm)))
                    error = list(map(list, zip(*error)))
                    
                    gen_stat = ''
                    for r in range(0,len(status)):
                        if r == 0:
                            gen_stat += 'Charge_Operation_Mode: '
                            prot = [i+1 for i,x in enumerate(status[r]) if x ==0]
                            if len(prot) != 0:
                                gen_stat += 'Protection [' + ', '.join(str(e) for e in prot) + '], '
                            dis = [i+1 for i,x in enumerate(status[r]) if x ==1]
                            if len(dis) != 0:
                                gen_stat += 'Disable [' + ', '.join(str(e) for e in dis) + '], '
                            en = [i+1 for i,x in enumerate(status[r]) if x ==2]
                            if len(en) != 0:
                                gen_stat += 'Enable [' + ', '.join(str(e) for e in en) + ']. '
                            gen_stat += '\n'
                        elif r == 1:
                            gen_stat += 'Discharge_Operation_Mode: '
                            prot = [i+1 for i,x in enumerate(status[r]) if x ==0]
                            if len(prot) != 0:
                                gen_stat += 'Protection [' + ', '.join(str(e) for e in prot) + '], '
                            dis = [i+1 for i,x in enumerate(status[r]) if x ==1]
                            if len(dis) != 0:
                                gen_stat += 'Disable [' + ', '.join(str(e) for e in dis) + '], '
                            en = [i+1 for i,x in enumerate(status[r]) if x ==2]
                            if len(en) != 0:
                                gen_stat += 'Enable [' + ', '.join(str(e) for e in en) + ']. '
                            gen_stat += '\n'
                        else:
                            statMod = [i+1 for i,x in enumerate(status[r]) if x ==1]
                            if len(statMod) != 0:
                                gen_stat += BitPos1_Label[r] + '[' + ', '.join(str(e) for e in statMod) + ']\n'
                        r+=1
                    
                    GenDat['Status'] = gen_stat
                    
                    gen_warn = ''
                    for r in range(0,len(warning)):
                        warnMod = [i+1 for i,x in enumerate(warning[r]) if x ==1]
                        if len(warnMod) != 0:
                            gen_warn += BitPos2_Label[r] + '[' + ', '.join(str(e) for e in warnMod) + ']\n'
                        r+=1
                    
                    if gen_warn == '':
                        gen_warn = 'No Warning.'
                    GenDat['Warning'] = gen_warn

                    gen_alr = ''
                    for r in range(0,len(alarm)):
                        alrMod = [i+1 for i,x in enumerate(alarm[r]) if x ==1]
                        if len(alrMod) != 0:
                            gen_alr += BitPos3_Label[r] + '[' + ', '.join(str(e) for e in alrMod) + ']\n'
                        r+=1
                    
                    if gen_alr == '':
                        gen_alr = 'No Alarm.'
                    GenDat['Alarm'] = gen_alr
                        
                    gen_err = ''
                    for r in range(0,len(error)):
                        errMod = [i+1 for i,x in enumerate(error[r]) if x ==1]
                        if len(errMod) != 0:
                            gen_err += BitPos4_Label[r] + '[' + ', '.join(str(e) for e in errMod) + ']\n'
                        r+=1
                    
                    if gen_err == '':
                        gen_err = 'No Error.'
                    GenDat['Error'] = gen_err
                    
                    GenDat['Detected_Mod'] = Detected_Mod
                    GenDat['Bus_Volt'] = round(np.mean(battVolts),2)
                    GenDat['Bus_Curr'] = round(np.sum(battCurrs),2)
                    CapacityList = [round(i*56.7/100,2) for i in battSOCs]
                    GenDat['Capacity'] = round(np.sum(CapacityList),2)

                    
                    if GenDat['Bus_Curr'] < 0:
                        (hour, minute) = divmod(GenDat['Capacity'], abs(GenDat['Bus_Curr']))
                        minute = minute*60/abs(GenDat['Bus_Curr'])
                        GenDat['BackupTime'] = '%d h %d m' %(hour,minute)
                    else:
                        GenDat['BackupTime'] = 'Unknown (not Discharged)'

                _GenDat = {}
                command = """_GenDat.update(GenDat)"""
                exec(command)

                command = """_GenDat['Timestamp'] = currentTime%d"""%i
                exec(command)
                    
                command = """
with open(FolderPath + '/json/GenData.json', 'w') as file:
    file.write(json.dumps(_GenDat))"""

                exec(command)
                
                maxCTs = []
                minCTs = []
                battVolts = []
                battCurrs = []
                battSOCs = []
                alarm = []

        with open(FolderPath + '/json/Comm.json') as json_data:
            Comm = json.load(json_data)
        Comm['Active_Code']=1
        if 'Timestamp' in Comm:
            del Comm['Timestamp']
        _Comm = {}
        command = """_Comm.update(Comm)"""
        exec(command)

        command = """_Comm['Timestamp'] = currentTime%d"""%i
        exec(command)
                
        with open(FolderPath + '/json/Comm.json', 'w') as file:
            file.write(json.dumps(_Comm))

        #print(get_process_memory()[0])
        #print(get_process_memory()[1])
        gc.collect()
        t1 = time.time()
        if t1-t0 > Interval:
            if Detected_Mod != 0:
                for j in range(1, Detected_Mod+1):
                    command = """db.InsertData(%d,currentTime%d,Data%d)"""%(j,j,j)
                    exec(command)
                command = """db.InsertComm(currentTime%d,Comm)"""%j
                exec(command)
                command = """db.InsertGenData(currentTime%d,GenDat)"""%j
                exec(command)

                command = """print(currentTime%d, " ==> Logged [", Detected_Mod, "]")""" %j
                exec(command)
                
                isDataAlreadyLogged = True

                db.commit()
        else:
            isDataAlreadyLogged = False
            
except KeyboardInterrupt:
    print('Ended')
    
