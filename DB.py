from time import strftime, localtime
import MySQLdb
from RegOID import *
import csv
import os, inspect, json

FolderPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
with open(FolderPath + '/json/Comm.json') as json_data:
    Comm = json.load(json_data)
if 'Timestamp' in Comm:
    del Comm['Timestamp']
if 'Active_Code' in Comm:
    del Comm['Active_Code']

Comm_Label = list(Comm.keys())
Comm_Val = list(Comm.values())

class DataBase(object):
    def __init__(self):
        self.connection = MySQLdb.connect(host = "localhost",
                              user = "gspe",
                              #user = "root",
                              passwd = "gspe-intercon",
                              #passwd = "",
                              db = "PanasonicDCB105ZK")
        self.cursor = self.connection.cursor()

    def drop(self):
        for i in range(1,17):
            self.cursor.execute("""DROP TABLE Module%d"""%i)
        self.cursor.execute("""DROP TABLE GeneralData""")
        self.cursor.execute("""DROP TABLE Communication""")
            
    def clearRecords(self):
        for i in range(1,17):
            self.cursor.execute("""DELETE FROM Module%d;"""%i)
        self.cursor.execute("""DELETE FROM GeneralData;""")
        self.cursor.execute("""DELETE FROM Communication;""")

    def create(self):
        #Communication TABLE
        self.command = """CREATE TABLE Communication(
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Timestamp DATETIME,
    Active_Code INT,
    """
        for j in range(0,len(Comm_Label)):
            self.command += Comm_Label[j]
            if j == 6:
                if Comm_Label[j] == 'snmpPort' or Comm_Label[j] == 'snmpVersion':
                    self.command += """ INT
    )"""
                else:
                    self.command += """ VARCHAR(256)
    )"""
            else:
                if Comm_Label[j] == 'snmpPort' or Comm_Label[j] == 'snmpVersion':
                    self.command += """ INT,
    """
                else:
                    self.command += """ VARCHAR(256),
    """
                
        #print(self.command)
        self.cursor.execute(self.command)
        
        #GENERAL DATA TABLE
        self.command = """CREATE TABLE GeneralData(
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Timestamp DATETIME,
    """
        for j in range(0,4):
            self.command += Reg1_Label[j]
            if j == 3:
                self.command += """ FLOAT,
    Bus_Volt FLOAT,
    Bus_Curr FLOAT,
    Detected_Mod FLOAT,
    Capacity FLOAT,
    BackupTime VARCHAR(256),
    Status TEXT,
    Warning TEXT,
    Alarm TEXT,
    Error TEXT
    )"""
            else:
                self.command += """ FLOAT,
    """

        #print(self.command)
        self.cursor.execute(self.command)
        
        #MODULE SPECIFIC DATA TABLE
        for i in range(1,17):
            self.command = """CREATE TABLE Module%d(
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Timestamp DATETIME,
    """%(i)
            for k in range(4,len(Reg1_Label)):
                self.command += Reg1_Label[k]
                self.command += """ FLOAT,
    """
            for k in range(0,len(Reg2_Label)):
                self.command += Reg2_Label[k]
                if Reg2_Label[k] == 'Serial_Number':
                    self.command += """ INT,
    """
                else:
                    self.command += """ VARCHAR(256),
    """
            for k in range(0,len(Reg3_Label)):
                self.command += Reg3_Label[k]
                if k == len(Reg3_Label)-1:
                    self.command += """ TEXT
    )"""
                else:
                    self.command += """ TEXT,
    """
            #print(self.command)
            self.cursor.execute(self.command)
        
    def InsertData(self,mod,timestamp,val_dict):
        format_str = """INSERT INTO Module%d(Timestamp, """ %(mod)

        key = list(val_dict.keys())
        val = list(val_dict.values())
        
        for j in range(0,len(key)):
            if j == len(key)-1:
                format_str += key[j]  + ') VALUES ('
            else:
                format_str += key[j] + ', '

        format_str += '"{Timestamp}", '
        
        for j in range(0,len(key)):
            if j == len(key)-1:
                format_str += '"{'+ key[j] + '}"' + ')'
            else:
                format_str += '"{'+ key[j] + '}"' + ', '
        #print(format_str)

        command = "sql_command = format_str.format(Timestamp = timestamp, "

        for j in range(0,len(key)):
            if j == len(list(key))-1:
                command += key[j] +'=val[%d]'%j + ')' 
            else:
                command += key[j] +'=val[%d]'%j + ', '
        #print(command)
        exec(command)
        self.cursor.execute(locals() ['sql_command'])

    def InsertGenData(self,timestamp,val_dict):
        format_str = """INSERT INTO GeneralData(Timestamp, """

        key = list(val_dict.keys())
        val = list(val_dict.values())
        
        for j in range(0,len(key)):
            if j == len(key)-1:
                format_str += key[j] + ') VALUES ('
            else:
                format_str += key[j] + ', '

        format_str += '"{Timestamp}", '
        
        for j in range(0,len(key)):
            if j == len(key)-1:
                format_str += '"{'+ key[j] + '}")'
            else:
                format_str += '"{'+ key[j] + '}"' + ', '
        #print(format_str)

        command = "sql_command = format_str.format(Timestamp = timestamp, "

        for j in range(0,len(key)):
            if j == len(list(key))-1:
                command += key[j] +'=val[%d]'%j + ')' 
            else:
                command += key[j] +'=val[%d]'%j + ', '
        #print(command)
        exec(command)
        self.cursor.execute(locals() ['sql_command'])

    def InsertComm(self,timestamp,val_dict):
        format_str = """INSERT INTO Communication(Timestamp, """
        key = list(val_dict.keys())
        val = list(val_dict.values())
        
        for j in range(0,len(key)):
            if j == len(key)-1:
                format_str += key[j] + ') VALUES ('
            else:
                format_str += key[j] + ', '

        format_str += '"{Timestamp}", '
        
        for j in range(0,len(key)):
            if j == len(key)-1:
                format_str += '"{'+ key[j] + '}"' + ')'
            else:
                format_str += '"{'+ key[j] + '}"' + ', '
        #print(format_str)

        command = "sql_command = format_str.format(Timestamp = timestamp, "
        
        for j in range(0,len(key)):
            if j == len(list(key))-1:
                command += key[j] +'=val[%d]'%j + ')' 
            else:
                command += key[j] +'=val[%d]'%j + ', '
        #print(command)
        exec(command)
        self.cursor.execute(locals() ['sql_command'])
    
    #Function to commit any changes in local database
    def commit(self):
        self.connection.commit()

    #Function to close connection to local database
    def close(self):
        self.connection.close()
        
#a = DataBase()
#a.drop()
#a.clearRecords()
#a.create()
#currentTime = strftime("%Y-%m-%d %H:%M:%S", localtime())
#a.InsertData(1,currentTime,{'Voltage':1})
#a.InsertGenData(currentTime,{'CV':1})
#a.commit()
#a.close()
