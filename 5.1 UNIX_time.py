import time
time.time()
day = int((time.time()/3600//24)+1)
current_day = (time.time()-((day-1)*3600*24))
hour = int(current_day//3600)
minute = int(((current_day-(hour*3600)))//60)
second = int(current_day-((hour*3600)+(minute*60)))
question = "Would you like to find out the current UNIX time?\n (answer with 'yes' or 'no')\n"

def yes_answer():
    print("Well, I'll be happy to inform you ^_^")
    print("The current day in UNIX time is:", day)
    print("The time in the current UNIX day is:", hour, ":", minute, ":", second)
    print("(That is:", hour, "hours,", minute, "minutes and", second, "seconds)")

def no_answer():
    print("Well, that's too bad...")
    print("I wouldn't tell you anyway...")
    print("Hmpf...")

def maybe_answer():
    print("Ask me once you understand whatchya want in your life, okay?")
    print("And stop wasting my time!")
    print("Good day...")

def options():
    answer = input(question)
    if answer == "yes":
        yes_answer()
        return
    elif answer == "no":
        no_answer()
        return
    elif answer == "maybe":
        maybe_answer()
        return
    else:
        print("I didn't understand...")
        options()

options()
