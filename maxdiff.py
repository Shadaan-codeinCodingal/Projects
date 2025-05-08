def find_max_difference(arr):
  n = len(arr)
  if n < 2:
    return 0
  min_val = arr[0]
  max_diff = 0
  for i in range(1, n):
    current_val = arr[i]
    difference = current_val - min_val
    if difference > max_diff:
      max_diff = difference
    if current_val < min_val:
      min_val = current_val
  return max_diff
numbers = [2, 7, 1, 9, 5]
max_difference1 = find_max_difference(numbers)
print(f"The maximum difference in {numbers} is: {max_difference1}")
