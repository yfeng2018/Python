# python 2
# 
# Name: Muhamed Adilovic
#
# Homework 2, Problem 1
# slicing and indexing challenges
#

pi = [3,1,4,1,5,9]
e = [2,7,1]

# Example problem (problem 0):
# Creating the list [2,5,9] from pi and e
answer0 = [ e[0] ] + pi[-2:]     
print answer0

# Problem 1:
# Creating the list [7,1] from pi and e
answer1 = e[1:]
print answer1

# Problem 2:
# Creating the list [9,1,1] from pi and e
answer2 = pi[::-4] + [e[-1]]
print answer2

# Problem 3:
# Creating the list [1,4,1,5,9] from pi and e
answer3 = pi[1:]
print answer3

# Problem 4:
# Creating the list [1,2,3,4,5] from pi and e
answer4 = e[::-2] + pi[::2]
print answer4



# starting strings for Homework 1

h = 'harvey'
m = 'mudd'
c = 'college'

# Problem 5:
# Creating the string 'heyyou'
answer5 = h[0] + h[4:] + h[-1] + c[1] + m[1]
print answer5

# Problem 6:
# Creating the string 'collude'
answer6 = c[0:4] + m[1:3] + c[-1]
print answer6

# Problem 7:
# Creating the string 'arveyudd'
answer7 = h[1:] + m[1:]
print answer7

# Problem 8:
# Creating the string 'hardeharharhar'
answer8 = h[0:3] + m[-1] + c[-1] + 3*h[0:3]
print answer8

# Problem 9:
# Creating the string 'legomyego'
answer9 = c[-4:-1] + c[1] + m[0] + h[-1] + c[-3:-1] + c[1]
print answer9

# Problem 10:
# Creating the string 'clearcall'
answer10 = c[0:5:2] + h[1:3] + c[0] + h[1] + c[2:4]
print answer10
