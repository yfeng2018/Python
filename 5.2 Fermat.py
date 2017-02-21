def check_fermat(a, b, c, n):
    if n>2:
        if (a^n + b^n == c^n):
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn't work.")
    else:
        print("I'm sorry but 'n' is smaller than or equal to 2...")

def input_function():
    a = int(input("Please insert the number 'a'\n"))
    b = int(input("Please insert the number 'b'\n"))
    c = int(input("Please insert the number 'c'\n"))
    n = int(input("Please insert the number 'n'\n"))
    check_fermat(a, b, c, n)

input_function()
    
