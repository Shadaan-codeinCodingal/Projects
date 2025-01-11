l = int(input("Enter a number: "))
h = int(input("Enter a higher number: "))
print("The prime numbers in this range are ")
for i in range(l, h+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)