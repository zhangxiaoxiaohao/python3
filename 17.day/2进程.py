from socket import *
from threading import Thread
s = None
ip = ''
port = 0
def send():
	while True:
		content = input("输入要输入的内容:\n")
		s.sendto(content.encode('gb2312'),(ip,port))
def recv():
	while True:
		msg = s.recvfrom(1024)
		print("%s-----%s"%(msg[0].decode('gb2312'),msg[1][0]),end='')
def main():
	global s
	global ip
	global port
	ip = input("请输入对方ip:")
	port = int(input("请输入对方端口:"))
	s = socket(AF_INET,SOCK_DGRAM)
	s.bind(('',6666))
	t = Thread(target=send)
	t1 = Thread(target = recv)
	t.start()
	t1.start()
	t.join()
	t1.join()
if __name__ == '__main__':
	main()	
