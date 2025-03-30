binary = list(input('Enter a binary code: '))
binary.reverse()
power = 1
decimal = 0
for i in binary:
    if i == '1':
        decimal+=power
    power = power * 2
print(decimal)
