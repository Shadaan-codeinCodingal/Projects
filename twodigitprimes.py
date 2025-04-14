primes = list(range(10,100))
for i in range(2,100):
  for j in range(10,100):
    if j % i ==0:
      if j in primes and j != i:
        primes.remove(j)
print(primes)
