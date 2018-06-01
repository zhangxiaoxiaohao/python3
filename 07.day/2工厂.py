class Op(object):
	def __init__(self,num1 = 0,num2 = 0):
		self.num1 = num1
		self.num2 = num2
	def getResult(self):
		pass	
class Jia(Op):
	def getResuit(self):
		return self.num1+self.num2
class Jian(Op):
	def getResuit(self):
		return self.num1-self.num2
class Cheng(Op):
	def getResuit(self):
		return self.num1*self.num2
class Chu(Op):
	def getResuit(self):
		if self.num2!=0:
			return self.num1/self.num2
class Factory(object):
	def create_Op(self,type):
		if type == "+":
			return Jia()
		elif type == "-":
			return Jian()
		elif type == "*":
			return Cheng()
		elif type == "/":
			return Chu()
xiao = Factory()
jia = xiao.create_Op("+")
jia.num1 = 5
jia.num2 = 5
print(jia.getResuit())
