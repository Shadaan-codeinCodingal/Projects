def sieveprimes(n):
    nums = [True for i in range(n+1)]
    p = 2
    while p * p <= n:
        if nums[p] == True:
            for i in range(p*p, n+1, p):
                nums[i]=False
        p+=1
    for i in range(2, n+1):
        if nums[i]:
            print(i)
l = int(input('Enter a number larger than 2: '))
print(f'The prime numbers until {l} are ')   
sieveprimes(l)        
