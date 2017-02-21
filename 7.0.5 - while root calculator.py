def root(a, x):
    while True:
        print(x)
        y=((x+(a/x))/2)
        if y==x:
            break
        x=y

root(196,5)
