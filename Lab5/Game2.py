import math as m 
import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
WIDTH = 1500
HEIGHT = 1000

PreText = pygame.font.Font(None, 58)
EndText = pygame.font.Font(None, 240)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
balls = []
targets = []

def ColGrad(Red, Green, Blue):
	Red += randint(-3, 3)
	if Red > 255:
		Red -= 6
	if Red < 0:
		Red += 6
	Green += randint(-3, 3)
	if Green > 255:
		Green -= 6
	if Green < 0:
		Green += 6
	Blue += randint(-3, 3)
	if Blue > 255:
		Blue -= 6
	if Blue < 0:
		Blue += 6

class Ball():
	def __init__(self):
		self.x = 120
		self.y = 950
		self.r = 10
		self.vx = 10
		self.vy = 10
		self.gr = 1.5
		self.color = (180, 240, 40)
		self.live = 30

	def motion(self):
		if self.x > WIDTH - self.r:
			self.vx = -self.vx
			self.x = WIDTH - 1 - self.r
		if self.y >= HEIGHT - self.r:
			self.vy = int(-self.vy / 2.5) 
			self.vx = int(self.vx / 2.5)
			self.y = HEIGHT - 1 - self.r
		if self.x < self.r:
			self.vx = - self.vx
			self.x = self.r + 1
		if self.y < self.r:
			self.vy = -self.vy
			self.y = self.r + 1
		if abs(self.vy) < 2 and self.y >= HEIGHT - 5 - self.r:
			self.vx = 0
			self.vy = 0
			self.gr = 0
			if self.r > 0:
				self.r -= 1
				self.y += 1
			self.live -= 1
		self.x += self.vx
		self.y -= self.vy
		self.vy -= self.gr
		circle(screen, self.color, (self.x, self.y), self.r)

	def hit_test(self, obj):
		if m.sqrt((self.x - obj.x)**2 + (self.y - obj.y)**2) < self.r + obj.r:
			return True
		else:
			return False

class Gun():
	def __init__(self):
		self.f2_power = 80
		self.f2_on = 0
		self.an = 1
		self.x = 120
		self.color = (255, 0, 0)
		self.critstate = 0
		self.polus = 1

	def fire2_start(self):
		self.f2_on = 1

	def fire2_end(self):
		global balls, bullet
		bullet += 1
		ball = Ball()
		ball.x = self.x
		ball.vx = self.f2_power * m.cos(self.an) * 0.6 * self.polus
		ball.vy = - self.f2_power * m.sin(self.an) * 0.6
		ball.r = 30 - int(self.f2_power*0.1)
		balls.append(ball)
		self.an = 1
		self.f2_on = 0
		self.f2_power = 80
		if self.critstate < 100:
			self.critstate = 0

	def draw(self):
		self.color = (180, 240, 40)
		if self.f2_power >= 180:
			if self.critstate % 20 < 10:
				self.color = (255, 0, 0)
			self.critstate += 1
		if self.polus == 1:
			polygon(screen, self.color, [(self.x + 10, 950), (self.x + 10 + int(self.f2_power*m.cos(self.an)), 950 + int(self.f2_power*m.sin(self.an))), 
			(self.x + 10 + int(self.f2_power*m.cos(self.an)) + 20*m.sin(self.an), 950 + int(self.f2_power*m.sin(self.an)) - 20*m.cos(self.an)),
			(self.x + 10 + 20*m.sin(self.an), 950 - 20*m.cos(self.an))], 0)
		else:
			polygon(screen, self.color, [(self.x + 10, 950), (self.x + 10 - int(self.f2_power*m.cos(self.an)), 950 + int(self.f2_power*m.sin(self.an))), 
			(self.x + 10 - int(self.f2_power*m.cos(self.an)) + 20*m.sin(self.an), 950 + int(self.f2_power*m.sin(self.an)) + 20*m.cos(self.an)),
			(self.x + 10 + 20*m.sin(self.an), 950 + 20*m.cos(self.an))], 0)
		polygon(screen, self.color, [(self.x - 80, 940), (self.x - 35, 940), (self.x - 15, 910), (self.x + 15, 910), (self.x + 35, 940), 
		(self.x + 80, 940), (self.x + 100, 950), (self.x + 100, 965), (self.x + 95, 975), (self.x - 95, 975), (self.x - 100, 965)], 0)

		for i in range(6):
			rect(screen, (0, 0, 0), (self.x - 55 + 20*i, 950, 10, 10), 0)
			circle(screen, self.color, (self.x - 75 + 30*i, 985), 15)
			circle(screen, (0, 0, 0), (self.x - 75 + 30*i, 985), 11)

	def targetting(self, event=0):
		if event and event.pos[0] > self.x:
			self.an = m.atan((event.pos[1] - 950) / (event.pos[0] - self.x))
			self.polus = 1
		elif event and event.pos[0] < self.x:
			self.an = -m.atan((event.pos[1] - 950) / (event.pos[0] - self.x))
			self.polus = -1
		elif event:
			self.an = 90
		
	def power_up(self):
		if self.f2_on:
			if self.f2_power < 180:
				self.f2_power += 2
				self.color = (180, 240, 40)
				
	def animate(self):
		for i in range(100):
			ball = Ball()
			ball.color = (255, 0, 0)
			ball.x = self.x
			ball.y = 950
			ball.r = 10
			if randint(0, 1) == 0:
				ball.vx = randint(40, 50)
			else:
				ball.vx = randint(-50, -40)
			ball.vy = randint(5, 15)
			ball.gr = -1
			balls.append(ball)

