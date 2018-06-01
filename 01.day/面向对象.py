class niao():
	def a_niao(self):
		print("鸟吃虫子")
	def b_niao(self):
		print("鸟在筑巢")
	def c_niao(self):
		print("鸟在孵蛋")
class yu():
	def a_yu(self):
		print("鱼在水里游")
	def b_yu(self):
		print("大鱼在吃小鱼")
	def c_yu(self):
		print("小鱼在吃草")
def s_name():
	name = niao()
	name.a_niao()
	name.b_niao()
	name.c_niao()
name = input("请输入名字")
s_name()
def name():	
	name1 = yu()
	name1.a_yu()
	name1.b_yu()
	name1.c_yu()	
name1 = input("请输入名字")
name()
