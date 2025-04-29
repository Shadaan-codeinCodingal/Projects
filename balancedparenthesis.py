def p(s,a,b,c,n):
    if c==2*n:
        for i in s:
            print(i,end="")
        print("\n")
        return
    if a > b:
        s[c] = "}"
        p(s,a,b+1,c+1,n)
    if a < n:
        s[c]="{"
        p(s,a+1,b,c+1,n)
n = int(input('enter no. of parenthesis: '))
s = [""]*2*n
p(s,0,0,0,n)2