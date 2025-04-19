def checkpower(n):
    count = 0
    if n & (~(n & (n-1))):
        while n > 1:
            n>>=1
            count +=1
        if count%2==0:
            return True
        else:
            return False
num = int(input('Enter a number: '))
if checkpower(num):
    print(f"{num} is a power of 4.")
else:
    print(f"{num} is not a power of 4.")