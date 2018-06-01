from threading import Tread
import time
import threading
g_num = 100
def work():
	global g_num
	g_num +=1
	print("%s---%d"%(threading.current_thread().name,g_num))
































