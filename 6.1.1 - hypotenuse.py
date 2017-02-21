def hypotenuse(a, b):
    import math
    a_squared = a**2
    b_squared = b**2
    c = math.sqrt(a_squared + b_squared)
    return c

print(hypotenuse(6, 18))
