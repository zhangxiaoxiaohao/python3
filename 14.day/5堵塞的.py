from multiprocessing import Pool
import time
import os
def work():
	for i in range(3):
		time.sleep(1)
		print("哈哈哈哈哈pid=%d"%os.getpid())
p = Pool(3)
for i in range(10):
	print(i)
	p.apply(work)
p.close()
p.join()







