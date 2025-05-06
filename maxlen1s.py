def maxones(arr, s):
    count = 0
    maxone= 0
    for i in range(0,s):
        if arr[i] == 0:
            count = 0
        else:
            count+=1
            maxone = max(maxone, count)
    return maxone
arr = [1,1,0,0,0,1,1,1,0,1,1,1,1]
print(maxones(arr,len(arr)))