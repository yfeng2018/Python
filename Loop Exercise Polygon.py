import turtle
munir = turtle.Turtle()

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

polygon(munir, 100, 20)
