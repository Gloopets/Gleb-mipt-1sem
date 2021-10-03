import turtle as t
t.shape('arrow')
t.shapesize(0.3)
t.bgcolor('black')
t.pensize(1)
t.screensize(1980, 1440)
t.color('green', 'white')
t.speed(0)

def Shalom(depht):
    if depht == 1:
        t.begin_fill()
        for i in range(3):
            t.forward(5)
            t.left(120)
        t.end_fill()

        t.forward(5)
        t.right(60)

    else:
        for i in range(7):
            Shalom(depht - 1)
            t.penup()
            t.forward(5*(3**(depht-2)))
            t.left(120)
            t.pendown()
        Shalom(depht - 1)
        t.forward(5*(3**(depht-2)))
        t.right(60)

Depht = 5
t.penup()
t.goto(-5*(3**(Depht-2)), -3*(3**(Depht-2)))
Shalom(Depht)
t.hideturtle()
t.exitonclick()