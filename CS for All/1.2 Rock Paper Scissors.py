# Name: Muhamed Adilovic
# Date: February 13, 2017

import random

user = raw_input("Choose your weapon: ")
comp = random.choice( ['rock','paper','scissors'] )

print 'the user (you) chose', user
print 'the comp (I) chose', comp

if user == 'rock':
    if comp == 'rock':
        print 'It seems is\'s tied'
    elif comp == 'paper':
        print 'Ha, I win!'
    else:
        print 'I\'ll have better luck next time, mark my words!'

if user == 'paper':
    if comp == 'paper':
        print 'It seems is\'s tied'
    elif comp == 'scissors':
        print 'Ha, I win!'
    else:
        print 'I\'ll have better luck next time, mark my words!'

if user == 'scissors':
    if comp == 'scissors':
        print 'It seems is\'s tied'
    elif comp == 'rock':
        print 'Ha, I win!'
    else:
        print 'I\'ll have better luck next time, mark my words!'

