import turtle
turtle.setup(800,800)
munir = turtle.Turtle()
munir.speed(0)

def koch_simple(t, length):
    x = length/3
    if length < 10:
        t.fd(x)
        return
    t.lt(60)
    koch_simple(t, x-1)
    t.rt(120)
    koch_simple(t, x-1)
    t.lt(60)
    koch_simple(t, x-1)

def snowflake_simple(t, length):
    for i in range(3):
        koch_simple(t, length)
        t.rt(120)

def koch(t, n):
    """Draws a koch curve with length n."""
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)

koch_simple(munir, 11550)

def snowflake(t, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(3):
        koch(t, n)
        t.rt(120)



turtle.done()
