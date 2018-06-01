from threading import Thread
import time
import threading
def work():
	name = threading.current_thread().name
	print(name)
	num = 1
	if name == "Thread-1":
		num += 1
		time.sleep(1)
		print("哈哈%d"%num)
	else:
		time.sleep(1)
		print("呵呵%d"%num)
t = Thread(target = work)
t.start()
t1 = thread(target = work)
t1.start()
