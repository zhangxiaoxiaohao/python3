import threading 
from time import sleep,ctime
def sing():
	for i in range(3):
		print("在唱歌")
		sleep(1)
def dance():
	for i in range(3):
		print("正在跳舞")
		sleep(1)
if __name__ == '__main__':
	print('开始')
	t1 = threading.Thread(target = sing)
	t2 = thread.Thread(target = dance)
	t1.start()
	t2.start()
	print('结')











