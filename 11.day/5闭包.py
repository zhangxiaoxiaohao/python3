def line(a,b):
	def line1(x):
		return a*x + b
	return line1
line2 = line(1,1)
line3 = line(4,5)
print(line2(5))
print(line3(5))
