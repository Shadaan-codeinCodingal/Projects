def equibriumpoint(a,s):
    leftsum = 0
    rightsum=0
    for i in range(s):
        leftsum =0
        rightsum=0
        for j in range(i):
            leftsum+=a[j]
        for j in range(i+1,s):
            rightsum+=a[j]
        if leftsum==rightsum:
            return i
    return -1
arr = [-7,1,5,2,-4,3]
print(equibriumpoint(arr,len(arr)))