import turtle
munir = turtle.Turtle()
hašima = turtle.Turtle()
print(munir)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

square(munir, 200)
square(hašima, 300)
turtle.mainloop()
