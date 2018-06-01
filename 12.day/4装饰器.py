def w1(fun):
	def gace():
		print("验证")
		fun()
	return gace
@w1
def foo():
	print("哈哈")

foo()

