def revnum(n):
    if n>0:
        last = n%10
        if n//10>0:
            temp = revnum((int)(n//10))  
            return last * pow(10,len(str(temp)))+temp
        return n
user = int(input('enter a number: '))
print('its reverse is:', revnum(user))