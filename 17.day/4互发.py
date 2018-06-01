from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.connect(("192.168.19.127",4444))
s.send("今晚布吃饭".encode('gb2312'))
while True:
	content = s.recv(1024)
	print(content.decode('gb2312'))
s.close()
