def water(a,s):
    water = 0
    lt = [0]*s
    rt = [0]*s
    lt[0] = a[0]
    for i in range(1,s):
        lt[i] = max(lt[i-1],a[i])
    rt[s-1] = a[s-1]
    for j in range(s-2,-1,-1):
        rt[j] = max(rt[j+1],a[j])
    for k in range(0,s):
        water += min(lt[k],rt[k])-a[k]
    return water
array = [0,1,0,2,1,0,1,3,2,1,2,1]
bars = water(array,len(array))
print('Water:', bars)