class DateTest():
	def __init__(self,year,month,day):
		self.year = year
		self.month = month
		self.day = day
	def OutDate(self):
		print("%年%月%日"%(self.year,self.month,self.day))
	@classmethod
	def handleDate(cls,date):
		a,b,c = date.split("-")
		d = cls(a,b,c)
		return d
str = "2018-05-29"
d = DateTest.handleDate(str)
d.OutDate







