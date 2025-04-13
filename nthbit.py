def nthbit(x, y):
    if x & (1 << y-1):
        print(f'The {y}th bit of {x} in binary is set(1).')
    else:
        print(f'The {y}th bit of {x} in binary is not set(0).')
x = int(input('Enter a number: '))
y = int(input('Enter the position to check a bit of the first number in binary: '))
nthbit(x,y)