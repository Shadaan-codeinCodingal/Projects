def myfunction(n):
  iterations= 0
  for i in range(0,n+1):
    print("first loop")
    iterations+=1
  #For loop 1, we have n iterations(O(n)).
  j=1
  while(j<=n+1):
    print("second loop",j)
    j=j*2
    iterations+=1
  # For loop 2, we have the number of powers till n iterations(O(log(n)))
  for i in range(0,100):
    print("third loop")
    iterations+=1
  # For loop 3, we have 100 iterations and it will be constant(O(1)).
  # It will take atleast 101 iterations(1 is lowest value) = 1 + 1 + 99 = 101
  print(f'The total number of iterations so far is {iterations}')
myfunction(7)
print('\n')
myfunction(8)