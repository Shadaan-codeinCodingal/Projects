x = int(input('Enter a number:'))
y = int(input('Enter another number:'))
hcf = 0
# Method 1
p = 1
while x*p%y!=0:
    p+=1
print(x*p)
# Method 2
  # Caluclating gcd on our own
def gcdl(x, y):
    while y:
        x, y = y, x % y
    return x
hcf = gcdl(x,y)
  # Using gcd function
import math
hcf = math.gcd(x, y)
 # Caluclating lcm
l= x*y//hcf
print(l)
