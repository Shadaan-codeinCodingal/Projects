def find_flips(arr):
    i = 0
    n = len(arr)
    while i < n:
        if arr[i] == 1:
            start = i
            while i + 1 < n and arr[i + 1] == 1:
                i += 1
            end = i
            print(f"Flip from position {start} to {end}")
        i += 1
    print("arr =", [0] * n)
arr = [0, 1, 1, 0, 1, 0, 1, 1, 1]
find_flips(arr)
