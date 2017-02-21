import turtle
munir = turtle.Turtle()
print(munir)

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

square(munir)
turtle.mainloop()
