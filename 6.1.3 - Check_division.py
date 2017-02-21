def answer():
    answer = input("Do you want to check another pair of numbers?\nAnswer with 'yes' or 'no'\n")
    if answer == "yes":
        x = int(input("Please input the number x\n"))
        y = int(input("Please input the number y\n"))
        check_division(x, y)
    elif answer == "no":
        print("Okay, thank you for using my program:)")
        return

def check_division(x, y):
    if x%y == 0:
        print ("They are divisible")
        answer()
    else:
        print("They are not divisible...")
        answer()

x = int(input("Please input the number x\n"))
y = int(input("Please input the number y\n"))

check_division(x, y)
