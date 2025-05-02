arr = [1,7,3,6,2,4]
arr.sort()
for i in range(0,len(arr)):
  x = arr[i]
  if i != 0:
    y = arr[i-1]
    if x -1 != y:
      print(x-1)
      break
