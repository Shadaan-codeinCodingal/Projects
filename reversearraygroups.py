def revarrgr(a,s,n):
    temp = 0
    while temp<s:
        start = temp
        end = min(temp+n-1, s-1)
        while start<end:
            a[start], a[end] = a[end], a[start]
            start +=1
            end-=1
        temp+=n
arr = [6,3,5,33,1,3,34,3,3,1,3,6]
arr_length = len(arr)
group_size = 2
revarrgr(arr,arr_length,group_size)
for i in range(arr_length):
    print(arr[i],end=" ")