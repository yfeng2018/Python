def power(a,b):
    if b==0:
        return 1
    elif b>0:
        return a*power(a,b-1)
    else:
        return ((1.0/a)*(power(a,b+1))

print power(2, -3)
