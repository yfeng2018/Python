import math
import turtle
turtle.setup(800, 800)
munir = turtle.Turtle()
munir.speed(500)

def center(t, x):
    t.pu()
    t.bk(x/2)
    t.lt(90)
    t.fd(math.sin(math.radians(60))*x/2)
    t.rt(90)
    t.pd()

def koch(t, x):
    if x<15:#change this number in order to get koch of different resolution
        t.fd(x)
        return
    s=x/3
    koch(t, s)
    t.lt(60)
    koch(t, s)
    t.rt(120)
    koch(t, s)
    t.lt(60)
    koch(t, s)

def snowflake(t, x):
    center(t, x)
    for i in range(3):
        koch(t, x)
        t.rt(120)

snowflake(munir, 500)
