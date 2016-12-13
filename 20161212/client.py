#coding = utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1',8080))

s.listen(5)

while True:
   
    connection,address=s.accept()
    buf = connection.recv(1024)
    connection.send(buf)

s.close()
    