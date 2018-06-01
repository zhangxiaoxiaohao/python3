import pygame
from PlanSprite import *
pygame.init()
screen = pygame.display.set_mode((480,700))

bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))

hero = pygame.image.load("./images/hero.gif")
screen.blit(hero,(180,500))

clock = pygame.time.Clock()
hero_rect = pygame.Rect(180,500,200,200)
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png")
enemy1.rect.x = 100
enemy_group = pygame.sprite.Group(enemy,enemy1)
while True:
	clock.tick(60)
	hero_rect.y -=3
	screen.blit(bg,(0,0))
	screen.blit(hero,hero_rect)
	if hero_rect.bottom <= 0:
		hero_rect.y = 700
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	enemy_group.update()
	enemy_group.draw(screen)
	pygame.display.update()

pygame.quit()
