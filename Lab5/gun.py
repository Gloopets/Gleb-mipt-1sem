import math
import pygame
from pygame.draw import *
from random import randint
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
balls = []
targets = []

FPS = 30

Red = 190
Green = 30
Blue = 30

WIDTH = 800
HEIGHT = 600

def ColGrad (Red, Green, Blue):
	Red += randint(-10, 10)
	if 0 > Red:
		Red += 20
	elif 255 < Red:
		Red -= 20
	Green += randint(-10, 10)
	if 0 > Green:
		Green += 20
	elif 255 < Green:
		Green -= 20
	Blue += randint(-10, 10)
	if 0 > Blue:
		Blue += 20
	elif 255 < Blue:
		Blue -= 20

class Ball:
    def __init__(self):
    	self.surf = screen
        self.x = 40
        self.y = 450
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.grav = 1
        self.color = (Red, Green, Blue)
        self.live = 30

    def draw_move(self):
		pygame.draw.circle(self.surf, self.color, (self.x, self.y), self.r)
        self.x += self.vx
        self.y -= self.vy
        self.vy -= self.grav
        if self.x > WIDTH or self.x < 0:
			self.vx = -self.vx
		if self.y > HEIGHT - 30:
			self.vy = -self.vy/2
			self.vx = -self.vx/2
			self.y = HEIGHT - 30
			if self.vy < 3:
				self.vy = 0
				self.vx = 0
				self.live -=1

    def hittest(self, obj):
        if (self.x - obj.x)**2 + (self.y - obj.y)**2 < (self.r + obj.r)**2:
			return True
       else:
            return False

class Gun:
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = (120, 120, 120)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        global balls
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = (255, 0, 0)
        else:
            self.color = (120, 120, 120)

    def draw(self):
		polygon(screen, ())

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 3
            self.color = (255, 0, 0)
        else:
            self.color = (120, 120, 120)

class Target(Ball):
    def hit(self, points=1):
        self.points += points
        self.points = 0

    def draw(self):
        circle(screen, self.color, x, y, r)

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target()
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.draw_move()
        if b.hittest(target) and target.score != 0:
            target.score = 0
            targets.remove(target)
            target.new_target()
    gun.power_up()

pygame.quit()
