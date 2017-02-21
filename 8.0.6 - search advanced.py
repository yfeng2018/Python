def find(word, letter, place):
    index=place
    while index<len(word):
        if word[index]==letter:
            return index
        index=index+1
    return -1

print(len('gdadsvoaiasjdvawevawet'))
print(find('gdadsvoaiasjdvawevawet', 't', 15))
