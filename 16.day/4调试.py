from socket import *



#创建udp

s = socket(AF_INET,SOCK_DGRAM)



s.sendto("嘎嘎".encode("gb2312"),("192.168.19.127",8080))



s.close()
