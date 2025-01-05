x = 7
y = 9
z = 5
print("Number 1, 2, 3 are",x,y,z)
if x > y:
    x,y = y,x
if z < x:
    z,x = x,z
if y >z:
    y,z = z,y
print(x,y,z)