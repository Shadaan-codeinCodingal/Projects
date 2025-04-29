def sleoa(a,s):
    l = sll = -2147483648
    for i in range(0,s): 
        if a[i] > l:
            l = a[i]
        elif a[i]>sll and a[i]!= l:
            sll = a[i]
    print(sll)
arr = [1,2,3,4,5,2,6,3,4,5]
size = len(arr)
sleoa(arr,size)