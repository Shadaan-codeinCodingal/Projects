def zerostoend(a,s):
    zero = 0
    notzero = 0
    while notzero != s:
        if a[notzero] != 0:
            a[zero], a[notzero]=a[notzero],a[zero]
            zero+=1
        notzero+=1
arr = [1,6,2,0,6,3,0,124,0,0,4,2]
print(arr)
zerostoend(arr,len(arr))
print(arr)