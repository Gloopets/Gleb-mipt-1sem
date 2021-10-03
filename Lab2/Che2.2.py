import turtle as t

N0 = [0, 0, 50, 0, 0, -100, -50, 0, 0, 100, 0, 0]
N1 = [0, -50, 50, 50, 0, -100, -50, 100]
N2 = [0, 0, 50, 0, 0, -50, -50, -50, 50, 0, -50, 100]
N3 = [0, 0, 50, 0, -50, -50, 50, 0, -50, -50, 0, 100]
N4 = [0, 0, 0, -50, 50, 0, 0, -50, 0, 100, -50, 0]
N5 = [0, -100, 50, 0, 0, 50, -50, 0, 0, 50, 50, 0, -50, 0]
N6 = [50, 0, -50, -50, 0, -50, 50, 0, 0, 50, -50, 0, 0, 50]
N7 = [0, -100, 0, 50, 50, 50, -50, 0, 0, 0]
N8 = [0, 0, 50, 0, 0, -100, -50, 0, 0, 50, 50, 0,-50, 0, 0, 50, 0, 0]
N9 = [0, -100, 50, 50, 0, 50, -50, 0, 0, -50, 50, 0, -50, 50]

NA = [N0, N1, N2, N3, N4, N5, N6, N7, N8, N9]

t.shape('turtle')
t.speed(6)
t.color('green')
t.bgcolor('black')
t.pensize(3)
A = input().split()
for i in range(len(A)):
    A[i] = int(A[i])

t.penup()
x = -300
y = 50
for i in range(len(A)):
    B = NA[A[i]]
    x += B[0]
    y += B[1]
    t.goto(x, y)
    t.pendown()
    for j in range(2, len(B) - 3, 2):
        x += B[j]
        y += B[j + 1]
        t.goto(x, y)
    t.penup()
    x += B[len(B) - 2]
    y += B[len(B) - 1]
    t.goto(x, y)
    x += 100
    t.forward(100)

t.exitonclick()
