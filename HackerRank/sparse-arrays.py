def findSparse(a, q):
    for i in q.keys():
        if i in a:
            for j in a:
                if i == j:
                    q[i] = q[i] + 1
    return "\n".join([str(i) for i in q.values()])


n = int(input())
s = [input() for i in range(n)]
n2 = int(input())
q = {input(): 0 for i in range(n2)}
print(findSparse(s, q))
# print(s, q)
