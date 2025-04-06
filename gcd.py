nl = int(input('Enter a number: '))
ns = int(input('Enter a smaller number:'))
while ns:
    nst = ns
    ns = nl % ns
    nl = nst
print('Their GCD/HCF is ', nst)