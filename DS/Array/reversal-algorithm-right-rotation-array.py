a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3

# solution 1

# result = a[len(a)-k:] + a[:len(a)-k]
# a[7:] = [8,9,10]
# a[:7] = [1,2,3,4,5,6,7]
# print(result)

# Solution 2
def rightRotation(arr):
    lastElement = arr[len(arr) - 1]
    for i in range(len(arr)):
        arr[len(arr) - i - 1] = arr[len(arr) - i - 2]
    arr[0] = lastElement
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(rightRotation(arr) )   
