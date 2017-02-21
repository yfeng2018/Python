def gcd(a,b):
    if b==0:
        return a
    elif a%b==0:
        return b
    else:
        gcd(b,a%b)
        print(a%b)
        
print(gcd(48,18))
