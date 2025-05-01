def leaders(a,s):
    m = a[s-1]
    print(m)
    for i in range(s-2,-1,-1):
        if a[i]>m:
            print(a[i])
            m = a[i]
arr = [6,3,5,7,5,7,6,8,4,6,3,4,2,3,8,5,6,9,9]
leaders(arr,len(arr))