import socket
import json


print("Listening for files...")
port = 6000
listenerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP Socket for listener.
listenerSocket.bind(('', port))


while True:

    rec = listenerSocket.recvfrom(1024)
    data = json.loads(rec[0].decode('utf-8'))
    print(f"Username: {str(data['username'])}, Files: {str(data['files'])} ") #Displaying username and files keys.






