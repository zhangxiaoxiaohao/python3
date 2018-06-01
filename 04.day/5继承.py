#coding=utf-8
class person():
	def __init__(self):
		self.__weight = 50

	def getweight(self):
		return self.__weight
	
	def chifang(self):
		print("会吃饭")
	
	def zoulu(self):
		print("会走路")

class Son(person):
	pass

xiaoming = Son()
xiaoming.chifang()
xiaoming.zoulu()
print(xiaoming.getweight())





