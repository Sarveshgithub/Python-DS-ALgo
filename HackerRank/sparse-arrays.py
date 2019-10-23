def findSparse(a, q):
    r = []
    for i in q:
        c = 0
        if i in a:
            for j in a:
                if i == j:
                    c += 1
        r.append(c)
    return "\n".join([str(i) for i in r])


n = int(input())
s = [input() for i in range(n)]
n2 = int(input())
q = [input() for i in range(n2)]
print(findSparse(s, q))
# print(s, q)
