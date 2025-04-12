def findparity(n):
    if n ^ 1 == n + 1:
        print(n,'is even.')
    else:
        print(n, 'is odd.')
num = int(input('Enter a number: '))
findparity(num)