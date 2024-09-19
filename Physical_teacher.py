import turtle as t
import time

t.ht()
t.up()
t.delay(0)

def teacher():
    teacher_t = t.clone()
    teacher_t.goto(-300,0)
    teacher_t.dot(100,"yellow")
    teacher_t.goto(-330,0)
    teacher_t.dot(30,"white")
    teacher_t.fd(-10)
    teacher_t.dot(20,"black")
    teacher_t.goto(-270,0)
    teacher_t.dot(30,"white")
    teacher_t.fd(10)
    teacher_t.dot(20,"black")
    teacher_t.goto(-300,-100)
    teacher_t.dot(150,"yellow")

def say(word,st):
    s = t.clone()
    s.goto(-250,50)
    s.write(word)
    time.sleep(st)
    s.clear()

def explain(word,x,y):
    e = t.clone()
    e.goto(x,y)
    e.write(word)

def hellow():
    say("Hi :D",2)
    say("I am your teacher.",2)
    say("Are you have any problem?",2)
    say("You can ask me 1.equa speed 2.go down 3.fly on sky",3)
    explain("You can ask me 1.equa speed 2.go down 3.fly on sky",-350,300)
    say("Input 1or2or3 and speed (use ' ' to space out)",3)
    explain("Input 1or2or3 and speed (use ' ' to space out)",-350,270)
    say("If you want next,input any word to contiun",2)
    explain("Input any word to contiun",-350,240)

def eqau(speed):
    eq = t.clone()
    x = -200
    y = 0
    for i in range(1,11):
        eq.goto(x,y)
        eq.dot(20)
        eq.goto(x,y+20)
        eq.write(f"{i} {x},{y}",align="center")
        x += speed
    enter = input()
    eq.clear()
    eq.goto(-200,0)
    eq.dot(20,"white")

def down(speed):
    do = t.clone()
    x = -200
    y = 200
    dosp = 0
    for i in range(1,11):
        do.goto(x,y)
        do.dot(20)
        do.goto(x,y+20)
        do.write(f"{i} {x},{y}",align="center")
        x += speed
        dosp += -10
        y += dosp
    enter = input()
    do.clear()
    do.goto(-200,200)
    do.dot(20,"white")

def on(speed):
    ont = t.clone()
    x = -200
    y = -200
    onsp = 100
    for i in range(1,11):
        ont.goto(x,y)
        ont.dot(20)
        ont.goto(x,y+20)
        ont.write(f"{i} {x},{y}",align="center")
        x += speed
        onsp += -20
        y += onsp
    enter = input()
    ont.clear()
    ont.goto(-200,-200)
    ont.dot(20,"white")

teacher()

hellow()

while True:
    ask,sp = map(int,input("Input:").split())
    if ask == 1:
        eqau(sp)
    elif ask == 2:
        down(sp)
    elif ask == 3:
        on(sp)
    else:
        print("Error")