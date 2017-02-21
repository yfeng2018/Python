import math

def is_between(x,y,z):
    return x<=y<=z

def is_between_check(x,y,z):
    if is_between(x,y,z):
        print(y, 'is between', x, 'and', z)
    else:
        print(y, 'isn\'t between', x, 'and', z)
    return
    

print(is_between_check(5,4,5))
