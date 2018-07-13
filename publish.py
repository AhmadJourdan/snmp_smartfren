import DB
import os, inspect
from time import localtime, strftime
import sys, json, time
import paho.mqtt.client as mqtt

#Connecting to Database
db = DB.DataBase()

FolderPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
ModNum = 16
    
#Host address (Thingsboard)
HOST = '35.232.145.106'

#Access token
TOKEN = 'gspe-smartfren'

#Open connection to thingsboard
client = mqtt.Client()

client.username_pw_set(TOKEN)

client.connect(HOST,1883,60)

#Reading and pushing data to cloud interval (in sec)
INTERVAL = 20

#Set the time for next reading
next_reading = time.time()

#starting loop
client.loop_start()

previousMonth = int(strftime("%m", localtime()))
with open(FolderPath + '/json/Comm.json') as json_data:
    Comm = json.load(json_data)
with open(FolderPath + '/json/GenData.json') as json_data:
    GenData = json.load(json_data)

try:
    while(True):
        currentTime = strftime("%Y-%m-%d %H:%M:%S", localtime())
        client.publish('v1/devices/me/telemetry', json.dumps(Comm),1)
        client.publish('v1/devices/me/telemetry', json.dumps(GenData),1)
        for i in range(1,17):
            with open(FolderPath + '/json/mod%d.json' %i) as json_data:
                data = json.load(json_data)
            keys = list(data.keys())
            for item in keys:
                data[item + '[%d]' %i] = data.pop(item)

            client.publish('v1/devices/me/telemetry', json.dumps(data),1)
        
        #set the time for the next reading
        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time>0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass

#End of program
client.loop_stop()
client.disconnect()
for i in range(1, modNum+1):
    command = "db%d.close()" %(i)
    exec(command)
