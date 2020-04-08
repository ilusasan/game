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

class Player:
	def __init__(self, platform, color=BEX):
		self.color = color
		self.x = 100
		self.y = 450
		self.speed = 4
		self.w = 25
		self.h = 25
		self.jumpHeight = 200
		self.state = "stop"
		self.platform = platform
		self.jump = False
		self.tempjh = self.y + self.jumpHeight

	def collision(self,object):
		for o in object:
			if self.y + self.h >= o.y:
				col = (True,"down")
			elif self.y <= o.y + o.h:
				col = (True,"up")
			elif self.x + self.w >= o.x:
				col = ( True,"right")
			elif self.x <= o.x + o.w:
				col = (True,"left")
			else:
				col = (False,"")
			if col[0] == True:
				break
		return col



	def  move(self):
		if (self.state == "left" 
		and not(self.collision(self.platform)[1] == "left")):
			self.x -= self.speed
		elif (self.state == "right"
			and not(self.collision(self.platform)[1] == "right")):
			self.x += self.speed
		if (self.collision(self.platform)[1] == "down"):
			self.tempjh = self.y + self.jumpHeight
			
		else :
			self.y += 3
		if (self.jump == True):
			if self.y <= self.tempjh:
				self.y -= 6
			else:
				self.jump = False

	def draw(self):
		self.move()
		pygame.draw.rect(s, self.color, (self.x, self.y, self.w, self.h))

class Platform:
	def __init__(self,x,y,w,h,color):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.color = color

	def draw(self):
		pygame.draw.rect(s, self.color, (self.x, self.y, self.w, self.h))



gr = Platform(0,490,750,10,PLOTFORM)
gr1 = Platform(400,250,200,100,(255, 255, 255))
pl = Player(platform = [gr,gr1])
while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				pl.jump = True
			elif event.key == pygame.K_d:
				pl.state = "right"
			elif event.key == pygame.K_a:
				pl.state = "left"
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a or event.key == pygame.K_d:
				pl.state = "stop"
			elif event.key == pygame.K_w:
				pl.jump = False 


	s.fill(BLUE)
	gr.draw()
	gr1.draw()
	pl.draw()
	pygame.display.update()
	clock.tick(FPS)
		

