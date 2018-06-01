def fib():
	n = 0
	a,b = 0,1
	while n < 10:
		print(b)
		a,b = b,a+b
		n+=1
fib()
