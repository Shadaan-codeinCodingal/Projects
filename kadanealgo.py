def kadane(a,s):
    max = -999999999999
    cmax = 0
    for i in range(0,s):
        cmax+=arr[i]
        if cmax>max:
            max=cmax
        if cmax<0:
            cmax =0
    return max
arr = [1,2,3,-4,5,-22,-4,25,2,-9]
print(kadane(arr,len(arr)))