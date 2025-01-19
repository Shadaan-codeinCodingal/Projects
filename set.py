set1 = {1, 3, 5, 6, 6, 7, 9, 8, 9}
print(set1)
set1.add(2)
print(set1)
set1.remove(7)
print(set1)
set2 = {2, 4, 4, 6, 9, 6, 7}
print(set2)
print("Difference:", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))