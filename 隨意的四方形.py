import turtle as t
def r(f,l,c):
    t.pencolor(c)
    for i in range(4):
        t.speed(0)
        t.fd(f)
        t.rt(l)
for i in range(100):
    r(i*6,120,"pink")

        
    
