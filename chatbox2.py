import socket
import sys
import datetime,time


s = socket.socket()
host = input("enter host id : ")
port = 8080
s.connect((host,port))
print('connection in established')
while 1:
    incoming_message = s.recv(10)
    incoming_message = incoming_message.decode()
    print('Pawan',incoming_message)
    print("received at:",datetime.datetime.now().time())
    print('\n')
    message = input(str('->'))
    message = message.encode()
    s.send(message)
    print("message delivered at:",datetime.datetime.now().time())
    print("\n")
    
