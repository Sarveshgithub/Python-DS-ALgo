def getPair(arr, l, r, x):
    while l != r:
        s = arr[l] + arr[r]
        if s == x:
            return (arr[l], arr[r])
        if s > arr[r]:
            r = (r - 1) % len(arr)
        else:
            l = (l + 1) % len(arr)
    return False


arr = [11, 15, 6, 8, 9, 10]
x = 16
l, r = 0, 0
for i in range(0, len(arr) - 1):
    if arr[i] > arr[i + 1]:
        l, r = i + 1, i
        break
print(getPair(arr, l, r, x))
