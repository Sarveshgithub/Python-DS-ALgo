array = [input().split(" ") for i in range(6)]
hourglass = []

for i in range(6):
    if i == 4:
        break
    for j in range(6):
        t = array[i][j : j + 3] + array[i + 1][j + 1 : j + 2] + array[i + 2][j : j + 3]
        hourglass.append(sum(map(int, t)))
        if j == 3:
            break
hourglass.sort()
print(hourglass[::-1][0])
