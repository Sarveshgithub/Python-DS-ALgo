def leftRotation(a, d):

    # while d != 0:
    #     firstElement = a[0]
    #     for i in range(len(a) - 1):
    #         a[i] = a[i + 1]
    #     a[len(a) - 1] = firstElement
    #     d -= 1
    return " ".join(a[d:] + a[:d])


d = int(input().split(" ")[1])
a = input().split(" ")
print(leftRotation(a, d))

