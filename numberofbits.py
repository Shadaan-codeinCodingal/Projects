def numbits(n):
    count=0
    p = n
    while n:
        count+=1
        n>>=1
    print('Total bits of',p, 'is', count)
num = int(input('Enter a number: '))
numbits(num)