class Home():
	def __init__(self,area,addres,atype):
		self.area = area
		self.addres = addres
		self.atype = atype
		self.jiaju = []
	def __str__(self):
		mag = "房子是%s万\n房子在%s\n房子面积%s"%(self.area,self.addres,self.atype)
		return mag
	def addBed(self,bed):
		if self.atype >= bed.getArea():
			self.jiaju.append(bed)
			self.atype -= bed.getArea()
			print("加入成功")
		else:
			print("面积不够了")
	def switch(self):
		if self.dengs[0].getIsopen():
			self.dengs[0].close()
		else:
			self.dengs[0].open()

class Bed():
	def __init__(self,name,area,color,btype):
		self.name = name
		self.area = area
		self.color = color
		self.btype = btype
	def __str__(self):
		mag = "床的品牌是%s\n床的面积%s\n颜色是%s\n床的类型%s"%(self.name,self.area,self.color,self.btype)
		return mag
	def getArea(self):
		return self.area
class light():
	def __init__(self,name):
		self.name = name
		self.isopen = False
	def __str__(self):
		mag = "我是%s"%self.name
		return mag
	def open(self):
		self.isopen = True
		print("灯亮了")
	def close(self):
		self.isopen = False
		print("灯灭了")
	def getIsopen(self):
		return self.isopen
name = Home(150,"在四海",200)
print(name)
ximengsi = Bed("席梦思",40,"黄色","木床")
aladingshengdeng = light("阿拉丁神灯")
print(aladingshengdeng)
print(ximengsi)
name.addBed(ximengsi)
name.addBed(ximengsi)
name.addBed(ximengsi)
name.addBed(ximengsi)
name.addBed(ximengsi)
name.addBed(ximengsi)
name.addBed(ximengsi)
name.addBed(ximengsi)






