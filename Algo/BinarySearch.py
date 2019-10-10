def binarySearch(a, target):
    L, R = 0, len(a) - 1
    while L <= R:
        mid = L + (R - L) // 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            L = mid + 1
        elif a[mid] > target:
            R = mid - 1
    return -1


a = [1, 2, 3]

a.sort()
print(a)
val = 30
print(binarySearch(a, val))

