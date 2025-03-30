def findnumber(n):
    roman = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    sum = 0
    for i in range(0,len(n)-1):
        if roman[n[i]]<roman[n[i+1]]:
            sum -=roman[n[i]]
        else:
            sum+=roman[n[i]]
    return sum + roman[n[-1]]
ronum = input('Enter a roman numeral: ')
print(f'This roman numeral represents {findnumber(ronum)}')