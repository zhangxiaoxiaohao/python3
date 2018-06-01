def w1(fun):
	def gace():
		print("验证")
		fun()
	return gace
def foo():
	print("哈哈")

foo = w1(foo)
foo()

