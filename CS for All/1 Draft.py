def makes10(a, b):
  if a or b == 10:
    return True
  elif a+b==10:
    return True
  elif a+b!=10:
      return False
  else:
    return False

print(makes10(9,9))
