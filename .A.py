import sys
import pysnmp
from pysnmp.smi.mibs.instances import *
from pysnmp.entity import engine, config
from pysnmp.entity.rfc3413 import cmdrsp, context
from pysnmp.carrier.asynsock.dgram import udp
from pysnmp.proto.api import v2c
import random
from RegOID import *
#from GSPE_DCB105ZK import *
import time, os, inspect, json
from DataType import dataType

FolderPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

while(True):
    try:
        with open(FolderPath + '/json/Comm.json') as json_data:
            Comm = json.load(json_data)

        sysOID = Comm['sysOID'].split('.')[1:]
        sysOID = list(map(int,sysOID))
        sysOID = tuple(sysOID)

        # Create SNMP engine
        snmpEngine = engine.SnmpEngine()

        # Transport setup

        # UDP over IPv4
        config.addSocketTransport(
            snmpEngine,
            udp.domainName,
            udp.UdpTransport().openServerMode((Comm['ipAddress'], int(Comm['snmpPort'])))
        )

        # SNMPv2c setup

        # SecurityName <-> CommunityName mapping.
        config.addV1System(snmpEngine, 'my-area', Comm['snmpCommunity'])

        # Allow read MIB access for this user / securityModels at VACM
        config.addVacmUser(snmpEngine, int(Comm['snmpVersion']), 'my-area', 'noAuthNoPriv', sysOID, sysOID)


        # Create an SNMP context
        snmpContext = context.SnmpContext(snmpEngine)

        # --- create custom Managed Object Instance ---

        mibBuilder = snmpContext.getMibInstrum().getMibBuilder()

        MibScalar, MibScalarInstance = mibBuilder.importSymbols(
            'SNMPv2-SMI', 'MibScalar', 'MibScalarInstance'
        )

        class MyStaticMibScalarInstance(MibScalarInstance):
            def setValue(self, value, name, idx):
                
                self.nm = tuple(map( str , name ) )
                self._oid = list(self.nm)[0:-1]
                self._oid = '.'+'.'.join(self._oid)
                   
                #Communication Data
                if self._oid in Comm_oids.keys():
                    self.varName = Comm_oids[self._oid]

                    if dataType[self.varName] == 'Float':
                        value = float(value)
                    elif dataType[self.varName] == 'Integer':
                        value = int(value)
                    elif dataType[self.varName] == 'Boolean':
                        value = int(value)
                    elif dataType[self.varName] == 'String':
                        value = str(value)
                        
                    Comm[self.varName] = value

                    with open(FolderPath + '/json/Comm.json', 'w') as file:
                        file.write(json.dumps(Comm))
                        
                    #print('changed: ' + self.varName)
                        
                    return self.getSyntax().clone(str(self.varVal))
            
            def getValue(self, name, idx):
                
                self.nm = tuple(map( str , name ) )
                self._oid = list(self.nm)[0:-1]
                self._oid = '.'+'.'.join(self._oid)

                #Communication Data
                if self._oid in Comm_oids.keys():
                    self.varName = Comm_oids[self._oid]
                    self.varVal = Comm[self.varName]
                    
                    #print('requested: ' + self.varName)
                    
                #General Data
                elif self._oid in overview_oids_Label:
                    with open(FolderPath + '/json/GenData.json') as json_data:
                        GenData = json.load(json_data)
                    self.varName = overview_oids[self._oid]
                    self.varVal = GenData[self.varName]
                    
                    #print('requested: ' + self.varName)

                #Module
                else:
                    self.mod = int(list(self.nm)[-2])
                        
                    with open(FolderPath + '/json/mod%d.json' %self.mod) as json_data:
                        data = json.load(json_data)
                        
                    self._oid = list(self.nm)[0:-2]
                    self._oid = '.'+'.'.join(self._oid)
                    self.varName = Mod_oids[self._oid]
                    self.varVal = data[self.varName]

                    #print('requested: ' + self.varName + ' of module %d' %self.mod)
                                   
                return self.getSyntax().clone(str(self.varVal))
   
        ###############################  Overview  ###################################
        pre = sysOID + (10,)        
        #Charging Voltage
        command ="""
mibBuilder.exportSymbols(
  '__MY_MIB', MibScalar(%s, v2c.OctetString()),
              MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
)""" %(pre+(10,),pre+(10,))
        exec(command)

        #Charging Current Limit
        command ="""
mibBuilder.exportSymbols(
  '__MY_MIB', MibScalar(%s, v2c.OctetString()),
              MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
)""" %(pre+(20,),pre+(20,))
        exec(command)

        #Discharging Current Limit
        command ="""
mibBuilder.exportSymbols(
  '__MY_MIB', MibScalar(%s, v2c.OctetString()),
              MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
)""" %(pre+(30,),pre+(30,))
        exec(command)

        #End of Discharge Voltage
        command ="""
mibBuilder.exportSymbols(
  '__MY_MIB', MibScalar(%s, v2c.OctetString()),
              MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
)""" %(pre+(40,),pre+(40,))
        exec(command)

        #BusVolt
        command ="""
mibBuilder.exportSymbols(
  '__MY_MIB', MibScalar(%s, v2c.OctetString()),
              MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
)""" %(pre+(50,),pre+(50,))
        exec(command)

        #BusCurr
        command ="""
mibBuilder.exportSymbols(
  '__MY_MIB', MibScalar(%s, v2c.OctetString()),
              MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
)""" %(pre+(60,),pre+(60,))
        exec(command)

        #Capacity
        command ="""
mibBuilder.exportSymbols(
  '__MY_MIB', MibScalar(%s, v2c.OctetString()),
              MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
)""" %(pre+(70,),pre+(70,))
        exec(command)

        #BackupTime
        command ="""
mibBuilder.exportSymbols(
  '__MY_MIB', MibScalar(%s, v2c.OctetString()),
              MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
)""" %(pre+(80,),pre+(80,))
        exec(command)

        #DetectedMod
        command ="""
mibBuilder.exportSymbols(
  '__MY_MIB', MibScalar(%s, v2c.OctetString()),
              MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
)""" %(pre+(90,),pre+(90,))
        exec(command)

        #Status
        command ="""
mibBuilder.exportSymbols(
  '__MY_MIB', MibScalar(%s, v2c.OctetString()),
              MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
)""" %(pre+(100,),pre+(100,))
        exec(command)

        #Warning
        command ="""
mibBuilder.exportSymbols(
  '__MY_MIB', MibScalar(%s, v2c.OctetString()),
              MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
)""" %(pre+(110,),pre+(110,))
        exec(command)

        #Alarm
        command ="""
mibBuilder.exportSymbols(
  '__MY_MIB', MibScalar(%s, v2c.OctetString()),
              MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
)""" %(pre+(120,),pre+(120,))
        exec(command)

        #Error
        command ="""
mibBuilder.exportSymbols(
  '__MY_MIB', MibScalar(%s, v2c.OctetString()),
              MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
)""" %(pre+(130,),pre+(130,))
        exec(command)

        ###############################  Communication  ###################################
        pre = sysOID + (20,)

        #IP Address
        command ="""
mibBuilder.exportSymbols(
  '__MY_MIB', MibScalar(%s, v2c.OctetString()).setMaxAccess('readwrite'),
              MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
)""" %(pre+(10,),pre+(10,))
        exec(command)

        #Netmask
        command ="""
mibBuilder.exportSymbols(
  '__MY_MIB', MibScalar(%s, v2c.OctetString()).setMaxAccess('readwrite'),
              MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
)""" %(pre+(20,),pre+(20,))
        exec(command)

        #Gateway
        command ="""
mibBuilder.exportSymbols(
  '__MY_MIB', MibScalar(%s, v2c.OctetString()).setMaxAccess('readwrite'),
              MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
)""" %(pre+(30,),pre+(30,))
        exec(command)

        #SNMP Version
        command ="""
mibBuilder.exportSymbols(
  '__MY_MIB', MibScalar(%s, v2c.OctetString()).setMaxAccess('readwrite'),
              MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
)""" %(pre+(40,),pre+(40,))
        exec(command)

        #SNMP Community
        command ="""
mibBuilder.exportSymbols(
  '__MY_MIB', MibScalar(%s, v2c.OctetString()).setMaxAccess('readwrite'),
              MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
)""" %(pre+(50,),pre+(50,))
        exec(command)

        #SNMP Port
        command ="""
mibBuilder.exportSymbols(
  '__MY_MIB', MibScalar(%s, v2c.OctetString()).setMaxAccess('readwrite'),
              MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
)""" %(pre+(60,),pre+(60,))
        exec(command)

        #System OID
        command ="""
mibBuilder.exportSymbols(
  '__MY_MIB', MibScalar(%s, v2c.OctetString()).setMaxAccess('readwrite'),
              MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
)""" %(pre+(70,),pre+(70,))
        exec(command)

        ###############################  Module  ###################################
        #### General ####
        pre = sysOID + (30,10,15,1,)
        #Voltage
        for i in range(1,17):
            command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(10,i),pre+(10,i))
            exec(command)

        #Current
        for i in range(1,17):
            command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(20,i),pre+(20,i))
            exec(command)

        #DC
        for i in range(1,17):
            command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(30,i),pre+(30,i))
            exec(command)
            
        #FCC
        for i in range(1,17):
            command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(40,i),pre+(40,i))
            exec(command)

        #RC
        for i in range(1,17):
            command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(50,i),pre+(50,i))
            exec(command)

        #SOC
        for i in range(1,17):
            command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(60,i),pre+(60,i))
            exec(command)

        #SOH
        for i in range(1,17):
            command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(70,i),pre+(70,i))
            exec(command)

        #Cycle Count
        for i in range(1,17):
            command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(80,i),pre+(80,i))
            exec(command)
            
        #### Temperatures ####
        pre = sysOID + (30,20,15,1,)
        #MaxCellTemp
        for i in range(1,17):
            command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(10,i),pre+(10,i))
            exec(command)

        #MinCellTemp
        for i in range(1,17):
            command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(20,i),pre+(20,i))
            exec(command)

        #MaxFETTemp
        for i in range(1,17):
            command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(30,i),pre+(30,i))
            exec(command)
            
        #MaxPCBPartsTemp
        for i in range(1,17):
            command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(40,i),pre+(40,i))
            exec(command)

        #CellTemp
        for i in range(1,4):
            for j in range(1,17):
                command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(40+(i*10),j),pre+(40+(i*10),j))
                exec(command)

        #FET_Temp
        for i in range(1,17):
            command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(80,i),pre+(80,i))
            exec(command)

        #PCB_Part_Temp
        for i in range(1,17):
            command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(90,i),pre+(90,i))
            exec(command)
            
        #### CellVoltage ####
        pre = sysOID + (30,30,15,1,)

        #MaxCellVoltage
        for i in range(1,17):
            command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(10,i),pre+(10,i))
            exec(command)

        #MinCellVoltage
        for i in range(1,17):
            command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(20,i),pre+(20,i))
            exec(command)

        #CellVoltage
        for i in range(1,14):
            for j in range(1,17):
                command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(20+(i*10),j),pre+(20+(i*10),j))
                exec(command)

        #### Notification ####
        pre = sysOID + (30,40,15,1,)

        #ModuleStatus
        for i in range(1,17):
            command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(10,i),pre+(10,i))
            exec(command)

        #ModuleWarning
        for i in range(1,17):
            command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(20,i),pre+(20,i))
            exec(command)

        #ModuleAlarm
        for i in range(1,17):
            command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(30,i),pre+(30,i))
            exec(command)

        #ModuleError
        for i in range(1,17):
            command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(40,i),pre+(40,i))
            exec(command)

        #### Profile ####
        pre = sysOID + (30,50,15,1,)

        #ManufactureName
        for i in range(1,17):
            command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(10,i),pre+(10,i))
            exec(command)

        #DeviceName
        for i in range(1,17):
            command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(20,i),pre+(20,i))
            exec(command)

        #SerialNumber
        for i in range(1,17):
            command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(30,i),pre+(30,i))
            exec(command)

        #Barcode
        for i in range(1,17):
            command ="""
mibBuilder.exportSymbols(
      '__MY_MIB', MibScalar(%s, v2c.OctetString()),
                  MyStaticMibScalarInstance(%s, (0,), v2c.OctetString())
    )""" %(pre+(40,i),pre+(40,i))
            exec(command)

        # --- end of Managed Object Instance initialization ----

        # Register SNMP Applications at the SNMP engine for particular SNMP context
        cmdrsp.GetCommandResponder(snmpEngine, snmpContext)
        cmdrsp.NextCommandResponder(snmpEngine, snmpContext)
        cmdrsp.BulkCommandResponder(snmpEngine, snmpContext)
        cmdrsp.SetCommandResponder(snmpEngine, snmpContext)

        # Register an imaginary never-ending job to keep I/O dispatcher running forever
        snmpEngine.transportDispatcher.jobStarted(1)

        # Run I/O dispatcher which would receive queries and send responses
        try:    
            print("SNMP is Running.")
            snmpEngine.transportDispatcher.runDispatcher()
        except:
            snmpEngine.transportDispatcher.closeDispatcher()
            raise
    except Exception as e:
        print(e)
        
