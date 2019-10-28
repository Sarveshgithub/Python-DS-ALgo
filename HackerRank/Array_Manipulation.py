#   a b k
    # 1 5 3
    # 4 8 7
    # 6 9 1
i1 = list(map(int,input().split(" ")))
n,m = i1[0],i1[1]
a = [0 for i in range(n)]
for i in range(m):
    val = list(map(int,input().split(" ")))
    for i in range(val[0]-1,val[1]):
        a[i] += val[2]

print(max(a))