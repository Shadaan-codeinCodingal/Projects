def wtcs(s):
    if s < 0:
        return
    if s==0:
        return 1
    ts = 0
    os = 0
    if s >=2:
        ts = wtcs(s-2)
    os = wtcs(s-1)
    return os + ts
stairs = int(input('In climbing stairs problem, enter the number of stairs: '))
print('Total number of ways you can climb all stairs by taking 1 or 2 steps:', wtcs(stairs))