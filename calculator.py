a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
symbol = input("What operation do you want to use?(+,-,*(nultiply),/(division but it will alway return decimal),%(modulo returns the remainder),//(Division always returns whole number),**(Exponent multiplying a number certain number of times)")
def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mutipli(x,y):
    return x * y
def deciDiv(x,y):
    return x / y
def floorDiv(x,y):
    return x // y
def mod(x,y):
    return x %  y
def expo(x,y):
    return x**y
if symbol == "+":
    print(add(a,b))
elif symbol == "-":
    print(sub(a,b))
elif symbol == "*":
    print(mutipli(a,b))
elif symbol == "/":
    print(deciDiv(a,b))
elif symbol == "//":
    print(floorDiv(a,b))
elif symbol =="%":
    print(mod(a,b))
elif symbol == "**":
    print(expo(a,b))
else:
    print("Error! Couldn't calculate the operation.")