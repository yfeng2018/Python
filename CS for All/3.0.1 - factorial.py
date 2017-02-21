def fac(N):
    '''Calculate N! using recursion'''
    if N==0:
        return 1
    else:
        return N*fac(N-1)

print fac(7)
