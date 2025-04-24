def revstr(s):
    if len(s)==1:
        return s[0]
    fc = s[0]
    return revstr(s[1:])+fc
stri = input('enter a string: ')
print(revstr(stri))