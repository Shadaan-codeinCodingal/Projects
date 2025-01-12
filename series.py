def seriescaluclate():
    n = int(input("Enter a number: "))
    sum = 0
    x = 1
    for i in range(1, n+1):
        sum = sum + x
        x = x + 3
    return sum
print(seriescaluclate())