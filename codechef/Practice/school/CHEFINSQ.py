# https://www.codechef.com/problems/CHEFINSQ

l = list(map(int, input().split()))
subset = {}
for i in range(len(l)):
    for j in range(i, len(l) - 1):
        s = l[i] + l[j + 1]
        if s in subset:
            subset.get(s).append((l[i], l[j + 1]))
        else:
            subset[s] = [(l[i], l[j + 1])]

key_min = min(subset.keys(), key=(lambda k: subset[k]))
print(len(subset[key_min]))
# 1 2 3 4
# 0
# 1,1
# 1,2
# 1,3
# 1
# 2,3
# 3,4
