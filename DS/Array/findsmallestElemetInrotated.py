def bs(a, tempArray, L, R):
    mid = (L + R) // 2
    if tempArray[mid] == "T" and tempArray[mid + 1] == "F":
        return a[mid + 1]
    elif tempArray[mid + 1] == "T":
        L = mid + 1
        return bs(a, tempArray, L, R)
    elif tempArray[mid - 1] == "F":
        R = mid - 1
        return bs(a, tempArray, L, R)
    elif tempArray[mid] == "F":
        return a[mid]
    else:
        return -1


a = [3, 1, 2]
# T, T, T, T, T, F,F
end = a[len(a) - 1]
tempArray = []
for i in a:
    if i <= end:
        tempArray.append("F")
    else:
        tempArray.append("T")

L, R = 0, len(a) - 1
smallest = -1
if "T" not in tempArray:
    smallest = a[0]
else:
    smallest = bs(a, tempArray, L, R)
print(smallest)

