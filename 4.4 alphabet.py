import math
import turtle
turtle.setup(1000,1000)
munir = turtle.Turtle()
munir.speed(0)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(1)

def arc(t, r, angle):
    polygon(t, (2*r*math.pi)/360, angle)

def draw_a(t, height):
    a=(height/math.sin(math.radians(70)))
    base=((a*math.sin(math.radians(40)))/(math.sin(math.radians(70))))
    a_prim=((height/math.sin(math.radians(70)))*0.6)
    base_prim=((a_prim*math.sin(math.radians(40)))/(math.sin(math.radians(70))))
    a_bk=((height/math.sin(math.radians(70)))*0.4)
    t.pu()
    t.fd(base)
    t.lt(110)
    t.pd()
    t.fd(a)
    t.lt(140)
    t.fd(a)
    t.pu()
    t.bk(a_bk)
    t.lt(110)
    t.pd()
    t.fd(base_prim)

def draw_b(t, height):
    t.fd(height*0.25)
    arc(t, height*0.3, 180)
    t.fd(height*0.25)
    t.rt(180)
    t.pu()
    t.fd(height*0.18)
    t.pd()
    arc(t, height*0.2, 180)
    t.fd(height*0.18)
    t.lt(90)
    t.fd(height)

def draw_c(t, height):
    arc(t, height/2, 55)
    t.pu()
    arc(t, height/2, 70)
    t.pd()
    arc(t, height/2, 235)

def draw_d(t, height):
    t.fd(height*0.2)
    arc(t, height/2, 180)
    t.fd(height*0.2)
    t.lt(90)
    t.fd(height)

def draw_e(t, height):
    t.fd(height*0.6)
    t.pu()
    t.bk(height*0.6)
    t.lt(90)
    t.pd()
    t.fd(height/2)
    t.rt(90)
    t.fd(height*0.4)
    t.pu()
    t.bk(height*0.4)
    t.lt(90)
    t.pd()
    t.fd(height/2)
    t.rt(90)
    t.fd(height*0.6)

def draw_f(t, height):
    t.lt(90)
    t.fd(height/2)
    t.rt(90)
    t.fd(height*0.4)
    t.pu()
    t.bk(height*0.4)
    t.lt(90)
    t.pd()
    t.fd(height/2)
    t.rt(90)
    t.fd(height*0.6)    

def draw_g(t, height):
    arc(t, height/2, 90)
    t.lt(90)
    t.fd(height*0.3)
    t.pu()
    t.bk(height*0.3)
    t.rt(90)
    arc(t, height/2, 30)
    t.pd()
    arc(t, height/2, 240)

def draw_h(t, height):
    t.lt(90)
    t.fd(height)
    t.pu()
    t.bk(height/2)
    t.rt(90)
    t.pd()
    t.fd(height*0.6)
    t.lt(90)
    t.pu()
    t.fd(height/2)
    t.pd()
    t.bk(height)

def draw_i(t, height):
    t.lt(90)
    t.fd(height)

def draw_j(t, height):
    t.pu()
    t.lt(90)
    t.fd(height*0.3)
    t.rt(180)
    t.pd()
    arc(t, height*0.3, 180)
    t.fd(height*0.7)

def draw_k(t, height):
    t.lt(90)
    t.fd(height)
    t.pu()
    t.bk(height*0.7)
    t.rt(30)
    t.pd()
    t.fd((height*0.7)/(math.sin(math.radians(60))))
    t.pu()
    t.bk((height*0.5)/(math.sin(math.radians(60))))
    t.rt(120)
    t.pd()
    t.fd((height*0.5)/(math.sin(math.radians(60))))
    t.bk(height)
    

draw_k(munir, 100)
