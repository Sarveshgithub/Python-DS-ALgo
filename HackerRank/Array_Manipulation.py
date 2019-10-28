#   a b k
    # 1 5 3
    # 4 8 7
    # 6 9 1
    
i1 = list(map(int,input().split(" ")))
n,m = i1[0],i1[1]
a = [0]*(n+2)
for i in range(m):
    val = list(map(int,input().split(" ")))
    a[val[0]]+= val[2]
    a[val[1]+1]+= -val[2]
for i in range(1,len(a)):
    a[i] = a[i-1]+a[i]
print(max(a))