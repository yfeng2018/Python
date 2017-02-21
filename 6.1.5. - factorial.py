def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

def ask():
    n=int(input('Please input your number...\n'))
    print(factorial(n))

ask()
