# https://www.geeksforgeeks.org/array-rotation/
# t = 1


def rightRotaion(arr):
    size = len(arr)
    temp = arr[size - 1]
    for i in range(0, size - 1):
        arr[size - 1 - i] = arr[size - 1 - i - 1]
    arr[0] = temp
    return arr


output = []
n = int(input())
for _ in range(n):
    input()
    a = [int(i) for i in input().split(" ")]
    s = len(a)
    tempArr = a
    count = 0
    for i in reversed(range(s)):
        tempArr = rightRotaion(tempArr)
        if i - count > -1:
            del tempArr[i - count]
        else:
            del tempArr[0]
        count += 1
        if len(tempArr) == 1:
            break
    print(str(tempArr[0]))
