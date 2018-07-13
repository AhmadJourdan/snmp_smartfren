####################################
#### Modbus Register Dictionary ####
####################################

#1. Battery Measurement
Reg1 = {
        'CV'            : [5128],
        'CCL'           : [5129],
        'DCL'           : [5130],
        'EDV'           : [5131],
        
        'DC'            : [5135],
        'FCC'           : [5136],
        'RC'            : [5137],
        'SOC'           : [5138],
        'SOH'           : [5139],
        'Cycle_Count'   : [5140],
        'Voltage'       : [5144],
        'Max_Cell_Voltage' : [5145],
        'Min_Cell_Voltage' : [5146],
        'Current'       : [5148],
        'Max_Cell_Temp' : [5152],
        'Min_Cell_Temp' : [5153],
        'Max_FET_Temp' : [5154],
        'Max_PCB_Parts_Temp' : [5155],
        'Cell_Temp1'    : [5160],
        'Cell_Temp2'    : [5161],
        'Cell_Temp3'    : [5162],
        'FET_Temp'      : [5163],
        'PCB_Parts_Temp': [5164],
        'C1V'           : [5168],
        'C2V'           : [5169],
        'C3V'           : [5170],
        'C4V'           : [5171],
        'C5V'           : [5172],
        'C6V'           : [5173],
        'C7V'           : [5174],
        'C8V'           : [5175],
        'C9V'           : [5176],
        'C10V'          : [5177],
        'C11V'          : [5178],
        'C12V'          : [5179],
        'C13V'          : [5180],
        }

Reg1_Label = list(Reg1.keys())
Reg1_Val = []
for i in list(Reg1.values()):
    if len(Reg1_Val)==0:
        Reg1_Val.append(i)
    else:
        if (i[0]-Reg1_Val[-1][-1])==1:
            Reg1_Val[-1]+=i
        else:
            Reg1_Val.append(i)

#2. Identity
Reg2 = {
        'Manufacture_Name'          : 5184,
        'Device_Name'               : 5192,
        #'Manufacture_Date'          : 5200,
        'Serial_Number'             : 5201,
        #'Program_Version'           : 5204,
        #'DATA_Version'              : 5205,
        'BarCode'                   : 5208,
         }

Reg2_Label = list(Reg2.keys())
Reg2_Val = list(Reg2.values())

#3. Flags
Reg3 = {'Status'    : 5120,
        'Warning'   : 5121,
        'Alarm'     : 5122,
        'Error'     : 5123,
        }

Reg3_Label = list(Reg3.keys())
Reg3_Val = list(Reg3.values())

Regs = {**Reg1, **Reg2, **Reg3}
Regs_Label = list(Regs.keys())
Regs_Val = list(Regs.values())


#Bit_Position
#Module Status Flags
BitPos1 = {'Charge_Operation_Mode' : [[0,1],['Protection', 'Disable', 'Enable']],
           'Discharge_Operation_Mode' : [[2,3],['Protection', 'Disable', 'Enable']],
           'Charging' : 4,
           'Battery_Installed': 7,
           'Fully_Charged': 8,
           'Fully_Discharged': 9,
           'Charge_Warning': 10,
           'Discharge_Warning': 11,
           'Terminate_Charge_Alarm': 12,
           'Terminate_Discharge_Alarm': 13,
           'Permanent_Failure': 15,
          }

BitPos1_Label = list(BitPos1.keys())
BitPos1_Val = list(BitPos1.values())

#Module Warning Flags
BitPos2 = {'Over_Cell_Voltage_Warning' : 0,
           'Remaining_Capacity_Alarm' : 1,
           'Under_Voltage_Warning' : 2,
           'Cell_Imbalance_Warning' : 3,
           'Over_Charge_Current_Warning': 4,
           'Over_Discharge_Current_Warning' : 6,
           'Over_Cell_Temperature_Warning_For_Charge' : 8,
           'Under_Cell_Temperature_Warning_For_Charge' : 9,
           'Over_Cell_Temperature_Warning_For_Discharge' : 10,
           'Under_Cell_Temperature_Warning_For_Discharge' : 11,
           'FET_Overheat_Warning' : 12,
           'PCB_Overheat_Warning' : 13,
           }

BitPos2_Label = list(BitPos2.keys())
BitPos2_Val = list(BitPos2.values())

#Module Alarm Flags
BitPos3 = {'Over_Cell_Voltage_Protection': 0,
           'Over_Total_Voltage_Protection': 1,
           'Under_Voltage_Protection': 2,
           'Discharge_Cut_Off_Protection': 3,
           'Over_Charge_Current_SW_Protection': 4,
           'Over_Discharge_Current_SW_Protection': 6,
           'Over_Discharge_Current_HW_Protection': 7,
           'Over_Cell_Temperature_Protection_For_Charge': 8,
           'Under_Cell_Temperature_Protection_For_Charge': 9,
           'Over_Cell_Temperature_Protection_For_Discharge': 10,
           'Under_Cell_Temperature_Protection_For_Discharge': 11,
           'FET_Overheat_Protection': 12,
           'PCB_Overheat_Protection': 13,
           'Module_Isolated':1,
           }

BitPos3_Label = list(BitPos3.keys())
BitPos3_Val = list(BitPos3.values())

#Module Error Flags
BitPos4 = {'Over_Voltage_Error_SW': 0,
           'Over_Voltage_Error_HW': 1,
           'Low_Voltage_Error': 2,
           'Cell_Imbalance_Error': 3,
           'Charge_FET_Error': 4,
           'Discharge_FET_Error': 5,
           'Current_Fuse_Error': 6,
           'Scp_Error': 7,
           'Cell_Overheat_Error': 8,
           'Thermistor-Error': 10,
           'AFE_Communication_Error': 11,
           'Calibration_Data_Error': 12,
           'Firmware_Checksum_Error': 13,
           'PCB_System_Error': 14,
           'Cell_Permanent_Failure': 15,
           }

