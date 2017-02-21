import math
import turtle
turtle.setup(1000,1000)
munir = turtle.Turtle()
munir.speed(0)
def triangle(turtle, length, sides):
    angle_tip=(360/sides)
    angle=(180-(180-angle_tip)/2)
    a=length
    width=math.sqrt(math.fabs((a**2+a**2)-(2*a*a*math.cos(math.radians(angle_tip)))))
    turtle.fd(length)
    turtle.lt(angle)
    turtle.fd(width)
    turtle.lt(angle)
    turtle.fd(length)
    turtle.lt(180)

def trianglezz(turtle, length, sides):
    for i in range(sides):
        triangle(turtle, length, sides)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(1)

def arc(t, r, angle):
    polygon(t, (2*r*math.pi)/360, angle)

def lattice(t, r, size):
    lattice_angle=180-size
    arc(t, r, size)
    t.lt(lattice_angle)
    arc(t, r, size)
    t.lt(lattice_angle)

def flower(t, width, size, x):
    """width represents the width of a lattice.
    size represents the size of a lattice.
    x represents the amount of lattices a flower will have.
    width and size work together so you'll have to experiment.
    """
    for i in range(x):
        lattice(t, width, size)
        t.lt(360/x)

flower(munir, 100, 70, 7)
trianglezz(munir, 20, 100)
turtle.done()
