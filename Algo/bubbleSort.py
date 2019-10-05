# bubble  sort
def bubbleSort(unSortArray):
    for i in range(len(unSortArray)):
        swap = False
        for j in range(0, len(unSortArray) - i - 1):
            if unSortArray[j] > unSortArray[j + 1]:
                swap = unSortArray[j]
                unSortArray[j] = unSortArray[j + 1]
                unSortArray[j + 1] = swap
                swap = True
        if swap == False:
            break
    return unSortArray
