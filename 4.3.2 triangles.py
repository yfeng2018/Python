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

trianglezz(munir, 100, 7)
turtle.done()
