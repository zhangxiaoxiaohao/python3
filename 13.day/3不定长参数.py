def w1(fun):
	
	def inner(*args,**kwargs):
		print("---验证---")
		print(*args)
		ret = fun(*args,**kwargs)
		return ret
	return inner
@w1
def test(a,b):
	print("a==%d b==%d"%(a,b))
	return "呵呵呵"
@w1
def test1():
	print("哈哈")
test1()
print(test(1,2))
