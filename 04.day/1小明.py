class person():
	def __init__(self):
		self.__money = 100
	def getmoney(self):
		return self.__money
	def setmoney(self,money):
		if money > 0:
			self.__money = money
		else:
			print("输入非法")
xiaoming = person()
0xiaoming.setmoney(300)
print(xiaoming.getmoney())



