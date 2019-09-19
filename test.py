from bubbleSort import bubbleSort


def checkInputs(n, array):
    if n == len(array) and len(array) > 1:
        for i in range(0, len(array)):
            array[i] = int(array[i])
        removeDups = list(set(array))
        sortArray = bubbleSort(removeDups)
        return sortArray[len(sortArray) - 2]
    else:
        return "please enter correct values"


n = int(input())
array = input().split()
print(checkInputs(n, array))

