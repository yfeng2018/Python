import math

def distance(xc, yc, xp, yp):
    radius = math.sqrt(((xp-xc)**2)+(yp-yc)**2)
    return radius

print(distance(2, 2, 4, 4))

def area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    area = ((radius*radius) * math.pi)
    return area

print(area(2, 2, 4, 4))
