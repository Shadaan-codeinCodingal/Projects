m = 5
n = 6
# Function 1 takes 1 iteration
def func1(x,y):
  return x*y
print(func1(m,n))
# Function 2 takes n iterations
def func2(x,y):
  sum = 0
  for i in range(y):
    sum = sum+x
  return sum
print(func2(m,n))