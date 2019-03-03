# Creation Date: Saturday, March 2nd 2019
# Original Authors: Rohan Rao
# Contents of file: Mocks the android app by sending fake OBD-II values over web sockets to the web server
# FOR TESTING PURPOSES ONLY

import random
import time 
import datetime
import json

from socketIO_client_nexus import SocketIO, LoggingNamespace

# Generate a comma-seperated string of values
def getString(counter):
    data = list()
    for i in range(19):
        data.append(str(random.randint(75, 100)))
    data[12] = str(counter)
    return str(",".join(data) + "\n")

def getStringRandom():
    data = list()
    for i in range(19):
        data.append(str(random.randint(75, 100)))
    
    data.append(str(datetime.datetime.now()))
    return str(",".join(data) + "\n")


def getJSONString():
    jsonDict = {
        "VIN" : "19023749012", 
        "RPM" : "0",
        "calculatedEngineLoad" : "0",
        "absoluteEngineLoad" : "0",
        "engineOilTemperature" : "0",
        "torquePercentage" : "0",
        "referenceTorque" : "0",
        "intakeTemperature" : "0",
        "intakePressure" : "0",
        "flowPressure" : "0",
        "engineCoolantTemperature" : "0",
        "barometricPressure" : "0",
        "vehicleSpeed" : "0",
        "engineRunningTime" : "0",
        "vehicleRunningDistance" : "0",
        "throttlePosition" : "0",
        "ambientTemperature" : "0",
        "controlModuleVoltage" : "0",
        "fuelLevel" : "0",
        "dateTimeStamp" : "0"
    }

    jsonDict["VIN"] = str(random.randint(75, 100))
    jsonDict["RPM"] = str(random.randint(75, 100))
    jsonDict["calculatedEngineLoad"] = str(random.randint(10000, 15000))
    jsonDict["absoluteEngineLoad"] = str(random.randint(75, 100))
    jsonDict["engineOilTemperature"] = str(random.randint(75, 100))
    jsonDict["torquePercentage"] = str(random.randint(75, 100))
    jsonDict["referenceTorque"] = str(random.randint(75, 100))
    jsonDict["intakeTemperature"] = str(random.randint(75, 100))
    jsonDict["flowPressure"] = str(random.randint(75, 100))
    jsonDict["barometricPressure"] = str(random.randint(75, 100))
    jsonDict["vehicleSpeed"] = str(random.randint(75, 100))
    jsonDict["engineRunningTime"] = str(random.randint(75, 100))
    jsonDict["engineCoolantTemperature"] = str(random.randint(75, 100))
    jsonDict["vehicleRunningDistance"] = str(random.randint(75, 100))
    jsonDict["throttlePosition"] = str(random.randint(75, 100))
    jsonDict["ambientTemperature"] = str(random.randint(75, 100))
    jsonDict["controlModuleVoltage"] = str(random.randint(75, 100))
    jsonDict["fuelLevel"] = str(random.randint(75, 100))
    jsonDict["dateTimeStamp"] = str(datetime.datetime.now())

    jsonString = json.dumps(jsonDict)

    return jsonString



socketIO = SocketIO('localhost', 4000, LoggingNamespace)
while True:
    # socketIO.emit('data', getStringRandom())
    socketIO.emit('data', getJSONString())
    time.sleep(0.5)



