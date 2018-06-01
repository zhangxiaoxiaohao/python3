import pygame
pygame.init()
screen = pygame.display.set_mode((480,700))

bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))

hero = pygame.image.load("./images/hero.gif")
screen.blit(hero,(180,500))

clock = pygame.time.Clock()
hero_rect = pygame.Rect(180,500,200,200)


while True:
	clock.tick(60)
	hero_rect.y -=10
	screen.blit(bg,(0,0))
	screen.blit(hero,hero_rect)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	pygame.display.update()

pygame.quit()
