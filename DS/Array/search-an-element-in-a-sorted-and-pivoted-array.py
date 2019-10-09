def searchElement(arr, e):
    L, R = 0, len(arr) - 1
    while arr[L] <= arr[R]:
        mid = L + R // 2
        if arr[mid] == e:
            return mid
        elif arr[mid] < e:
            L = mid + 1
        elif arr[mid] > e:
            R = mid - 1

    return -1


a = [30, 40, 50, 10, 20]
e = 10
a.sort()
print(searchElement(a, e))

