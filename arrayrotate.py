def rotations(a,s,n):
    for i in range(n):
        rotate(a,s)
def rotate(a,s):
    temp = a[0]
    for i in range(s-1):
        a[i]= a[i+1]
    a[s-1]=temp
a = [1,36,4,4,2,3,44,55]
for i in range(0,len(a)):
    print(a[i],end=" ")
print("\n")
rotations(a,len(a),4)
for i in range(0,len(a)):
    print(a[i],end=" ")