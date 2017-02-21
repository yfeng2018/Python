def is_between(x, y, z):
    if x<=y<=z:
        return True
    else:
        return False

if is_between(4, 7, 6):
    print("They are in the order...")
else:
    print("They are not in the order...")

if is_between(5, 19, 212415):
    print("They are in the correct order...")
else:
    print("they are not in the correct order...")
