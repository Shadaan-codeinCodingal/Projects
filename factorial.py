def fac(n):
    if n==1 or n == 0:
        return 1
    return n * fac(n-1)
n = int(input('Enter a number: '))
print(f"{n}! = {fac(n)}")
# Iterative Approach
mul = 1
while n>1:
    mul *=n
    n -=1
print(mul)
l = 1
for i in range(2, n+1):
    l *= i
print(l)