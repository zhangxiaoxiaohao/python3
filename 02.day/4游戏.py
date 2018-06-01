class Boy():
	def __init__(self,age,height):
		self.age = age
		self.height = height
		self.games = []	
	
	def slleep(self):
		print("学习")
	def eat(self):
		print("在开车")
	def sss(self):
		print("年龄%s\n身高%s"%(self.age,self.height))
xiaoming = Boy(12,170)
xiaoming.slleep()
xiaoming.eat()
xiaoming.sss()


xiaohong = Boy(14,165)
xiaohong.slleep()
xiaohong.eat()
xiaohong.sss()
