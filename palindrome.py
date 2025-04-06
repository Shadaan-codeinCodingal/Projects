n = int(input('Enter a number: '))
o = n
r = 0
while n > 0:
    digit = n % 10
    r = digit + r*10
    n //= 10
if o == r:
    print('Your number is a palindrome.')
else:
    print('Your number is not a palindrome.')