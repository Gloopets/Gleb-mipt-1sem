import turtle as t

t.speed(2)
t.color('red')
t.bgcolor('black')
t.shape('circle')
t.screensize(10000, 10000)
t.goto(500, 0)
t.goto(-400, 0)
x = -400
y = 0
Vx = 3
Vy = 20
Ay = -1
for dt in range(500):
    x += Vx
    y += Vy + Ay/2
    Vy += Ay
    if y < 0:
       t.goto(x, 0)
       y = 0
       Vy = -Vy * 0.9
    else:
        t.goto(x,y)
t.exitonclick()