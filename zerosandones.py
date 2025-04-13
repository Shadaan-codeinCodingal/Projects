def  numbits(n):
    o = 0
    z = 0
    while n:
        if  n&1==1:
            o +=1
        else:
            z+=1
        n >>=1
    print('In binary form, ')
    print('The number of ones in that number will be', o)
    print('The number of zeros in that number will be', z)
num = int(input('Enter a number: '))
numbits(num)