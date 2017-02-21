def root(a, x):
    cutoff=0.00001
    while True:
        print(x)
        y=((x+(a/x))/2)
        if abs(y-x)<cutoff:
            break
        x=y

root(100,5)
