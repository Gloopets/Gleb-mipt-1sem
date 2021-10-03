import turtle as t

def star(rays):
    for i in range(rays):
        t.forward(100)
        t.right(180 - 180/rays)
star(15)
t.penup()
t.goto(200, 0)
t.pendown()
star(21)
