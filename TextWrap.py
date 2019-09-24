s = input()
w = int(input())
l = "\n".join([s[i : i + w] for i in range(0, len(s), w)])
print(l)