class Target():
	def __init__(self):
		self.points = randint(0, 100)
		self.vy = randint(- 7, 7)
		self.vx = randint(- 7, 7)
		self.r = randint(20, 40)
		self.y = randint(200, HEIGHT - 200)
		self.x = randint(WIDTH/2, WIDTH - self.r)
		self.red = randint(0, 255)
		self.green = randint(0, 255)
		self.blue = randint(0, 255)

	def motion(self):
		if self.r < self.x < WIDTH - self.r:
			self.x += self.vx
		else:
			self.x -= self.vx
			self.vx = -self.vx
		if self.r < self.y < HEIGHT - self.r:
			self.y += self.vy
		else:
			self.y -= self.vy
			self.vy = -self.vy
		self.vx += randint(-1,1)
		if self.vx > 10: 
			self.vx -= 5
		self.vy -= randint(-1,1)
		if self.vy > 10: 
			self.vy -= 5
		ColGrad(self.red, self.green, self.blue)
		circle(screen, (self.red, self.green, self.blue), (self.x, self.y), self.r)
	

for i in range(10):
	target = Target()
	targets.append(target)
gun = Gun()
bullet = 0
counter = 0
time_counter = 0
flag = 1
clock = pygame.time.Clock()
finished = False
roll = 0

while not finished:
	clock.tick(FPS)
	time_counter += 1/FPS
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			gun.fire2_start()
		elif event.type == pygame.MOUSEBUTTONUP:
			gun.fire2_end()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				roll = 1
			elif event.key == pygame.K_LEFT:
				roll = -1
		elif event.type == pygame.KEYUP:
			roll = 0
		elif event.type == pygame.MOUSEMOTION:
			gun.targetting(event)
	screen.fill((85, 107, 47))
	if flag == 1:
		gun.x += roll*10
		if gun.critstate <= 50:
			gun.draw()
		for target in targets:
			target.motion()
		for ball in balls:
			ball.motion()
			for target in targets:
				if ball.hit_test(target):
					target.score = 0
					targets.remove(target)
					counter += 5
			if ball.live == 0:
				balls.remove(ball)
		Co = 'Score:'+' '+str(counter)
		Ti = 'Time:'+' '+str(int(time_counter*100)/100)
		CountShow = PreText.render(Co, True, (205, 227, 167))
		TimeShow = PreText.render(Ti, True, (205, 227, 167))
		screen.blit(CountShow, (12, 9))
		screen.blit(TimeShow, (12, 69))
		if gun.critstate == 50:
			gun.animate()
			counter = -10000
		if gun.critstate > 90:
			flag = 2
		if counter > 50 and time_counter < 20:
			flag = 3
		elif time_counter >= 20:
			flag = 2
	if flag == 2:
		SMERT = 'TbI YMEP'
		LastShow = EndText.render(SMERT, True, (255, 0, 0))
		screen.blit(LastShow, (300, 450))
	if flag == 3:
		SMERT = 'MOLODETS'
		LastShow = EndText.render(SMERT, True, (255, 0, 0))
		screen.blit(LastShow, (300, 450))
	pygame.display.update()
	
	if gun.f2_on == 1:
		gun.power_up()

pygame.quit()