BitPos4_Label = list(BitPos4.keys())
BitPos4_Val = list(BitPos4.values())

###################################################
#### Variables List which need to be processed ####
###################################################
DivBy10_1 = []
DivBy10_2 = ['Min_Cell_Temp','Max_Cell_Temp','Max_FET_Temp','Max_PCB_Parts_Temp','FET_Temp','SOC','SOH', 'Cell_Temp1', 'Cell_Temp2', 'Cell_Temp3', 'PCB_Parts_Temp']

DivBy100_1 = ['CV', 'EDV','CCL', 'DCL']
DivBy100_2 = ['Current', 'Voltage']

DivBy1000_1 = []
DivBy1000_2 = ['Max_Cell_Voltage', 'Min_Cell_Voltage','C1V', 'C2V', 'C3V', 'C4V', 'C5V', 'C6V',
             'C7V', 'C8V', 'C9V', 'C10V', 'C11V', 'C12V', 'C13V', 'FCC', 'RC', 'DC']


##############################
#### SNMP OIDs Dictionary ####
##############################
sysOID = '.1.3.6.1.4.1.10000.10.1'


#1. Overview
ovw = sysOID + '.10'
overview_oids = {'CV'            : ovw + '.10',
                'CCL'           : ovw + '.20',
                'DCL'           : ovw + '.30',
                'EDV'           : ovw + '.40',
                'Bus_Volt'      : ovw + '.50',
                'Bus_Curr'      : ovw + '.60',
                'Capacity'      : ovw + '.70',
                'BackupTime'    : ovw + '.80',
                'Detected_Mod'  : ovw + '.90',
                'Status'        : ovw + '.100',
                'Warning'       : ovw + '.110',
                'Alarm'         : ovw + '.120',
                'Error'         : ovw + '.130',
                }

overview_oids = {v: k for k, v in overview_oids.items()}
overview_oids_Label = list(overview_oids.keys())
overview_oids_Val = list(overview_oids.values())
#print(overview_oids)

#2. Communication
comm = sysOID + '.20'
Comm_oids = {'ipAddress'         : comm + '.10',
             'netMask'           : comm + '.20',
             'gateway'           : comm + '.30',
             'snmpVersion'       : comm + '.40',
             'snmpCommunity'     : comm + '.50',
             'snmpPort'          : comm + '.60',
             'sysOID'            : comm + '.70',
            }

Comm_oids = {v: k for k, v in Comm_oids.items()}
Comm_oids_Label = list(Comm_oids.keys())
Comm_oids_Val = list(Comm_oids.values())
#print(Comm_oids)

#3. Module
Module = sysOID + '.30'

#General
Gen = Module + '.10.15.1'
Mod_oids1 = {'Voltage'    : Gen + '.10',
             'Current'    : Gen + '.20',
             'DC'         : Gen + '.30',
             'FCC'        : Gen + '.40',
             'RC'         : Gen + '.50', 
             'SOC'        : Gen + '.60',
             'SOH'        : Gen + '.70',
             'Cycle_Count': Gen + '.80'
            }

#Temperatures
Temps = Module + '.20.15.1'
Mod_oids2 = {'Max_Cell_Temp'        : Temps + '.10',
             'Min_Cell_Temp'        : Temps + '.20',
             'Max_FET_Temp'         : Temps + '.30',
             'Max_PCB_Parts_Temp'   : Temps + '.40',
             'Cell_Temp1'           : Temps + '.50',
             'Cell_Temp2'           : Temps + '.60',
             'Cell_Temp3'           : Temps + '.70',
             'FET_Temp'             : Temps + '.80',
             'PCB_Parts_Temp'       : Temps + '.90',
             }
    
#Cell Voltage
CellVolt = Module + '.30.15.1'
Mod_oids3 = {'Max_Cell_Voltage'  : CellVolt + '.10',
             'Min_Cell_Voltage'  : CellVolt + '.20',
             'C1V'             : CellVolt + '.30',
             'C2V'             : CellVolt + '.40',
             'C3V'             : CellVolt + '.50',
             'C4V'             : CellVolt + '.60',
             'C5V'             : CellVolt + '.70',
             'C6V'             : CellVolt + '.80',
             'C7V'             : CellVolt + '.90',
             'C8V'             : CellVolt + '.100',
             'C9V'             : CellVolt + '.110',
             'C10V'            : CellVolt + '.120',
             'C11V'            : CellVolt + '.130',
             'C12V'            : CellVolt + '.140',
             'C13V'            : CellVolt + '.150',
             }

#Notification
Notf = Module + '.40.15.1'
Mod_oids4 = {'Status'   : Notf + '.10',
             'Warning'  : Notf + '.20',
             'Alarm'    : Notf + '.30',
             'Error'    : Notf + '.40',
             }

#Profile
Prof = Module + '.50.15.1'
Mod_oids5 = {'Manufacture_Name'  : Prof + '.10',
             'Device_Name'       : Prof + '.20',
             'Serial_Number'     : Prof + '.30',
             'BarCode'           : Prof + '.40'
             }

Mod_oids = {**Mod_oids1, **Mod_oids2, **Mod_oids3, **Mod_oids4, **Mod_oids5}
Mod_oids = {v: k for k, v in Mod_oids.items()}
Mod_oids_Label = list(Mod_oids.keys())
Mod_oids_Val = list(Mod_oids.values())
#print(Mod_oids)



