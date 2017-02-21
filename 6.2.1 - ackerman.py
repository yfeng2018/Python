def ackerman(m, n):
    if m==0:
        result=n+1
        return result
    elif m>0 and n==0:
        result=ackerman(m-1, 1)
        return result
    elif m>0 and n>0:
        result=ackerman(m-1, ackerman(m, n-1))
        return result
    else:
        resut=('I\'m sorry but those number aren\'t supported...')
        return result

def ask():
    m=int(input('Please enter the first number\n'))
    n=int(input('Please enter the second number\n'))
    print(ackerman(m, n))

ask()
