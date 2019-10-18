def findPair(startIndex, arr, k, pair, i):
    for i in range(startIndex, len(arr)):
        for j in range(i + 1, len(arr) + 1):
            subarray = arr[i:j]
            if sum(subarray) == k:
                pair.append(subarray)
                return findPair(i + 1, arr, k, pair, i)
            elif sum(subarray) > k:
                break
    if i == len(arr) - 1:
        return pair


# [2, 4, 1, 2, 1, 6, 7, 3, 5, 8]
a = list(map(int, [8, 8, 8]))

print(findPair(0, a, 8, [], 0))
