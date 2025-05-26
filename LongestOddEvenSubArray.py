def findlen(arr):
  length = 1
  subcomp=1
  parity = True if arr[0] % 2 == 0 else False
  for i in range(1,len(arr)):
    if parity==True:
      if arr[i] % 2 == 0:
        subcomp = 1
      else:
        subcomp+=1
        parity = False
    else:
      if arr[i] % 2 == 0:
        subcomp+=1
        parity = True
      else:
        subcomp = 1
    if subcomp >length and (i+1!=len(arr) and (arr[i+1] % 2 == 0)==parity):
      length = subcomp
      subcomp = 1
    if i+1==len(arr) and subcomp>length:
      return subcomp
  else:
    return length
arr = [6,4,9,4,7,2,3,4,2,52]
print(findlen(arr))
