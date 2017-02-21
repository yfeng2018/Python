def is_palindrome(word):
    for i in range(((len(word))//2)+1):
        if len(word)<2:
            return True
        if word[0] != word[-1]:
            return False
        word = word[1:-1]
        
print(is_palindrome("anavolimilovana"))

