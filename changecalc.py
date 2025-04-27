def find_combinations(amount):
    coins = [500, 100, 10, 5, 1]
    index=0
    current=[]
    if amount == 0:
        print(current)
        return
    if amount < 0 or index >= len(coins):
        return
    find_combinations(amount - coins[index], index, current + [coins[index]])
    find_combinations(amount, index + 1, current)
n = int(input("Enter amount: "))
find_combinations(n)
