def computepower(a, b):
    r = 1
    while b > 0:
        if b %2 == 0:
            a = a * a
            b>>=1
        else:
            r = r *a
            b -=1
    return r
x = int(input('Enter x in x^y: '))
y = int(input('Enter y in x^y: '))
print('x^y=', computepower(x,y))