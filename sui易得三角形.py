import turtle as t
def d(a,l,c):
    t.pencolor(c)
    for i in range(4):
        t.fd(a)
        t.rt(l)
        t.speed(0)
    if a<600:
        d(a+1,120,"pink")
d(1,120,"pink")
