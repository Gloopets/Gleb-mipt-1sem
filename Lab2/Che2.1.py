import turtle as t
from random import *

t.speed(0)
t.color('red')
t.bgcolor('black')
t.shape('turtle')
t.shapesize(10)
t.screensize(10000, 10000)
for i in range(100000):
    t.forward(randint(0, 30))
    t.left(randint(1, 360))
