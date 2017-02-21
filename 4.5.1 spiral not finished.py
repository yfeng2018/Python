import math
import turtle
turtle.setup(1000,1000)
munir = turtle.Turtle()
munir.speed(0)

def spiral(t, r, angle, width):
    """r represents the half radius of a circle/spiral.
    angle represents the angle of spiral that will be drawn.
    (angle needs to be more than 360 to start the spiral drawing)
    width represents the width between the spiral lines.
    (recommended with=between 0.1 and 0.01)
    """
    for i in range(angle):
        t.fd((2*r*math.pi)/360)
        t.lt(1)
        r=r+width


def dotted_spiral(t, r, angle, width):
    #produces dotted spiral
    for i in range(angle):
        t.pd()
        t.fd((2*r*math.pi)/360)
        t.lt(1)
        r=r+width
        t.pu()
        t.fd((2*r*math.pi)/360)
        t.lt(1)
        r=r+width

spiral(munir, 10, 36000, 0.03)

turtle.exitonclick()
