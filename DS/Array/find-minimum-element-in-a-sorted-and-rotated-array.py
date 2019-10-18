# a = [5, 6, 1, 2, 3, 4]
# a= [1,2,3,4]
# if firstelment < lastelement , so no need to find the pivot
# pivot = the index where the element is grreater then next element
# output = 1


def findPivot(arr):
    l, r = 0, len(arr)
    if arr[0] < arr[len(arr)-1]:
        return arr[0]
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[1]
        else:
            return arr[0]
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            return arr[mid + 1]
        elif arr[mid] < arr[mid + 1]:
            r = mid - 1
        elif arr[mid] > arr[mid + 1]:
            l = mid + 1

arr = [2, 1]
print(findPivot(arr))
