import turtle
munir = turtle.Turtle()
def triangle(length):
    for i in range(3):
        munir.fd(length)
        munir.lt(120)
    munir.lt(60)

def trianglezz(length):
    for i in range(6):
        triangle(length)

trianglezz(30)
