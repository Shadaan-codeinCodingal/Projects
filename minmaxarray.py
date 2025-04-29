arr = [3,6,5,7,3,4,6,3,4,2,3]
l = 0
for i in range(len(arr)):
    if arr[i]> l:
        l=arr[i]
print(l)
s = arr[0]
for i in range(1,len(arr)):
    if arr[i] < s:
        s = arr[i]
print(s)