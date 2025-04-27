def hanoi(n,a,b,c):
    if n ==1:
        print('Move disk 1 from pole', a, 'to pole',b)
        return
    hanoi(n-1,a,c,b)
    print('Move disk',n,'from pole',a,'to pole',b)
    hanoi(n-1,c,b,a)
n = 3
hanoi(n,'A','C','B')