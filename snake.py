import pygame
import random

N = 20
M = 20
size = 48
width = size * N
height = size * M
cherryPositionX = random.randint(0, 20)
cherryPositionY = random.randint(0, 20)
score = 0
timeDelay = 100

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

screen = pygame.Surface((width, height))
screen.fill((0, 0, 0))

# backGroung = pygame.image.load('images/fon.png')
# snakeHead = pygame.image.load('images/snakeHead.png')
# cherryImage = pygame.image.load('images/FRUKT.png')
# bodySnake = pygame.image.load('images/bodySnake.png')


squarePositionX = 0
squarePositionY = 48
square = pygame.Surface((48, 48))
square.fill((69, 255, 236))

done = True
while done:
	#отлеживаем события
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			done = False
	squarePositionX += size
	#отрисовка
	window.blit(screen,(0,0))
	window.blit(square,(squarePositionX,squarePositionY))
	pygame.display.flip()
	pygame.time.delay(timeDelay)