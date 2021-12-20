import turtle as t
import math

t.shape('turtle')
t.speed(0)
def Chill(n):
    t.penup()
    t.goto(10*n/math.sin(2*math.pi/n), 0)
    t.setheading(0)
    t. pendown()
    t.left(90 + 180/n)
    for i in range(n):
        t.forward(n*10)
        t.left(360/n)
for j in range(3, 13, 1):
    Chill(j)