import math
import turtle
munir = turtle.Turtle()
def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(1)

def arc(t, r, angle):
    """Draws an arc using turtle graphics.
    r represents radius.
    angle represents the angle that an arc will be drawn.
    If angle is put 360, this function will create a full circle.
    This is a long explanation, but I am actually just trying to
    learn the usage of docstring :)
    """
    polygon(t, (2*r*math.pi)/360, angle)
    
arc(munir, 50, 180)
