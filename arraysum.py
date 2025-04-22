import random
def arrsum(a):
    if len(a)==1:
        return a[0]
    return a[0]+arrsum(a[1:])
a = []
for i in range(random.randint(1,10)):
    a.append(int(input('Enter a number: ')))
print('The sum of all numbers you entered is', arrsum(a))