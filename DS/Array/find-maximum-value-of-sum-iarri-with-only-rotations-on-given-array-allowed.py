def findPivot(a):
    for i in range(0, len(a)):
        if a[i] > a[i + 1]:
            break
    return i + 1


def getMaximum(a, l, r):
    i = len(a) - 1
    count = 0
    while l != r:
        count += a[l] * i
        l = (l - 1) % len(a)
        i = i - 1
    return count


a = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
p = findPivot(a)
print(getMaximum(a, p - 1, p))

