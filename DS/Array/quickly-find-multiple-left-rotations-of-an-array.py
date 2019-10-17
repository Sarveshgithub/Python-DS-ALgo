# Quickly find multiple left rotations of an array | Set 1
# Given an array of size n and multiple values around which we need to left rotate the array. How to quickly find multiple left rotations?

# Examples:

# Input : arr[] = {1, 3, 5, 7, 9}
#         k1 = 1
#         k2 = 3
#         k3 = 4
#         k4 = 6
# Output : 3 5 7 9 1
#          7 9 1 3 5
#          9 1 3 5 7
#          3 5 7 9 1

# Input : arr[] = {1, 3, 5, 7, 9}
#         k1 = 14
# Output : 9 1 3 5 7


# left rotation of array


def leftRotion(arr):
    last = len(arr) - 1
    first = arr[0]
    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]
    arr[last] = first
    return arr


def nTimes(n, arr):
    if n == 0:
        return arr
    else:
        arr = leftRotion(arr)
    return nTimes(n - 1, arr)


arr = [1, 3, 5, 7, 9]
print(nTimes(14, arr))
