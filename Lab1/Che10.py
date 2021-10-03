import turtle as t

t.shape('turtle')
t.speed(0)
p = int(input())
for i in range(p):
    t.circle(100)
    t.left(360/p)
y = int(input())