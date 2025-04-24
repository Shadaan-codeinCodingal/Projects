def cip(n):
    if n <= 0:
        return False
    if n==1:
        return True
    if n%4==0:
        return cip(n//4)
    return False
num = int(input('enter a number: '))
if cip(num):
    print('This number is a power of 4.')
else:
    print('This number is not a power of 4.')