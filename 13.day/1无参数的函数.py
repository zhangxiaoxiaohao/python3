def w1(fun):
	
	def inner():
		print("---验证---")
		return fun()
	return inner
@w1
def test():
	print("哈哈哈")
	return "呵呵呵"
print(test())
