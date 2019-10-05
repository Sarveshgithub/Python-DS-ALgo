def binarySearch(a, target):
    L, R = 0, len(a) - 1
    while a[L] <= a[R]:
        mid = (L + R) // 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            L = mid + 1
        elif a[mid] > target:
            R = mid - 1
    return -1


a = [9, 8, 4, 5, 1, 2]

a.sort()
print(a)
val = 1
print(binarySearch(a, val))

