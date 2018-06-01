from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.bind(('',11111))
s.listen(5)
newSocket,info= s.accept()
while True:
	msg = newSocket.recv(1024)
	print(msg.decode('gb2312'))
newSocket.close()
s.close()
