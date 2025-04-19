def numprint(n):
    if n > 10:
        return
    print(n)
    numprint(n+1)
numprint(1)