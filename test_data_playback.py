import bluetooth
import random
import time

filename = "test_run_march_3.txt"
f.open(filename)

server_socket= bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_socket.bind(("", bluetooth.PORT_ANY))
server_socket.listen(1)

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

# Start advertising the service
bluetooth.advertise_service(server_socket, "RaspiBtSrv",
                   service_id=uuid,
                   service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                   profiles=[bluetooth.SERIAL_PORT_PROFILE])

while True:
    client_socket, address = server_socket.accept()
    print("Connected to client")

    # Inner loop - send data to client periodically
    for line in f:
        try:
            client_socket.send(line)
            print(line)
            time.sleep(0.5)
        except:
            print('Client disconnected')
            client_socket.close()
            break

server_socket.close()