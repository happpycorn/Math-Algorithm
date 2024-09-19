import turtle as t
import math as m
import random as r

t.screensize(700,700)
t.tracer(False)
t.ht()
t.up()

v = 100
angle = 0
canvas = t.getcanvas()
x = canvas.winfo_pointerx()-720
y = (canvas.winfo_pointery()-450)*-1


hehe = t.clone()
hehe.st()
hehe.goto(-200,-200)
t.update()

def see():
    s = t.clone()
    s.goto(-200,-200)
    for i in range(0,int(v/3)):
        x = v*m.cos(angle*3.1/180)*i-200
        y = v*m.sin(angle*3.1/180)*i-0.5*9.8*i*i-200
        s.goto(x,y)
        s.dot(10)
    t.update()
    s.clear()

def fly():
    pass

def enemycreat():
    global enemy,ex,ey
    enemy = t.clone()
    ex = r.randrange(-100,200)
    ey = r.randrange(-100,200)
    enemy.goto(ex,ey)

while True:
    t.tracer(False)
    x = canvas.winfo_pointerx()-720
    y = (canvas.winfo_pointery()-450)*-1
    xl = abs(x+200)
    yl = abs(y+200)
    if xl != 0:
        angle = m.degrees(m.atan(yl/xl))
    hehe.setheading(angle)
    see()