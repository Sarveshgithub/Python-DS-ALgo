# binary search
def bs(arr, L, R, e):
    print(arr, L, R, e)
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
    if l == r:
        return l
    mid = (l + r) // 2
    print(mid)
    if a[mid] > a[mid + 1]:
        return mid + 1
    if a[mid - 1] < a[mid]:
        l = mid + 1
    else:
        r = mid - 1
    return findPivot(a, l, r)


a = [11, 15, 26, 38, 9, 10]
pivot = -1
l, r = 0, len(a) - 1

pivot = findPivot(a, l, r)
# print(a[pivot:])

