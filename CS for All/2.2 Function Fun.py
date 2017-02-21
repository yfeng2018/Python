# python 2
#
# Homework 2, Problem 2
#
# Name:
# Date:
#

def dbl(x):
    """  output: dbl returns twice its input
         input x: a number (int or float)
         Spam is great, and dbl("spam") is better!
    """
    return 2*x


def tpl(x):
    """  output: tpl returns thrice its input
         input x: a number (int or float)
    """
    return 3*x


def sq(x):
    """ output: sq returns square root of its input
        input x: a number (int or float)
    """
    return x**2


def interp(low,hi,fraction):
    """ output: interp returns the float
        which is fraction of the way between low and hi
        input x: a number (int or float)
    """
    return ((hi-low)*fraction)+low


def checkends(s):
    """ output: "True" if the first and the last letters
        of the string are the same
        Otherwise, it is "False"
        input: a string
    """
    if s[0]==s[-1]:
        return True
    else:
        return False


def flipside(s):
    """ output: returns the string with inverted halves
        input: a string
    """
    h=len(s)/2
    return s[h:]+s[0:h]
    

def convertFromSeconds(s):
    """ output: returns the list of four elements:
        days, hours, minutes and seconds
        input: nonnegative integer representing seconds
    """
    d=s/86400
    h=(s-(d*86400))/3600
    m=(s-((d*86400)+(h*3600)))/60
    sec=s-((d*86400)+(h*3600)+(m*60))
    L=[d,h,m,sec]
    return L


def front3(str):
    """ otput: returns first three letters of a string three times
        if the string is shorter than 3 letters, returns it three times
        input: a string
    """
  if len(str)>=3:
    return 3*str[0:3]
  else:
    return 3*str

print convertFromSeconds(94356)
