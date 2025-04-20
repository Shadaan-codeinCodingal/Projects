def incdec(x,y):
    if x < 1 or x > y:
        return
    print(x)
    incdec(x-1,y)
    print(x)
n = int(input('Enter a number: '))
incdec(n,n)