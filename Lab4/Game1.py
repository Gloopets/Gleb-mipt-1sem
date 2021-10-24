import pygame
from pygame.draw import *
from random import randint
pygame.init()
pygame.font.init()

FPS = 50
A = 1200
B = 900
screen = pygame.display.set_mode((A, B))

Matrix = pygame.font.Font(None, 35)
Count = pygame.font.Font(None, 50)
PreText = pygame.font.Font(None, 58)
Doom = pygame.font.Font(None, 100)
Aware = pygame.font.Font(None, 170)

Balls_Number = 30
Rectangles_Number = 10
Time_Restrict = 40
T = Time_Restrict
Objects_Number = Balls_Number + Rectangles_Number
objects = Objects_Number
Score_Restrict = Balls_Number*100 + Rectangles_Number*200
S = Score_Restrict

BOOKOVKI = []
OSKOLKI = []
OBLOMKI = []
SHARIKI = []
XPEHOTA = []

colR = 40
colG = 240
colB = 40

flag = -2
counter = 0
time_counter = 0
pre_counter = 0
DOOM = -9
Losses = 0
Wins = 0
	
def CreateShard(eventpos0, eventpos1, ballcolorRed, ballcolorGreen, ballcolorBlue, ballxspeed, ballyspeed):
	shard = Shard()
	shard.x = randint(eventpos0 - 50, eventpos0 + 50)
	shard.y = randint((eventpos1 - (2500 - (shard.x - eventpos0)**2)**0.5)//1, (eventpos1 + (2500 - (shard.x - eventpos0)**2)**0.5)//1)
	shard.xspeed = (shard.x - eventpos0) / 10 + ballxspeed
	shard.yspeed = (shard.y - eventpos1) / 10 + ballyspeed
	shard.colorRed = ballcolorRed
	shard.colorGreen = ballcolorGreen
	shard.colorBlue = ballcolorBlue
	OSKOLKI.append(shard)
	
def CreateOblomok(eventpos0, eventpos1, xpencolorRed, xpencolorGreen, xpencolorBlue, xpenxspeed, xpenyspeed):
	oblomok = Oblomok()
	oblomok.x = randint(eventpos0 - 50, eventpos0 + 50)
	oblomok.y = randint((eventpos1 - (2500 - (oblomok.x - eventpos0)**2)**0.5)//1, (eventpos1 + (2500 - (oblomok.x - eventpos0)**2)**0.5)//1)
	oblomok.xspeed = (oblomok.x - eventpos0) / 10 + xpenxspeed
	oblomok.yspeed = (oblomok.y - eventpos1) / 10 + xpenyspeed
	oblomok.colorRed = xpencolorRed
	oblomok.colorGreen = xpencolorGreen
	oblomok.colorBlue = xpencolorBlue
	OBLOMKI.append(oblomok)

class Matreeks:
	def __init__(self):
		self.SYM = chr(randint(30,255))
		self.x = randint(0, A)
		self.y = B
		self.xspeed = 0
		self.yspeed = randint(-15, -7)
		self.r = 0
		self.g = 0
		self.b = 0
	def write(self):
		SymShow = Matrix.render(self.SYM, True, (self.r, self.g, self.b))
		screen.blit(SymShow, (self.x, self.y))
		self.x += self.xspeed
		self.y += self.yspeed
		self.SYM = chr(randint(30,255))
		
def CreateLetter(objx, objy, objxspeed, objyspeed, r, g, b):
	letter = Matreeks()
	letter.r = r
	letter.g = g
	letter.b = b
	letter.x = randint(objx//1 - 50, objx//1 + 50)
	letter.y = randint((objy//1 - (2500 - (letter.x - objx//1)**2)**0.5)//1, (objy//1 + (2500 - (letter.x - objx//1)**2)**0.5)//1)
	letter.xspeed = (letter.x - objx) / 20
	letter.yspeed = (letter.y - objy) / 20
	BOOKOVKI.append(letter)

class Shard:
	def __init__(self):
		self.x = 0
		self.xspeed = 0
		self.y = 0
		self.yspeed = 0
		self.r = randint(6,9)
		self.grav = 0.1
		self.colorRed = 0
		self.colorGreen = 0
		self.colorBlue = 0
	def draw(self):
		circle(screen, (self.colorRed, self.colorGreen, self.colorBlue), (self.x, self.y), self.r)
		circle(screen, (0, 0 ,0), (self.x, self.y), self.r - 3)
		self.colorRed += randint(-1, 1)
		if self.colorRed > colR + 5:
			self.colorRed -= 2
		elif self.colorRed < colR - 5:
			self.colorRed += 2
		self.colorGreen += randint(-1, 1)
		if self.colorGreen > colG + 5:
			self.colorGreen -= 2
		elif self.colorGreen < colG - 5:
			self.colorGreen += 2
		self.colorBlue += randint(-1, 1)
		if self.colorBlue > colB + 5:
			self.colorBlue -= 2
		elif self.colorBlue < colB - 5:
			self.colorBlue += 2
	def motion(self):
		self.x += self.xspeed
		self.y += self.yspeed
		self.yspeed += self.grav
	def letterize(self, r, g, b):
		CreateLetter(self.x, self.y, self.xspeed, self.yspeed, r, g, b)
		
class Oblomok:
	def __init__(self):
		self.x = 0
		self.xspeed = 0
		self.y = 0
		self.yspeed = 0
		self.side = randint(11,17)
		self.grav = 0.1
		self.colorRed = 0
		self.colorGreen = 0
		self.colorBlue = 0
	def draw(self):
		rect(screen, (self.colorRed, self.colorGreen, self.colorBlue), (self.x, self.y, self.side, self.side), 0)
		rect(screen, (0, 0, 0), (self.x + 3, self.y + 3, self.side - 6, self.side - 6), 0)
		self.colorRed += randint(-1, 1)
		if self.colorRed > colR + 5:
			self.colorRed -= 2
		elif self.colorRed < colR - 5:
			self.colorRed += 2
		self.colorGreen += randint(-1, 1)
		if self.colorGreen > colG + 5:
			self.colorGreen -= 2
		elif self.colorGreen < colG - 5:
			self.colorGreen += 2
		self.colorBlue += randint(-1, 1)
		if self.colorBlue > colB + 5:
			self.colorBlue -= 2
		elif self.colorBlue < colB - 5:
			self.colorBlue += 2
	def motion(self):
		self.x += self.xspeed
		self.y += self.yspeed
		self.yspeed += self.grav
	def letterize(self, r, g, b):
		CreateLetter(self.x, self.y, self.xspeed, self.yspeed, r, g, b)
		
class Ball:
	def __init__(self):
		self.x = randint(60, A-60)
		self.y = randint(60, B-60)
		self.r = randint(40, 50)
		self.xspeed = randint(-5, 5)
		self.yspeed = randint(-5, 5)
		self.colorRed = randint(0, 255)
		self.colorGreen = randint(0, 255)
		self.colorBlue = randint(0, 255)
		self.life = 2
	def draw(self):
		circle(screen, (self.colorRed, self.colorGreen, self.colorBlue), (self.x, self.y), self.r)
		self.colorRed += randint(-20, 20)
		if self.colorRed > 255:
			self.colorRed -= 40
		elif self.colorRed < 0:
			self.colorRed += 40
		self.colorGreen += randint(-20, 20)
		if self.colorGreen > 255:
			self.colorGreen -= 40
		elif self.colorGreen < 0:
			self.colorGreen += 40
		self.colorBlue += randint(-20, 20)
		if self.colorBlue > 255:
			self.colorBlue -= 40
		elif self.colorBlue < 0:
			self.colorBlue += 40
	def motion(self):
		if self.r < self.x < A-self.r:
			self.x += self.xspeed
		else:
			self.x -= self.xspeed
			self.xspeed = -self.xspeed
		if self.r < self.y < B-self.r:
			self.y += self.yspeed
		else:
			self.y -= self.yspeed
			self.yspeed = -self.yspeed
		self.xspeed += randint(-1,1)/3
		if self.xspeed > 10: self.xspeed -= 5
		self.yspeed -= randint(-1,1)/3
		if self.yspeed > 10: self.yspeed -= 5
	def damage(self):
		self.r /= 2
		self.xspeed *= 2
		self.yspeed *= 2
		self.life -= 1
	def letterize(self, r, g, b):
		if self.life == 2:
			for i in range(70):
				CreateLetter(self.x, self.y, self.xspeed, self.yspeed, r, g, b)
		elif self.life == 1:
			for i in range(50): 
				CreateLetter(self.x, self.y, self.xspeed, self.yspeed, r, g, b)

class XPEHb:
	def __init__(self):
		self.x = randint(0, A-100)
		self.y = randint(0, B - 60)
		self.height = randint(50, 80)
		self.width = randint(50, 80)
		self.xspeed = randint(-5, 5)
		self.yspeed = randint(-5, 5)
		self.colorRed = randint(0, 255)
		self.colorGreen = randint(0, 255)
		self.colorBlue = randint(0, 255)
		self.life = 2
	def draw(self):
		rect(screen, (self.colorRed, self.colorGreen, self.colorBlue), (self.x, self.y, self.width, self.height), 0)
		self.colorRed += randint(-20, 20)
		if self.colorRed > 255:
			self.colorRed -= 40
		elif self.colorRed < 0:
			self.colorRed += 40
		self.colorGreen += randint(-20, 20)
		if self.colorGreen > 255:
			self.colorGreen -= 40
		elif self.colorGreen < 0:
			self.colorGreen += 40
		self.colorBlue += randint(-20, 20)
		if self.colorBlue > 255:
			self.colorBlue -= 40
		elif self.colorBlue < 0:
			self.colorBlue += 40
	def motion(self):
		if 0 < self.x < A-self.width:
			self.x += self.xspeed
		else:
			self.x -= self.xspeed
			self.xspeed = -self.xspeed
		if 0 < self.y < B-self.height:
			self.y += self.yspeed
		else:
			self.y -= self.yspeed
			self.yspeed = -self.yspeed
		self.xspeed += randint(-1,1)/3
		if self.xspeed > 10: self.xspeed -= 5
		self.yspeed -= randint(-1,1)/3
		if self.yspeed > 10: self.yspeed -= 5
	def damage(self):
		self.x += self.width/4
		self.y += self.height/4
		self.width /= 2
		self.height /= 2
		self.xspeed *= 2
		self.yspeed *= 2
		self.life -= 1
	def letterize(self, r, g, b):
		if self.life == 2:
			for i in range(150): 
				CreateLetter(self.x + self.width/2, self.y + self.height/2, self.xspeed, self.yspeed, r, g, b)
		elif self.life == 1:
			for i in range(100): 
				CreateLetter(self.x + self.width/2, self.y + self.height/2, self.xspeed, self.yspeed, r, g, b)
	
def WhiteNoise(objects, r, g, b):
	if objects == -1: 
		pass
	else:
		num = randint((1000/Objects_Number**2*objects**2)//1, (1500/Objects_Number**2*objects**2)//1)
		for i in range (num):
			rect(screen, (r, g, b), (randint(0, A), randint(0, B), randint(1, 3), randint(10, 20)), 0)
		
def DOOM_Noise(Doom, r, g, b):
	num = randint((400*Doom)//1, (500*Doom)//1)
	for i in range (num):
		rect(screen, (r, g, b), (randint(0, A), randint(0, B), randint(1, 3), randint(10, 20)), 0)
		rect(screen, (r, g, b), (randint(0, A), randint(0, B), randint(10, 20), randint(1, 3)), 0)
		
def FillFigures(Balls_Number, Rectangles_Number):
	for i in range(Balls_Number):
		ball = Ball()
		SHARIKI.append(ball)
	for i in range(Rectangles_Number):
		xpen = XPEHb()
		XPEHOTA.append(xpen)
	
def RemoveObjects(colR, colG, colB):
	for ball in SHARIKI:
		ball.letterize(colR, colG, colB)
		SHARIKI.remove(ball)
	for xpen in XPEHOTA:
		xpen.letterize(colR, colG, colB)
		XPEHOTA.remove(xpen)
	for shard in OSKOLKI:
		shard.letterize(colR, colG, colB)
		OSKOLKI.remove(shard)
	for oblomok in OBLOMKI:
		oblomok.letterize(colR, colG, colB)
		OBLOMKI.remove(oblomok)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
	clock.tick(FPS)
#----------------------------------------------------------------------------------------------------------------------------------------------
	if flag == -2:
		Disclaimer = 'If you have epilepsy: play another game'
		DisclaimerShow = PreText.render(Disclaimer, True, (80, 255, 80))
		screen.blit(DisclaimerShow, (200, 320))
		
		Disclaimer2 = 'Else: press any button'
		Disclaimer2Show = PreText.render(Disclaimer2, True, (255, 255, 80))
		screen.blit(Disclaimer2Show, (350, 420))
#----------------------------------------------------------------------------------------------------------------------------------------------
	if flag == -1:
		if Losses <= 3 and Wins == 0:
			colR = 40 + Losses*70
			colG = 240 - Losses*70
			colB = 40
		elif Wins > 0:
			colR = 40
			colG = 240
			colB = 40 + Wins*70
		WhiteNoise(Objects_Number, colR, colG, colB)
		RemoveObjects(colR, colG, colB)
		for bookva in BOOKOVKI:
			BOOKOVKI.remove(bookva) 
		
		rect(screen, (255, 255, 0), (480, 20, 250, 55), 0)
		Menu1 = 'Main menu'
		Menu1Show = PreText.render(Menu1, True, (0, 0, 0))
		screen.blit(Menu1Show, (500, 30))
		
		rect(screen, (0, 0, 0), (430, 200, 340, 150), 0)
		rect(screen, (0, 255, 0), (430, 200, 340, 150), 3)
		Menu2 = 'Easy'
		Menu2Show = Aware.render(Menu2, True, (80, 255, 80))
		screen.blit(Menu2Show, (460, 220))
		
		rect(screen, (0, 0, 0), (430, 400, 340, 150), 0)
		rect(screen, (0, 255, 0), (430, 400, 340, 150), 3)
		Menu3 = 'Hard'
		Menu3Show = Aware.render(Menu3, True, (80, 255, 80))
		screen.blit(Menu3Show, (460, 420))
		
		rect(screen, (0, 0, 0), (360, 600, 480, 150), 0)
		rect(screen, (0, 255, 0), (360, 600, 480, 150), 3)
		Menu4 = 'Custom'
		Menu4Show = Aware.render(Menu4, True, (80, 255, 80))
		screen.blit(Menu4Show, (380, 620))
		
		rect(screen, (0, 0, 0), (800, 20, 130, 55), 0)
		rect(screen, (255, 0, 0), (800, 20, 130, 55), 3)
		Quit = 'Quit'
		QuitShow = PreText.render(Quit, True, (255, 0, 0))
		screen.blit(QuitShow, (820, 30))
		
		rect(screen, (0, 0, 0), (290, 20, 115, 55), 0)
		rect(screen, (0, 255, 255), (290, 20, 115, 55), 3)
		Info = 'Info'
		InfoShow = PreText.render(Info, True, (0, 255, 255))
		screen.blit(InfoShow, (310, 30))
#----------------------------------------------------------------------------------------------------------------------------------------------
	if flag == 0:
		pre_counter += 2
		screen.fill((0, 0, 0))
		
		rect(screen, (255, 255, 255), (800, 20, 130, 55), 3)
		Skip = 'Skip'
		SkipShow = PreText.render(Skip, True, (255, 255, 255))
		screen.blit(SkipShow, (820, 30))
		
		if Losses == 0:
			Preambula1 = 'The Matrix is under threat'
		elif Losses < 3:
			Preambula1 = 'The Matrix is getting infected'
		elif Losses == 3:
			Preambula1 = 'The Matrix is infected'
		Pre1Show = PreText.render(Preambula1, True, (80, 255, 80))
		screen.blit(Pre1Show, (330, 150))
		if pre_counter < 120:
			rect(screen, (0, 0, 0), (330 + pre_counter*5.6, 150, 1000, 70))
			
		Preambula2 = 'Through distortion, the Matrix CODE became visible.'
		Pre2Show = PreText.render(Preambula2, True, (80, 255, 80))
		screen.blit(Pre2Show, (60, 230))
		if pre_counter < 360:
			rect(screen, (0, 0, 0), (60 + (pre_counter-160)*5.6, 230, 2000, 70))
			
		Preambula3 = 'The CODE must be hidden. Interference must be removed.'
		Pre3Show = PreText.render(Preambula3, True, (80, 255, 80))
		screen.blit(Pre3Show, (40, 360))
		if pre_counter <= 600:
			rect(screen, (0, 0, 0), (40 + (pre_counter-400)*4.2, 360, 4000, 70))
			rect(screen, (0, 0, 0), (560, 360, 4000, 70))
		if 600 < pre_counter < 800:
			rect(screen, (0, 0, 0), (560 + (pre_counter-600)*4.2, 360, 4000, 70))
			
		Preambula4 = 'You will be given '+str(Time_Restrict)+' seconds to accomplish the task.'
		Pre4Show = PreText.render(Preambula4, True, (80, 255, 80))
		screen.blit(Pre4Show, (40, 440))
		if pre_counter < 1000:
			rect(screen, (0, 0, 0), (40 + (pre_counter-800)*5.6, 440, 6000, 70))
			
		Preambula5 = '(Press any button to start)'
		Pre5Show = PreText.render(Preambula5, True, (225, 255, 80))
		if pre_counter%100 < 50:
			screen.blit(Pre5Show, (340, 600))
		if pre_counter < 1100:
			rect(screen, (0, 0, 0), (340, 600, 700, 70))
		if pre_counter >= 2100:
			flag = 1
#----------------------------------------------------------------------------------------------------------------------------------------------
	if flag == 1:
		time_counter += 2
#----------------------------------------------------------------------------------------------------------------------------------------------
	if flag == 2:
		if Losses == 3:
			WhiteNoise(Objects_Number, colR, colG, colB)
		else:
			WhiteNoise(objects, colR, colG, colB)
		rect(screen, (0, 0, 0), (400, 200, 400, 150), 0)
		rect(screen, (255, 255, 0), (400, 200, 400, 150), 3)
		Pause = 'Menu'
		PauseShow = Aware.render(Pause, True, (225, 255, 80))
		screen.blit(PauseShow, (440, 220))
		
		rect(screen, (0, 0, 0), (430, 400, 340, 150), 0)
		rect(screen, (255, 0, 0), (430, 400, 340, 150), 3)
		Pause2 = 'Quit'
		Pause2Show = Aware.render(Pause2, True, (255, 80, 80))
		screen.blit(Pause2Show, (470, 420))
#----------------------------------------------------------------------------------------------------------------------------------------------
	if flag == 3:
		WhiteNoise(Objects_Number, colR, colG, colB)
		
		rect(screen, (0, 0, 0), (480, 20, 250, 55), 0)
		rect(screen, (255, 255, 0), (480, 20, 250, 55), 3)
		Menu1 = 'Main menu'
		Menu1Show = PreText.render(Menu1, True, (255, 255, 0))
		screen.blit(Menu1Show, (500, 30))
		
		rect(screen, (0, 255, 255), (290, 20, 115, 55), 0)
		Info = 'Info'
		InfoShow = PreText.render(Info, True, (0, 0, 0))
		screen.blit(InfoShow, (310, 30))
		
		rect(screen, (0, 0, 0), (40, 120, 1120, 740), 0)
		rect(screen, (0, 255, 255), (40, 120, 1120, 740), 3)
		
		
		if Wins == 0 and Losses != 0:
			rect(screen, (255, 255, 255), (800, 20, 270, 55), 0)
			Information = 'STATUS: Losses = '+str(Losses) 
		elif Losses == 0 and Wins != 0:
			rect(screen, (255, 255, 255), (800, 20, 250, 55), 0)
			Information = 'STATUS: Wins = '+str(Wins)
		else: 
			rect(screen, (255, 255, 255), (800, 20, 380, 55), 0)
			Information = 'STATUS: Wins = 0 Losses = 0'
		InformationShow = Matrix.render(Information, True, (0, 0, 0))
		screen.blit(InformationShow, (820, 37))
		
		Information = 'The Manual:'
		InformationShow = Doom.render(Information, True, (40, 240, 250))
		screen.blit(InformationShow, (360, 130))
		
		Information = 'You are in the Main menu. Click with your mouse button'
		InformationShow = PreText.render(Information, True, (40, 240, 250))
		screen.blit(InformationShow, (70, 230))
		
		Information = 'on any game mode. This will start THE LORE part. Also'
		InformationShow = PreText.render(Information, True, (40, 240, 250))
		screen.blit(InformationShow, (60, 280))
		
		Information = 'you can quit the game by clicking on "QUIT" button.'
		InformationShow = PreText.render(Information, True, (40, 240, 250))
		screen.blit(InformationShow, (60, 330))
		
		Information = 'THE LORE part can be skipped completely ("SKIP" but-'
		InformationShow = PreText.render(Information, True, (40, 240, 250))
		screen.blit(InformationShow, (70, 420))
		
		Information = 'ton) or partially (PAB - Press Any Button).'
		InformationShow = PreText.render(Information, True, (40, 240, 250))
		screen.blit(InformationShow, (60, 470))
		
		Information = 'During the game, click on objects with mouse buttons.'
		InformationShow = PreText.render(Information, True, (40, 240, 250))
		screen.blit(InformationShow, (70, 560))
		
		Information = 'Until finished, game can be paused (PAB). From Pause'
		InformationShow = PreText.render(Information, True, (40, 240, 250))
		screen.blit(InformationShow, (60, 610))
		
		Information = 'menu you can either go to Main menu or quit. Going to'
		InformationShow = PreText.render(Information, True, (40, 240, 250))
		screen.blit(InformationShow, (60, 660))
		
		Information = 'Main menu will count as a loss. PAB to continue playing'
		InformationShow = PreText.render(Information, True, (40, 240, 250))
		screen.blit(InformationShow, (60, 710))
		
		Information = 'After you either win or lose, the ENDING starts. You can'
		InformationShow = PreText.render(Information, True, (40, 240, 250))
		screen.blit(InformationShow, (60, 760))
		
		Information = 'PAB to skip it and return to Main menu.'
		InformationShow = PreText.render(Information, True, (40, 240, 250))
		screen.blit(InformationShow, (60, 810))
#----------------------------------------------------------------------------------------------------------------------------------------------	
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if flag == -2:
				flag = -1
			elif flag == 0:
				if pre_counter < 1100:
					pre_counter = (pre_counter//200 + 1)*200
				else:
					flag = 1
			elif flag == 1:
				if objects > -1: 
					flag = 2
				else: 
					DOOM = DeadEnd
			elif flag == 2:
				flag = 1	
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if flag == -2:
				flag = -1
			elif flag == -1:
				if 430 < event.pos[0] < 770 and 200 < event.pos[1] < 350:
					FillFigures(6, 2)
					Time_Restrict = 20
					Score_Restrict = 1000
					Objects_Number = 8
					objects = Objects_Number
					LPD = 3
					WPV = 1
					flag = 0
				elif 430 < event.pos[0] < 770 and 400 < event.pos[1] < 550:
					FillFigures(60, 20)
					Time_Restrict = 70
					Score_Restrict = 10000
					Objects_Number = 80
					objects = Objects_Number
					LPD = 1
					WPV = 3
					flag = 0
				elif 360 < event.pos[0] < 840 and 600 < event.pos[1] < 750:
					FillFigures(Balls_Number, Rectangles_Number)
					Time_Restrict = T
					Score_Restrict = S
					Objects_Number = Balls_Number + Rectangles_Number
					objects = Objects_Number
					LPD = 1
					WPV = 1
					flag = 0
				elif 290 < event.pos[0] < 405 and 20 < event.pos[1] < 75:
					flag = 3
				elif 800 < event.pos[0] < 930 and 20 < event.pos[1] < 75:
					finished = True
			elif flag == 0:
				if 800 < event.pos[0] < 930 and 20 < event.pos[1] < 75:
					flag = 1
			elif flag == 1:
				for ball in SHARIKI:
					if ((event.pos[0] -ball.x)**2 + (event.pos[1] - ball.y)**2)**0.5 < ball.r and ball.life == 2:
						for i in range(50):
							CreateShard(event.pos[0], event.pos[1], ball.colorRed, ball.colorGreen, ball.colorBlue, ball.xspeed, ball.yspeed)
						ball.damage()
					elif ((event.pos[0] -ball.x)**2 + (event.pos[1] - ball.y)**2)**0.5 < ball.r and ball.life == 1:
						objects -= 1
						SHARIKI.remove(ball)
						for i in range(150):
							CreateShard(event.pos[0], event.pos[1], ball.colorRed, ball.colorGreen, ball.colorBlue, ball.xspeed, ball.yspeed)
				for xpen in XPEHOTA:
					if 0 < event.pos[0] - xpen.x < xpen.width and 0 < event.pos[1] -xpen.y < xpen.height and xpen.life == 2:
						for i in range(100):
							CreateOblomok(event.pos[0], event.pos[1], xpen.colorRed, xpen.colorGreen, xpen.colorBlue, xpen.xspeed, xpen.yspeed)
						xpen.damage()
					elif 0 < event.pos[0] - xpen.x < xpen.width and 0 < event.pos[1] -xpen.y < xpen.height and xpen.life == 1:
						objects -=1
						XPEHOTA.remove(xpen)
						for i in range(300):
							CreateOblomok(event.pos[0], event.pos[1], xpen.colorRed, xpen.colorGreen, xpen.colorBlue, xpen.xspeed, xpen.yspeed)
			elif flag == 2:
				if 400 < event.pos[0] < 800 and 200 < event.pos[1] < 350:
					flag = -1
					counter = 0
					time_counter = 0
					pre_counter = 0
					DOOM = -9
					Wins = 0
					Losses += LPD
				elif 430 < event.pos[0] < 770 and 400 < event.pos[1] < 550:
					finished = True
			elif flag == 3:
				if 480 < event.pos[0] < 730 and 20 < event.pos[1] < 75:
					flag = -1
		elif event.type == pygame.QUIT and flag == -2:
			finished = True
#----------------------------------------------------------------------------------------------------------------------------------------------
	if flag == 1:
		if Losses == 3:
			WhiteNoise(Objects_Number, colR, colG, colB)
		else:
			WhiteNoise(objects, colR, colG, colB)
		for bookva in BOOKOVKI:
			bookva.write()
			if bookva.y < 0:
				BOOKOVKI.remove(bookva)
		for ball in SHARIKI:
			ball.motion()
			ball.draw()
		for xpen in XPEHOTA:
			xpen.motion()
			xpen.draw()	
		for shard in OSKOLKI:
			shard.motion()
			shard.draw()
			if shard.y > B:
				OSKOLKI.remove(shard)
				bookva = Matreeks()
				bookva.r = colR
				bookva.g = colG
				bookva.b = colB
				BOOKOVKI.append(bookva)
				counter += 1
		for oblomok in OBLOMKI:
			oblomok.motion()
			oblomok.draw()
			if oblomok.y > B:
				OBLOMKI.remove(oblomok)
				bookva = Matreeks()
				bookva.r = colR
				bookva.g = colG
				bookva.b = colB
				BOOKOVKI.append(bookva)
				counter += 1
		Co = 'Score:'+' '+str(counter)+' / '+str(Score_Restrict)
		Ti = 'Time:'+' '+str(time_counter//1/100)
		if 0 < time_counter < (Time_Restrict - 10)*100 and objects != -1:
			CountShow = Count.render(Co, True, (colR, colG, colB))
			TimeShow = Count.render(Ti, True, (colR, colG, colB))
		elif time_counter%100 < 50 and objects != -1:
			CountShow = Count.render(Co, True, (255 - colR, 255 -colG, 255 - colB))
			TimeShow = Count.render(Ti, True, (255 - colR, 255 -colG, 255 - colB))
		elif time_counter%100 >= 50 and objects != -1:
			CountShow = Count.render(Co, True, (colR, colG, colB))
			TimeShow = Count.render(Ti, True, (colR, colG, colB))
		elif objects == -1 and Victory == 1:
			if Wins <= 3 - WPV:
				CountShow = Count.render(Co, True, (40, 240, 40 + (Wins + WPV)*70))
				TimeShow = Count.render(Ti, True, (40, 240, 40 + (Wins + WPV)*70))
			else:
				CountShow = Count.render(Co, True, (40, 240, 250))
				TimeShow = Count.render(Ti, True, (40, 240, 250))
		elif objects == -1 and Victory == 0:
			if Losses <= 3 - LPD:
				CountShow = Count.render(Co, True, (40 + (Losses + LPD)*70, 240 - (Losses + LPD)*70, 40))
				TimeShow = Count.render(Ti, True, (40 + (Losses + LPD)*70, 240 - (Losses + LPD)*70, 40))
			else:
				CountShow = Count.render(Co, True, (250, 30, 40))
				TimeShow = Count.render(Ti, True, (250, 30, 40))
		screen.blit(CountShow, (12, 9))
		screen.blit(TimeShow, (12, 59))
	pygame.display.update()
	screen.fill((0, 0, 0))
#----------------------------------------------------------------------------------------------------------------------------------------------
	if counter >= Score_Restrict - 1:
		counter = Score_Restrict//1 + Score_Restrict%1
		objects = -1
		RemoveObjects(colR, colG, colB)
		Victory = 1
		Win_Time = time_counter/100
	elif time_counter > Time_Restrict*100 - 1:
		time_counter = Time_Restrict*100
		objects = -1
		Victory = 0
		Score = counter
		RemoveObjects(colR, colG, colB)
	if flag == 1:
		if objects == -1:
			DOOM += 0.02
			time_counter -= 2
			if Victory == 1:
				if -9 < DOOM <= -5.5:
					Warn = 'You win!'+'  '+'Time:'+' '+str(Win_Time)
					if Wins <= 3 - WPV:
						WarnShow = Doom.render(Warn, True, (40, 240, 40 + (Wins + WPV)*70))
					else:
						WarnShow = Doom.render(Warn, True, (40, 240, 250))
					screen.blit(WarnShow, (250, 400))
				elif -5 < DOOM <= -3:
					for bookva in BOOKOVKI:
						BOOKOVKI.remove(bookva)
					if Wins <= 3 - WPV:
						if Wins == 0:
							Warn = 'Matrix Reloads'
						else:
							Warn = 'Matrix Updates'
						WarnShow = Aware.render(Warn, True, (40, 240, 40 + (Wins + WPV)*70))
					else:
						Warn = 'Matrix Updates'
						WarnShow = Aware.render(Warn, True, (40, 240, 250))
					screen.blit(WarnShow, (150, 400))
				elif -3 < DOOM < 5:
					if Wins <= 3 - WPV:
						if Wins == 0:
							Warn = 'Matrix Reloads'
						else:
							Warn = 'Matrix Updates'
						WarnShow = Aware.render(Warn, True, (40, 240, 40 + (Wins + WPV)*70))
					else:
						Warn = 'Matrix Updates'
						WarnShow = Aware.render(Warn, True, (40, 240, 250))
					if randint(0, 2) > 0:
						screen.blit(WarnShow, (150 + randint((3+DOOM)*(-30)//1, (3+DOOM)*30//1), 400 + randint((3+DOOM)*(-20)//1, (3+DOOM)*20//1)))	
				if 5 > DOOM >= 0:
					if Wins <= 3 - WPV:
						DOOM_Noise(DOOM, 40, 240, 40 + (Wins + WPV)*70)
					else:
						DOOM_Noise(DOOM, 40, 240, 250)
				DeadEnd = 5
			if Victory == 0:
				if Losses + LPD >= 3: DeadEnd  = 8
				else: DeadEnd  = 6
				if -9 < DOOM <= -5.5:
					Warn = 'You Lose!'+'  '+'Score:'+' '+str(Score)
					if Losses <= 3 - LPD:
						WarnShow = Doom.render(Warn, True, (40 + (Losses + LPD)*70, 240 - (Losses + LPD)*70, 40))
					else:
						WarnShow = Doom.render(Warn, True, (250, 30, 40))
					screen.blit(WarnShow, (250, 400))
				elif -5 < DOOM <= -3:
					for bookva in BOOKOVKI:
						BOOKOVKI.remove(bookva) 
					Warn = 'Matrix corrupts'
					if Losses <= 3 - LPD:
						WarnShow = Aware.render(Warn, True, (40 + (Losses + LPD)*70, 240 - (Losses + LPD)*70, 40))
					else: 
						WarnShow = Aware.render(Warn, True, (250, 30, 40))
					screen.blit(WarnShow, (150, 400))
				elif -3 < DOOM < 6:
					Warn = 'Matrix corrupts'
					if Losses <= 3 - LPD:
						WarnShow = Aware.render(Warn, True, (40 + (Losses + LPD)*70, 240 - (Losses + LPD)*70, 40))
					else: 
						WarnShow = Aware.render(Warn, True, (250, 30, 40))
					if randint(0, 2) > 0:
						screen.blit(WarnShow, (150 + randint((3+DOOM)*(-30)//1, (3+DOOM)*30//1), 400 + randint((3+DOOM)*(-20)//1, (3+DOOM)*20//1)))	
				if 8 > DOOM >= 0 and Losses <= 3 - LPD:
					DOOM_Noise(DOOM/2, 40 + (Losses + LPD)*70, 240 - (Losses + LPD)*70, 40)
				elif 8 > DOOM >= 0:
					DOOM_Noise(DOOM/2, 250, 30, 40)
				if 8 > DOOM >= 6 and Losses + LPD >= 3:
					Do1 = 'СЛАВА'
					Do2 = 'УКРАИНЕ'
					for i in range (8):
						for j in range (20):
							Do1Show = Doom.render(Do1, True, (40, 160, 220))
							Do2Show = Doom.render(Do2, True, (220, 220, 40))
							screen.blit(Do1Show, (randint(-30,-10) + 600*i, randint(-25,-15) + 52*j))
							screen.blit(Do2Show, (randint(-380,-360) + 600*i, randint(-25,-15) + 52*j))	
			if DOOM >= DeadEnd:
				flag = -1
				counter = 0
				time_counter = 0
				pre_counter = 0
				DOOM = -9
				screen.fill((0, 0, 0))
				objects = Objects_Number
				if DeadEnd == 6 or DeadEnd == 8:
					Losses+= LPD
					Wins = 0
				else: 
					Losses = 0
					Wins += WPV
	if Wins >= 4: Wins = 3
	if Losses >= 4: Losses = 3
pygame.quit()

