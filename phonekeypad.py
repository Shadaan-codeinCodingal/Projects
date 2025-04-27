k = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
comb = [7,4,6]
def findcomb(combs, curr,output,n):
    if curr == n:
        print(*output,sep=',')
        return
    for i in range(len(k[combs[curr]])):
        output.append(k[combs[curr]][i])
        findcomb(combs, curr+1,output,n)
        output.pop()
        if combs[curr] == 0 or combs[curr]==1:
            return
findcomb(comb, 0, [], len(comb))