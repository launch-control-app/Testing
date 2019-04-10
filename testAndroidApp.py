# Creation Date: February 1st 2019
# Original Authors: Rohan Rao, Christian Francisco
# Contents of file: Mocks the microncontroller by sending fake OBD-II values over bluetooth to an android app
# FOR TESTING PURPOSES ONLY

import bluetooth
import random
import time

# Generate a comma-seperated string of values
def getString(counter):
    data = list()
    for i in range(19):
        #data.append("-999")
        data.append(str(random.randint(32, 45)))
    #data[1] = "-999"
    return str(",".join(data) + "\n")

server_socket= bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_socket.bind(("", bluetooth.PORT_ANY))
server_socket.listen(1)

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

# Start advertising the service
bluetooth.advertise_service(server_socket, "RaspiBtSrv",
                   service_id=uuid,
                   service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                   profiles=[bluetooth.SERIAL_PORT_PROFILE])

print("Now listening...")

counter = 0
# Outer loop - connect to client
while True:
    client_socket, address = server_socket.accept()
    print("Connected to client")

    # Inner loop - send data to client periodically
    while True:
        try:
            str_to_send = getString(counter)
            client_socket.send(str_to_send)
            print(str_to_send)
            if (counter == 255):
                counter = 0
            else:
                counter = 255
            time.sleep(0.20)
        except:
            print('Client disconnected')
            client_socket.close()
            break


server_socket.close()



