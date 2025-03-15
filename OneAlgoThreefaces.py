def method1(n):
    return n * (n+1)/2
print(method1(7))
def method2(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
print(method2(7))
def method3(n):
    add = 0
    for j in range(1, n+1):
        for k in range(1,j+1):
            add+=1
    return add
print(method3(7))