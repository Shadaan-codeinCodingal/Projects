binary = list(input('Enter a binary code: '))
binary.reverse()
power = 1
decimal = 0
for i in binary:
    if i == '1':
        decimal+=power
    if i != '1' and i != '0':
        print('Error!')
        break
    power = power * 2
print(decimal)
