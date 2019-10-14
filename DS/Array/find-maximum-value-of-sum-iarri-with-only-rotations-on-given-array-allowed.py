def findPivot(a):
    for i in range(0, len(a)):
        if a[i] > a[i + 1]:
            break
    return i + 1


def getMaximum(a, l, r):
    i = len(a)
    while l != r:
        print(":::", l, a[l], l - 1)
        l = (l - 1) % len(a)
        print("::l:", l)
        i = (i - 1) % len(a)


a = [1, 20, 2, 10]
p = findPivot(a)

print(getMaximum(a, p - 1, p))

