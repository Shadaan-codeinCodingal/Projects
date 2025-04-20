def head(x, y):
    if x > y:
        return 
    head(x+1,y)
    print(x)
x = int(input('Enter a number:'))
head(1,x)