import math
import turtle
munir = turtle.Turtle()
def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t, r):
    polygon(t, (2*r*math.pi)/360, 360) #turtle makes 360 turns, so every turn's length is computed through circumference

def arc(t, r, angle):
    polygon(t, (2*r*math.pi)/360, angle/2.0)
    
arc(munir, 50, 180)
