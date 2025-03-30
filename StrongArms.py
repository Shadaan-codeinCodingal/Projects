number = int(input('Enter a number: '))
digits = len(str(number))
sum = 0
temp = number
while temp >0:
    digit = temp% 10
    sum += digit**digits
    temp//=10
if sum == number:
    print('This number is an armstrong number.')
else:
    print('This number is not an armstrong number.')