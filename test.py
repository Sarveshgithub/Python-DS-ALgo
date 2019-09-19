from bubbleSort import bubbleSort


def checkInputs(n, array):
    if n == len(array) and len(array) > 1:
        array = [int(array[i]) for i in range(len(array))]
        removeDups = list(set(array))
        sortArray = bubbleSort(removeDups)
        return sortArray[len(sortArray) - 2]
    else:
        return "please enter correct values"


n = 5
array = ["1", "4", "1", "5", "3"]
print(checkInputs(n, array))

