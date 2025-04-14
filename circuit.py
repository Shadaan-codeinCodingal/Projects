# The circuit shows that Q = (A & B) | ((B|C)&(B&C))
def findq(a, b, c):
  return (a&b)|((b|c)&(b&c))
a = int(input('enter a number: '))
b = int(input('enter a number: '))
c = int(input('enter a number: '))
print('My circuit diagram shows the output Q = (A & B) | ((B|C)&(B&C)) where a is the first number, b is the second number and cis the third number giving the output Q =', findq(a, b, c))
