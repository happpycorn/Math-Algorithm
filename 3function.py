import turtle as t

t.delay(0)
t.speed(0)
t.up()

for i in range(-100,100):
    a = (i/10)**3 - 5*i
    t.goto(i,a)
    t.dot(10)

a = input()