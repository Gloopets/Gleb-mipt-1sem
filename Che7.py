import turtle as t

t.shape('turtle')
t.speed(0)
k = 0.36
for i in range (0, 1800, 1):
    t.forward(k)
    t.left(2)
    k = k + 0.002