#coding=utf-8
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',9000))
s.listen(5)
print 'server begin in 127.0.0.1:9891'
while True:
    c,addr = s.accept()

    print 'client get connect'
    c.send('Welcome!')
    c.close()
