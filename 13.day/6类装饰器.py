class Dag(object):
	def __init__(self,fun):
		print("初始化")
		self.__fun = fun
	def __call__(self):
		print("验证")
		self.__fun()
@Dag
def test():
	print("haha")
test()
