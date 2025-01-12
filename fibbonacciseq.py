def fibbonacci():
    n = int(input("Enter a number: "))
    num = 0
    num2 = 1
    num3 = 0
    print(num)
    print(num2)
    for i in range(1, n-1):
        num3 = num + num2
        print(num3)
        num = num2
        num2 = num3
fibbonacci()
