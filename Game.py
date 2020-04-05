import pygame,sys
pygame.init()
x=50
y=100
s = pygame.display.set_mode((750,500))
FPS=100
clock=pygame.time.Clock()
BLUE=169, 169, 169
BEX=0, 255, 255
BBLUE=0, 255, 0
PLOTFORM=139, 69, 19

while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				y-=150
			elif event.key == pygame.K_d:
				x+=30
			elif event.key == pygame.K_a:
				x-=30

	s.fill(BLUE)
	if not (y+25 >= 490):
		y+=3
	if not (y-25 >= 400):
		y+=0
	elif not (x+25 <= 500):
		x+=0

		
	

	pygame.draw.rect(s, PLOTFORM,  (500,400,100,25))
	pygame.draw.rect(s, BEX, (x,y,25,25))
	pygame.draw.rect(s, BEX, (x,y,25,25))
	pygame.draw.rect(s, BBLUE, (0,490,750,10))
	pygame.display.update()
	clock.tick(FPS)
		

