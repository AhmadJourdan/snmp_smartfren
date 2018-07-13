from time import localtime, strftime
import json
import minimalmodbus
from RegOID import *
import time

minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL=True

#Function to read the value (0 or 1) of a certain bitnumber
def readbitval(data, bitnumber):
    dat = data
    mask = 2**bitnumber
    c = dat & mask
    c = c>>bitnumber
    return c

class module(object):
    def __init__(self, port, deviceAddress):
        self.Port = port
        self.DevAdd = deviceAddress
        self.Mod = minimalmodbus.Instrument(self.Port, self.DevAdd)

    #Function to read the battery profile
    def readID(self,registerlist):
        result = []
        addr = registerlist
        result.append(self.Mod.read_string(addr[0],8,4).rstrip(' \t\r\n\0'))
        result.append(self.Mod.read_string(addr[1],8,4).rstrip(' \t\r\n\0'))
        #result.append(self.Mod.read_register(addr[2],0,4))
        result.append(self.Mod.read_register(addr[2],0,4))
        #result.append(hex(self.Mod.read_register(addr[4],0,4)))
        #result.append(hex(self.Mod.read_register(addr[5],0,4)))
        result.append(self.Mod.read_string(addr[3],8,4).rstrip(' \t\r\n\0'))
        return result

    def getData(self):
        #t0 = time.time()
        self.battM = {}
        self.genDat = {}
        val = []
        for i in range(0,len(Reg1_Val)):
            val += self.Mod.read_registers(Reg1_Val[i][0], len(Reg1_Val[i]),4)
        
        #General Data (only on slaveAddress = 1)
        val1 = val[0:4]
        
        for i in range(0,4):
            self.genDat[Reg1_Label[i]] = val1[i]
        for i in DivBy100_1:
            self.genDat[i] = self.genDat[i]/100
        for i in DivBy1000_1:
            self.genDat[i] = self.genDat[i]/1000
        
        #Module Specific Data
        val2 = val[4:]
        
        for i in range(4,len(Reg1_Label)):
            self.battM[Reg1_Label[i]] = val2[i-4]
            
        self.battM['Current'] = self.Mod.read_register(5148,0,4,True)
        
        for i in DivBy10_2:
            self.battM[i] = self.battM[i]/10
        for i in DivBy100_2:
            self.battM[i] = self.battM[i]/100
        for i in DivBy1000_2:
            self.battM[i] = self.battM[i]/1000
        
        
        #t1 = time.time()
        #print(str(t1-t0))
        if self.DevAdd == 1:
            return [self.genDat, self.battM]
        else:
            return self.battM

    def getStatus(self):
        #t0 = time.time()
        
        self.Status = {}
        val = []
        
        v = self.Mod.read_register(Reg3_Val[0],0,4)
        
        for i in range(0,len(BitPos1_Val)):
            if i > 1:
                val.append(readbitval(v,BitPos1_Val[i]))
            else:
                MSB = readbitval(v,BitPos1_Val[i][0][0])
                LSB = readbitval(v,BitPos1_Val[i][0][1])
                val.append(MSB<<1 | LSB)
        
        for i in range(0,len(BitPos1_Label)):
            if i > 1:
                self.Status[BitPos1_Label[i]] = val[i]
            else:
                self.Status[BitPos1_Label[i]] = BitPos1_Val[i][1][val[i]]
                
        self.StatusKeys = list(self.Status.keys())
        self.StatusVals = list(self.Status.values())
        
        self.mod_stat = ''

        self.index = 0
        self.statCount = 0
        
        for item in self.StatusVals:
            if self.index > 1:
                if item == 1:
                    self.mod_stat += str(self.StatusKeys[self.index])
                    self.statCount += 1
                    if self.statCount > 1:
                        self.mod_stat += ', '
                    elif self.statCount == 1:
                        self.mod_stat += '.'
            else:
                self.mod_stat += str(self.StatusKeys[self.index]) + ': '+ str(self.StatusVals[self.index]) + '\n'
                
            self.index += 1
        self.dat = {}
        self.dat['Status'] = self.mod_stat
        #t1 = time.time()
        #print(str(t1-t0))
        
        return [self.dat, val]


    def getWarning(self):
        #t0 = time.time()

        self.Warning = {}
        val = []
        
        v = self.Mod.read_register(Reg3_Val[1],0,4)
        
        for i in range(0,len(BitPos2_Val)):
            val.append(readbitval(v,BitPos2_Val[i]))
        
        for i in range(0,len(BitPos2_Label)):
            self.Warning[BitPos2_Label[i]] = val[i]
                
        self.WarningKeys = list(self.Warning.keys())
        self.WarningVals = list(self.Warning.values())
        
        self.mod_warn = ''

        self.index = 0
        self.WarningCount = 0
        
        for item in self.WarningVals:
            if item == 1:
                self.mod_warn += str(self.WarningKeys[self.index])
                self.mod_warn += '\n'
                self.WarningCount += 1  
            self.index += 1
        if self.WarningCount == 0:
            self.mod_warn = 'No Warning. \n'
            
        self.dat = {}
        self.dat['Warning'] = self.mod_warn
        #t1 = time.time()
        #print(str(t1-t0))
        
        return [self.dat, val]
    
    def getAlarm(self):
        #t0 = time.time()
        
        self.Alarm = {}
        val = []
        
        v = self.Mod.read_register(Reg3_Val[2],0,4)
        v2 = self.Mod.read_register(18,0,4)
        
        for i in range(0,len(BitPos3_Val)):
            if i == len(BitPos3_Val)-1:
                val.append(readbitval(v2,BitPos3_Val[i]))
            else:
                val.append(readbitval(v,BitPos3_Val[i]))
        
        for i in range(0,len(BitPos3_Label)):
            self.Alarm[BitPos3_Label[i]] = val[i]
                
        self.AlarmKeys = list(self.Alarm.keys())
        self.AlarmVals = list(self.Alarm.values())
        
        self.mod_alr = ''

        self.index = 0
        self.AlarmCount = 0
        
        for item in self.AlarmVals:
            if item == 1:
                self.mod_alr += str(self.AlarmKeys[self.index])
                self.mod_alr += '\n'
                self.AlarmCount += 1  
            self.index += 1
        if self.AlarmCount == 0:
            self.mod_alr = 'No Alarm. \n'
            
        self.dat = {}
        self.dat['Alarm'] = self.mod_alr
        #t1 = time.time()
        #print(str(t1-t0))
        return [self.dat, val]

    def getError(self):
        #t0 = time.time()
        
        self.Error = {}
        val = []
        
        v = self.Mod.read_register(Reg3_Val[3],0,4)
        
        for i in range(0,len(BitPos4_Val)):
            val.append(readbitval(v,BitPos4_Val[i]))
        
        for i in range(0,len(BitPos4_Label)):
            self.Error[BitPos4_Label[i]] = val[i]
                
        self.ErrorKeys = list(self.Error.keys())
        self.ErrorVals = list(self.Error.values())
        
        self.mod_Err = ''

        self.index = 0
        self.ErrorCount = 0
        
        for item in self.ErrorVals:
            if item == 1:
                self.mod_Err += str(self.ErrorKeys[self.index])
                self.mod_Err += '\n'
                self.ErrorCount += 1  
            self.index += 1
        if self.ErrorCount == 0:
            self.mod_Err = 'No Error. \n'
            
        self.dat = {}
        self.dat['Error'] = self.mod_Err
        #t1 = time.time()
        #print(str(t1-t0))
        return [self.dat, val]
    
    def getID(self):
        #t0 = time.time()
        self.idtt = {}
        self.dat = self.readID(Reg2_Val)
        for i in range(0,len(Reg2_Label)):
            self.idtt[Reg2_Label[i]]=self.dat[i]
        #t1 = time.time()
        #print(str(t1-t0))
        return self.idtt

    def readAll(self):
        if self.DevAdd == 1:
            [self.GenData,self.dat1] = self.getData()
            [self.dat2, self.StatVal] = self.getStatus()
            [self.dat3, self.WarnVal] = self.getWarning()
            [self.dat4, self.AlrVal] = self.getAlarm()
            [self.dat5, self.ErrVal] = self.getError()
            self.dat6 = self.getID()
            self.data = {**self.dat1,**self.dat2,**self.dat3,**self.dat4,**self.dat5,**self.dat6}
            return [self.GenData, self.data, self.StatVal, self.WarnVal, self.AlrVal, self.ErrVal]
        
        else:
            self.dat1 = self.getData()
            [self.dat2, self.StatVal] = self.getStatus()
            [self.dat3, self.WarnVal] = self.getWarning()
            [self.dat4, self.AlrVal] = self.getAlarm()
            [self.dat5, self.ErrVal] = self.getError()
            self.dat6 = self.getID()
            self.data = {**self.dat1,**self.dat2,**self.dat3,**self.dat4,**self.dat5,**self.dat6}
            return [self.data, self.StatVal, self.WarnVal, self.AlrVal, self.ErrVal]


#m = module('COM4',1)
#ta = time.time()
#a = m.readAll()
#tb = time.time()
#print(str(tb-ta))
#for i in a:
    #print(i)
    #print('========================================================')




