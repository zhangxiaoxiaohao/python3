import pygame
from PlanSprite import *
pygame.init()
class PlaneGame(object):
	def __init__(self):
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		self.clock = pygame.time.Clock()
		self.__create_sprites()
		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
		pygame.time.set_timer(CREATE_BULLET_EVENT,500)
		self.enemy_group = pygame.sprite.Group()
		#敌机销毁精灵组
		self.enemy1_down_group = pygame.sprite.Group()
		self.count = 0
		self.score = 0 #分数


	def __create_sprites(self):
		bg1 = Background()
		bg2 = Background(True)
		self.back_group = pygame.sprite.Group(bg1,bg2)

		self.hero = Hero()
		self.hero_group = pygame.sprite.Group(self.hero) 
	def start_game(self):
		print("开始游戏")
		while True:
			self.clock.tick(FRAME_PER_SEC)
			self.__event_handler()
			self.__check_collide()
			self.__update_sprites()
			pygame.display.update()
	def __event_handler(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				PlaneGame.game_over()
			elif event.type == CREATE_ENEMY_EVENT:
				enemy = Enemy()
				self.enemy_group.add(enemy)
			elif event.type == CREATE_BULLET_EVENT:
				self.hero.fire()
			keys_pressed = pygame.key.get_pressed()
			if keys_pressed[pygame.K_RIGHT]:
				self.hero.speed = 8
				self.hero.speed1 = 0
			elif keys_pressed[pygame.K_LEFT]:
				self.hero.speed = -8
				self.hero.speed1 = 0
			elif keys_pressed[pygame.K_UP]:
				self.hero.speed1 = -8
				self.hero.speed = 0
			elif keys_pressed[pygame.K_DOWN]:
				self.hero.speed1 = 8
				self.hero.speed = 0
			else:
				self.hero.speed1 = 0
				self.hero.speed = 0
	def __check_collide(self):
		  # 1. 子弹摧毁敌机

			#敌机精灵组在前 并返回敌机的精灵

		enemy_down = pygame.sprite.groupcollide(self.enemy_group,self.hero.bullet_group, True, True)
		enemy1_down_group.add(enemy_down)#加入到销毁组
		enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
		if len(enemies) > 0:
			# 让英雄牺
			self.hero.kill()
			# 结束游戏
			PlaneGame.game_over()
	def __update_sprites(self):
		self.back_group.update()
		self.back_group.draw(self.screen)

		self.enemy_group.update()
		self.enemy_group.draw(self.screen)

		self.hero_group.update()
		self.hero_group.draw(self.screen)
		
		self.hero.bullet_group.update()
		self.hero.bullet_group.draw(self.screen)
		self.hero.bullet_group.update()

		self.hero.bullet_group.draw(self.screen)
		self.drawText(str(self.score),SCREEN_RECT.width - 30,50)
		#敌机销毁
		for enemy1_down in enemy1_down_group:
			self.screen.blit(enemy1_down_surface[enemy1_down.down_index],enemy1_down.rect)
			if self.count % 15 == 0:
				enemy1_down.down_index += 1
				if enemy1_down.down_index == 3:
					self.score +=5
					enemy1_down_group.remove(enemy1_down)
					print(self.score)
	@staticmethod
	def game_over():
		pygame.quit
		exit()
	def drawText(self,text,posx,posy,textHeight=48,fontColor=(0,0,0),backgroudColor=(255,255,255)):
		fontObj = pygame.font.SysFont(None, textHeight)  # 通过字体文件获得字体对象
		textSurfaceObj = fontObj.render(text, True,fontColor,backgroudColor)  # 配置要显示的文字
		textRectObj = textSurfaceObj.get_rect()  # 获得要显示的对象的rect
		textRectObj.center = (posx, posy)  # 设置显示对象的坐标
		self.screen.blit(textSurfaceObj, textRectObj)  # 绘制字
if __name__ =="__main__":
	game = PlaneGame()
	game.start_game()

