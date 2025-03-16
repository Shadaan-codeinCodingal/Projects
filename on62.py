def createstars(n):
    iterations = 0
    for i in range(0,n):
        for j in range(0,n):
            print('*', end = " ")
            iterations+=1
        print(' ')
    print(f'When n = {n}, the number of iterations will be {iterations}.')
createstars(5)
createstars(4)
createstars(3)
print('Conclusion: No matter what value of n, the number of iterations will be n^2(or n*n).')