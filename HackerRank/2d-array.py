arr = [[int(j) for j in input().split(" ") if j != ""] for i in range(6)]


def showArr(arr):
    for i in range(6):
        for j in range(6):
            print(arr[i][j], " ", end="")
        print("\n")


def minhourglasses(arr):
    s = -100000
    for i in range(0, 4):
        for j in range(0, 4):
            ts = sum(arr[i][j : j + 3] + [arr[i + 1][j + 1]] + arr[i + 2][j : j + 3])
            if ts > s:
                s = ts
                # glass = arr[i][j : j + 3] + [arr[i + 1][j + 1]] + arr[i + 2][j : j + 3]
    return s


# for index, i in enumerate(minhourglasses(arr)):
#     if index == 3:
#         print(
#             "\n", " ", i, " ",
#         )
#     else:
#         print(i, " ", end="")
print(minhourglasses(arr))
# print
# print(arr)
# showArr(arr)
