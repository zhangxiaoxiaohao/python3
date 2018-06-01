from multiprocessing import Process
import time
import os
def test(arg):
	for i in range(5):
		time.sleep(1)
		print("哈哈哈%s pid =%d"%(arg,os.getpid()))


p = Process(target=test,args=("laowang",))
p.start()

p.join(3)
print("呵呵呵呵")
