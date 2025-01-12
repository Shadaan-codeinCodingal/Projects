n = int(input("Enter a number: "))
num_digits = len(str(n))
armstrong_sum = 0
holdingnum = n
while holdingnum > 0:
    digit = holdingnum % 10
    armstrong_sum = armstrong_sum + digit ** num_digits
    holdingnum = holdingnum // 10
if armstrong_sum == n:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")
