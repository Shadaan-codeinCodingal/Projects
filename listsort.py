def checkifsort(arr):
    if len(arr)==1 or len(arr)==0:
        return True
    return arr[0]<arr[1] and checkifsort(arr[1:])
array=[]
for i in range(6):
    array.append(int(input('Enter a number')))
if checkifsort(array):
    print('The array is sorted.')
else:
    print('The array is not sorted.')