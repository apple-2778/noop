import turtle as t
import random
t.speed(0)
t.color("orange")
def d(r):
    if r<5:
        return
    if 1<=r<=30:
        if random.randint(0,2)==0:
            t.color("white")
        else:
            t.color("green")
            t.pensize(r/3)
    elif r<20:
        if random.randint(0,1)==0:
                t.color("blue")
        else:
            t.color("yellow")
            t.pensize(r/3)
    else:
        t.color("black")
        t.pensize(r/10)
            
    t.fd(r)
    a=1.5*random.random()
    b=1.5*random.random()    
    t.rt(20*a)
    d(r-10*b)
    t.lt(40*a)
    d(r-10*b)
    t.rt(20*a)
    t.bk(r)
t.lt(90)
t.bk(300)
d(78)
    
