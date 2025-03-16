def iterations(n):
    iteration = 0
    for i in range(1, n+1):
        iteration +=1
    print(f'When n is {n}, the number of iterations will be {iteration}')
iterations(10)
iterations(20)
iterations(30)
print('Conclusion: The number of iterations will be the value of n. When n increases, the number of iterations increases and vice versa.')