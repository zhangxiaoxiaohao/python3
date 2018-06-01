class Person():
	def __init__(self,name):
		self.name = name
		self.gun = None
		self.hp = 100
	def zhuangzidan(self,danjia,bullet):
		danjia.addbullet(bullet)
	def zhuangdanjia(self,danjia,bullet):
		gun.addDanjia(danjia)
	def takeGun(self,gun):
		self.gun = gun
	def openGun(self,diren):
		if diren.hp > 0:
		zidan = self.gun.popGunllet()
		zidan.kill(diren)
class Gun():
	def __init__(self,name):
		self.name = name
		self.danjia = None
	def addDanjia(self,danjia):
		self.danjia = danjia
		print(id(self.danjia))
	def popGunBullet(self):
		return self.danjia.popBullet()

class Danjia():

	def __init__(self,size)
		self.size = size
		self.bullet_list = []
	def addbullet(self,bullet):
		self.bullet_list.append(bullet)

	def popBullet(self):
		return self.bullet_list.pop()
class Bullet():
	def __init__(self):
		self.weili = 5
	def kill(self,diren):
		diren.hp -= self.weili
		print("剩余血量%d"%diren.hp)
laowang = person("老王")
ak47 = Gun("ak47")
danjia = Danjia(20)
for i in range(20):
	bullet = bullet()
	laowang.zhangzidan(danjia,bullet)
lanwang.zhuangdanjia(ak47,danjia)

laosong = person("老宋")

laowang.takeGun(ak47)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)


