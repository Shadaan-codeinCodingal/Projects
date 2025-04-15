def findbothoddoccurinngnums(array):
    xor = array[0]
    x = 0
    y = 0
    for i in range(1, len(array)):
        xor =xor ^array[i]
    sb = 0
    sb = xor & ~(xor -1)
    for i in range(len(array)):
        if array[i]& sb:
            x = x ^ array[i]
        else:
            y = y ^ array[i]
    print('The two odd occuring numbers are', x, 'and', y)
print('Write a list of numbers contating a recurring pair and write 2 odd occuring numbers with a space between them like 6 9 9 6 7 8 6 9 9 6 6 9 6 9')
arr = list(map(int,input().split()))
findbothoddoccurinngnums(arr)