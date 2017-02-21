import math
import turtle
turtle.setup(1000.1000)
munir = turtle.Turtle()
munir.speed(0)
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

flower(munir, 150, 50, 11)
turtle.done()
