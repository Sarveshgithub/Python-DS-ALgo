s = int(input())
l = [input() for i in range(s)]
d = {}
for i in l:
    if i in d:
        d.update({i: d.get(i) + 1})
    else:
        d[i] = 1
print(len(d))
print(" ".join([str(i) for i in d.values()]))
