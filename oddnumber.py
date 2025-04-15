def findoddoccuringnum(array):
    r = 0
    for i in array:
        r = r ^ i
    return r
print('Write a list containg a specific pair of number reapeatedly found in the array and write one number that is not in the pair')
arr = list(map(int,input().split()))
print('The odd occuring number in this array is', findoddoccuringnum(arr))