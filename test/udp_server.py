import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9000))
print 'Bind UDP on 9000'
while True:
	data,addr = s.recvfrom(1024)
	print 'Recived from %s:%s'%addr
	s.send('Hello,%s!' %data)