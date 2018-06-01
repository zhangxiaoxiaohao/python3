import random
import pygame
SCREEN_RECT = pygame.Rect(0,0,480,700)
FRAME_PER_SEC = 60
CREATE_ENEMY_EVENT =pygame.USEREVENT
CREATE_BULLET_EVENT =pygame.USEREVENT + 1
#爆炸销毁图片

bg1 = pygame.image.load('./images/enemy0_down1.png')

bg2 = pygame.image.load('./images/enemy0_down2.png')

bg3 = pygame.image.load('./images/enemy0_down3.png')

bg4= pygame.image.load('./images/enemy0_down4.png')



#爆炸的精灵组

enemy1_down_group = pygame.sprite.Group()



#把爆炸图片放到列表中

enemy1_down_surface = []

enemy1_down_surface.append(bg1)

enemy1_down_surface.append(bg2)

enemy1_down_surface.append(bg3)

enemy1_down_surface.append(bg4)

class GameSprite(pygame.sprite.Sprite):
	def __init__(self,image_name,speed=1):
		super().__init__()
		
		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()
		self.speed = speed



	def update(self):
		self.rect.y += self.speed

class Background(GameSprite):
	def __init__(self,is_alt=False):
		image_name = "./images/background.png"
		super().__init__(image_name)
		if is_alt:
			self.rect.y = -self.rect.height
	
	def update(self):
		super().update()
		if self.rect.y > SCREEN_RECT.height:
			self.rect.y = -self.rect.height

class Enemy(GameSprite):
	def __init__(self):
		image_name = "./images/enemy-1.gif"
		super().__init__(image_name)
		self.speed = random.randint(1,3)
		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x)
		self.rect.bottom = 0
		self.down_index = 0 #敌机销毁图片索引
	def update(self):
		super().update()
		if self.rect.y >= SCREEN_RECT.height:
			self.kill()
	def __del__(self):
		pass
class Hero(GameSprite):
	def __init__(self):
		image_name = "./images/hero.gif"
		super().__init__(image_name,0)
		self.speed1 = 0
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120
		self.bullet_group = pygame.sprite.Group()
	def update(self):
		self.rect.x +=self.speed
		self.rect.y += self.speed1
		if self.rect.left < 0:
			self.rect.left = 0
		elif self.rect.right > SCREEN_RECT.width:
			self.rect.right =SCREEN_RECT.width
		elif self.rect.bottom > SCREEN_RECT.height:
			self.rect.bottom =  SCREEN_RECT.height
		elif self.rect.y < 0:
			self.rect.y = 0
	
	def fire(self):
		bullet = Bullet()

		bullet.rect.bottom = self.rect.y - 20
		bullet.rect.centerx = self.rect.centerx
		self.bullet_group.add(bullet)
class Bullet(GameSprite):
	def __init__(self):
		image_name = "./images/bullet1.png"
		super().__init__(image_name,-10)
	def update(self):
		super().update()
		if self.rect.bottom < 0:
			self.kill()










