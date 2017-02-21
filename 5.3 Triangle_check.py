def is_triangle(a, b, c):
        if a+b>c:
            if a+c>b:
                if b+c>a:
                    print("yes")
                else:
                    print("no")
            else:
                print("no")
        else:
            print("no")

def input_function():
    a = int(input("Please insert the number 'a'\n"))
    b = int(input("Please insert the number 'b'\n"))
    c = int(input("Please insert the number 'c'\n"))
    is_triangle(a, b, c)

input_function()
