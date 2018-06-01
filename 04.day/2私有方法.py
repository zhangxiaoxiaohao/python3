class Msg():
	def __sendMsg(self,money):
		money -= 1
		print("短信,扣钱")
	def publicSend(self,money):
		if money <= 0:
			print("发送失败")
		else:
			self.__sendMsg(money)
msg = Msg()
msg.publicSend(15)
