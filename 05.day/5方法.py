class Dag(object):
	__a = 0
	def __new__(cls):
		if cls.__a == None:
			cls.__a = object.__new__(cls)
			return cls.__a
		else:
			return cls.__a
	def __init__(self,name):
		self.name = name
dag1 = Dag()
dag2 = Dag()
dag3 = Dag()
dag4 = Dag()
dag5 = Dag()

print(id(dag1))
print(id(dag2))
print(id(dag3))
print(id(dag4))
print(id(dag5))











		
