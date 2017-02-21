def is_power(a,b):
    x=a/b
    if x==1:
        return True
    
    if a%b==0:
        return is_power(x,b)
    
    else:
        return False
    

def is_power2(a,b):
    if a == 1:
        return True

    if a%b != 0:
        return False

    return is_power2(a/b, b)

print(is_power(83521, 17))
