import pygame
import random

N = 20
M = 20
size = 48
width = size * N
height = size * M

score = 0
timeDelay = 300
moveDirection = ""
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

screen = pygame.Surface((width, height))
screen.fill((0, 0, 0))

# backGroung = pygame.image.load('images/fon.png')
# snakeHead = pygame.image.load('images/snakeHead.png')
# cherryImage = pygame.image.load('images/FRUKT.png')
# bodySnake = pygame.image.load('images/bodySnake.png')

square = pygame.Surface((size, size))
square.fill((69, 255, 236))
squarePositionX = random.randint(2, N - 2) * size
squarePositionY = random.randint(2, M - 2) * size

cherry = pygame.Surface((size, size))
cherry.fill((255, 0, 230))
cherryPositionX = random.randint(2, N - 2) * size
cherryPositionY = random.randint(2, M - 2) * size

bodyPosition = []

done = True

while done:
	#отлеживаем события
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			done = False
		# События нажатий клавиш
		elif e.type == pygame.KEYDOWN:
			if e.key == pygame.K_a and moveDirection != "RIGHT":
				moveDirection = "LEFT"
			elif e.key == pygame.K_d and moveDirection != "LEFT":
				moveDirection = "RIGHT"
			elif e.key == pygame.K_w and moveDirection != "DOWN":
				moveDirection = "UP"
			elif e.key == pygame.K_s and moveDirection != "UP":
				moveDirection = "DOWN"
	# Реализация движения
	if moveDirection == "LEFT":
		squarePositionX -= size
	elif moveDirection == "RIGHT":
		squarePositionX += size
	elif moveDirection == "UP":
		squarePositionY -= size
	elif moveDirection == "DOWN":
		squarePositionY += size


	# Если координаты головы змейки и фрутка совпадают, то фрукт "съедается"
	if cherryPositionY == squarePositionY and cherryPositionX == squarePositionX:
		score += 1
		cherryPositionX = random.randint(2, N - 2) * size
		cherryPositionY = random.randint(2, M - 2) * size


	# Проверка на окончание игры
	if squarePositionX > width or squarePositionX < 0:
		done = False
	elif squarePositionY > height or squarePositionY < 0:
		done = False

	#отрисовка
	window.blit(screen,(0,0)) # Отрисовка экрана
	for i in range(len(bodyPosition)): #Отрисовка туловища змеи
		if score != 0:
			window.blit(square, (bodyPosition[-1 - i]))
		if (squarePositionX, squarePositionY) == bodyPosition[-1 - i] and score >= 1:
			done = False
	window.blit(cherry,(cherryPositionX, cherryPositionY)) # Отрисовка фрукта
	window.blit(square,(squarePositionX, squarePositionY)) # Отрисовка головы

	# Отслеживание координат тела змейки
	if score >= 1:
		bodyPosition.append((squarePositionX, squarePositionY))
		bodyPosition = bodyPosition[-score:]

	#Обновление экрана и задержка(fps)
	pygame.display.flip()
	pygame.time.delay(timeDelay)