import socket
import sys
import datetime,time


sock = socket.socket()
host = socket.gethostname()
print('server will start on host',host)
port = 8080
sock.bind((host,port))
print('-'*40)
print("server has binded up host and port")
print("-"*40)
print("waiting for incoming connection")
sock.listen(1)
conn, addr = sock.accept()
print(addr, 'conected......')
print('\n')
while 1:
    message = input(str('->'))
    message = message.encode()
    conn.send(message)
    print("** message delivered at:",datetime.datetime.now().time())
    print("\n")
    incoming_message = conn.recv(10)
    incoming_message = incoming_message.decode()
    print('virat : ',incoming_message)
    print("received at: ",datetime.datetime.now().time())
