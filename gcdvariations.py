n1 = int(input('Enter a number: '))
n2 = int(input('Enter a number: '))
# Method 1(Shortest)
import math
gcd = math.gcd(n1,n2)
print('Their GCD/HCF is ', gcd)
# Method 2
f1 = set()
f2 = set()
for i in range(1,n1+1):
    if n1%i==0:
        f1.add(i)
for i in range(1,n2+1):
    if n2%i==0:
        f2.add(i)
comfactors = f1.intersection(f2)
print(max(comfactors))