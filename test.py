unSortArray = [23, 43, 1, 34, 343, 55]
for i in range(len(unSortArray)):
    index = i
    for j in range(index + 1, len(unSortArray)):
        if unSortArray[index] > unSortArray[j]:
            index = j
    swap = unSortArray[i]
    unSortArray[i] = unSortArray[index]
    unSortArray[index] = swap

print(unSortArray)
