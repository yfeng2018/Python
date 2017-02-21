def is_palindrome(word):
    if len(word)>1:
        if word[0] != word[-1]:
            return False
        else:
            word=word[1:-1]       
            return is_palindrome(word)
    else:
        return True

unos = input("Type the word that you want to check if it is palindrome or not...\n")
                   
print(is_palindrome(unos))
