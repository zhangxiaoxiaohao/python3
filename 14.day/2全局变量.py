import os 
import time
ret = os.fork()
num = 0
if ret == 0:
	num += 1
	time.sleep(5)
	print("我是子类")
	print("我是子类num%d"%num)
else:
	time.sleep(2)
	num += 1
	print("我是父类")
	print("我是父类num%d"%num)
print("哈哈哈")
