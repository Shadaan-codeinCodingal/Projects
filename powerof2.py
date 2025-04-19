def checkifpower(n):
    if n==0:
        return 0
    if n &(~(n-1)) == n:
        return 1
    return 0
num = int(input('Enter a number: '))
if checkifpower(num):
    print(f"{num} is a power of 2")
else:
    print(f"{num} is not a power of 2.")