def vowels(s):
    Vowels=['a', 'e', 'i', 'o', 'u']
    if len(s)==0:
        return 0
    elif s[0] in Vowels:
        return 1+vowels(s[1:])
    else:
        return vowels(s[1:])
