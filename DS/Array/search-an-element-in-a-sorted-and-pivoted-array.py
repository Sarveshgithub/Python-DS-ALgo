# binary search
def bs(arr, L, R, e):
    while L <= R:
        mid = (L + R) // 2
        print("before", L, R, mid)
        print(arr[L], arr[R])
        if arr[mid] == e:
            return mid
        elif arr[mid] < e:
            L = mid + 1
        elif arr[mid] > e:
            R = mid - 1
        print("After", L, R, mid)
    return -1


def findPivot(a, l, r):
    mid = (l + r) // 2
    print("m:", mid, "l:", l, "r:", r)
    if l == r:
        return r + 1
    if a[mid] > a[mid + 1]:
        return mid + 1
    if a[mid - 1] <= a[mid]:
        l = mid + 1
    else:
        r = mid - 1
    return findPivot(a, l, r)


a = [34, 43, 45, 1, 2, 3, 4, 5]
pivot = -1
l, r = 0, len(a) - 1

pivot = findPivot(a, l, r)
target = 4
if target == a[pivot]:
    print(pivot)
elif target < a[pivot] or target > a[len(a) - 1]:
    print(bs(a, l, pivot - 1, target))
else:
    print(bs(a, pivot, r, target))
# print(a[pivot:])

