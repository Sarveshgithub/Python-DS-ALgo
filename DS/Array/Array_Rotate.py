# https://www.geeksforgeeks.org/array-rotation/
# t = 1
arr = [1, 2, 3, 4]

size = len(arr)
temp = arr[size - 1]
# lastElement = arr[size - 1]
for i in range(0, size - 1):
    arr[size - 1 - i] = arr[size - 1 - i - 1]
arr[0] = temp
print(arr)

