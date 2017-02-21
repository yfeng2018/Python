def root(a, x):
    import math
    while True:
        print(x)
        y=((x+(a/x))/2)
        if y==x:
            break
        x=y
    print('a', (len(str(a))-2)*' ', 'mysqrt(a)          ', 'math.sqrt(a)       ', 'diff')
    print(a, x, (17-(len(str(math.sqrt(a)))))*' ', math.sqrt(a), (18-(len(str(math.sqrt(a)))))*' ', abs(math.sqrt(a)-x))
    
root(10012,5)
