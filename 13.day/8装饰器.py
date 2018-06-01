def w2(fn):
	def a():
		print(123)
		fn()
	return a
def w1(fn):
	def a():
		print(456)
		fn()
	return a
@w2
@w1
def test3():
	print(789)
#test3 = w1(test3)
#test3 = w2(test3)
test3()

