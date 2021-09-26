import turtle as t

t.shape('turtle')
t.speed(0)
p = int(input())
for i in range(p):
    t.circle(i)
    t.left(180)
    t.circle(i)
    t.left(180)
y = int(input())