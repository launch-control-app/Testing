import bluetooth
import random
import time 

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
    return str(",".join(data) + "\n")




socketIO = SocketIO('localhost', 4000, LoggingNamespace)
while True:
    socketIO.emit('data', getStringRandom())
    time.sleep(0.5)



