def Count(S, L, I):
    count = 0
    index = I
    while index<len(S):
        if S[index] == L:
            count += 1
            index += 1
    print(count)

print(Count('jabadabadu', 'a', 1))
