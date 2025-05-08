def kadane(a):
    max = 0
    cmax = 0
    for i in range(0,len(a)):
        cmax +=a[i]
        if cmax < 0:
            cmax = 0
        if max < cmax:
            max = cmax
    return max
def maxcircSum(a):
    max_kadane = kadane(a)
    max_wrap = 0
    for i in range(0,len(a)):
        max_wrap+=a[i]
        a[i]=-a[i]
    max_wrap=max_wrap+kadane(a)
    if max_wrap > max_kadane:
        return max_wrap
    else:
        return max_kadane
arr = [11,10,-20,5,-3,-5,8,-13,10]
print(maxcircSum(arr))