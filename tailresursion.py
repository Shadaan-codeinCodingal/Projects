def tail(x,y):
    if x > y:
        return
    print(x)
    tail(x+1,y)
n = int(input('enter a number: '))
tail(1,n)