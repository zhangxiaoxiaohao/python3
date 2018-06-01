def w1(fun):
	
	def inner(a,b):
		print("---验证---")
		ret = fun(a,b)
		return ret
	return inner
@w1
def test(a,b):
	print("a==%d b==%d"%(a,b))
	return "呵呵呵"
print(test(1,2))
