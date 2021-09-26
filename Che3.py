import turtle as t

t.shape('turtle')
t.speed(0)
for i in range(1, 10, 1):
    t.penup()
    t.goto(-10*i, -10*i)
    t.pendown()
    for j in range(4):
        t.forward(20*i)
        t.left(90)