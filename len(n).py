def len(lst):
    if lst == []:
        return 0
    return 1 + len(lst[1:])
test_list = [1, 2, 3, 4, 5]
print(f"Length of {test_list} is: {len(test_list)}")
