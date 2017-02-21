def compare(x, y):
    if x>y:
        return 1
    elif x==y:
        return 0
    else:
        return -1

x = int(input("Please input the number x...\n"))
y = int(input("Please input the number y...\n"))

print(compare(x, y))
