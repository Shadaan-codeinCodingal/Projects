import random
def lae(arr):
    if len(arr)==1:
        return arr[0]
    return max(arr[0], lae(arr[1:]))
a = []
for i in range(random.randint(1,10)):
    a.append(int(input('Enter a number: ')))
print('the largest number of all the numbers you entered is', lae(a))