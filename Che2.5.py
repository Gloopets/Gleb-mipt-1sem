import turtle as t
import math
from random import *

t.speed(0)
t.shape('square')
t.penup()
t.goto(-200, -200)
t.pendown()
for i in range(4):
    t.forward(400)
    t.left(90)
t.hideturtle()

pool = [t.Turtle(shape='circle') for i in range(10)]
for unit in pool:
    unit.penup()
    unit.speed(10)
    unit.left(randint(1, 360))
    unit.goto(randint(-200, 200), randint(-200, 200))

while True:
    for unit in pool:
        if -200 < unit.xcor() < 200 and -200 < unit.ycor() < 200:
            unit.forward(2)
        elif unit.xcor() >= 200:
            unit.left(180 - 2*unit.heading())
            unit.forward(2)
        elif unit.ycor() >= 200:
            unit.left(180 - 2*(unit.heading()-90))
            unit.forward(2)
        elif unit.xcor() <= -200:
            unit.left(180 - 2*(unit.heading()-180))
            unit.forward(2)
        elif unit.ycor() <= -200:
            unit.left(180 - 2*(unit.heading()-270))
            unit.forward(2)

