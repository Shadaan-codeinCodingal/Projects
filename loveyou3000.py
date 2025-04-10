l = int(input('Enter a very low number greater than 1: '))
h = int(input('Enter a very large number: '))
for i in range(l, h+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
