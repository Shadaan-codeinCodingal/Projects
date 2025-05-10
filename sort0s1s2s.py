def sortarray(a,s):
  sortedarray = [[],[],[]]
  for i in range(0,s):
    sortedarray[a[i]].append(a[i])
  actualsortedarray = sortedarray[0]+sortedarray[1]+sortedarray[2]
  return actualsortedarray
arr = [0,1,2,1,0]
print(sortarray(arr,len(arr)))
