def Count(s, L):
    count = 0
    for letter in s:
        if letter == L:
            count += 1
    print(count)

Count('jabadabadu', 'a')
