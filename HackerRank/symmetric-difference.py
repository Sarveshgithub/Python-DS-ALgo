i1 = int(input())
m = set(map(int, input().split()))
i2 = int(input())
n = set(map(int, input().split()))
s = m.difference(n)
p = n.difference(m)
s.update(p)
f = list(s)
f.sort()
[print(i) for i in f]

