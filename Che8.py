import turtle as t

t.shape('turtle')
t.speed(0)
n = 5
for i in range(100):
    t.forward(n)
    t.left(90)
    t.forward(n)
    t.left(90)
    n = n + 5