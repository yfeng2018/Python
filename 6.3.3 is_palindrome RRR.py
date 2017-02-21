def is_palindrome(word):
    print(word)
    if word[0]!=word[-1]:
        print('Nope, it is not a palindrome...')
    else:
        if len(word)>1:
            word=word[1:-1]
            is_palindrome(word)
        else:
            print('Yes, it is a palindrome!')
    
def ask():
    word=input('Hello.\nThis program checks if the word is a palindrome.\nPlease input a meaningful word...\n')
    print(is_palindrome(word))

ask()
