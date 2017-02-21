import math
import turtle
turtle.setup(1000,1000)
munir = turtle.Turtle()
munir.speed(0)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(1)
        length=length+0.001

def spiral(t, r, angle):
    """r represents the starting radius of the spiral.
    angle represents the length of the spiral in degrees.
    """
    polygon(t, ((2*r*math.pi)/360), angle)
    
spiral(munir, 15, 36000)
turtle.exitonclick()
