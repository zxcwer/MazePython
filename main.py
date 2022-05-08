import pygame, sys
from settings import *
x1 = 5
y1 =415
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))

bg = pygame.image.load("back-bg.jpeg")
bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))

#draw 3 rectangles for maze route
path = [((0,400),(200,30)),((200,400),(30,200)),((200,600),(300,30)),((500,200),(30,430)),((500,200),(100,30)),((600,100),(30,130))]
run = True

clock = pygame.time.Clock()
while run:
	for event in pygame.event.get():
		if event.type ==pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	if (x1-615)**2+(y1-130)**2<=100:
		print("you won")


	screen.blit(bg,(0,0))
	for x in path:
		pygame.draw.rect(screen,(255,255,255),x)

	keys = pygame.key.get_pressed()
	'''if any(b[0][0]<x1<b[1][0]+b[0][0] and b[0][1]<y1<b[1][1]+b[1][0] for b in path):
		print(x1,y1)
	'''	
	if keys[pygame.K_UP]:
		y1 -= 1
	elif keys[pygame.K_DOWN]:
		y1 += 1

	if keys[pygame.K_LEFT]:
		x1 -= 1
	elif keys[pygame.K_RIGHT]:
		x1 += 1

	pygame.draw.rect(screen,(0,0,0),(x1,y1,5,5))
	pygame.draw.circle(screen,(255,0,0),(615,130),10)
	pygame.display.update()
