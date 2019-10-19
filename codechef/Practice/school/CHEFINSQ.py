# https://www.codechef.com/problems/CHEFINSQ

# l = list(map(int, input().split()))
# subset = {}
# for i in range(len(l)):
#     for j in range(i, len(l) - 1):
#         s = l[i] + l[j + 1]
#         if s in subset:
#             subset.get(s).append((l[i], l[j + 1]))
#         else:
#             subset[s] = [(l[i], l[j + 1])]

# key_min = min(subset.keys(), key=(lambda k: subset[k]))
# print(len(subset[key_min]))
# https://www.geeksforgeeks.org/print-subsets-given-size-set/
# 1 2 3 4
# 0
# 1,1
# 1,2
# 1,3
# 1
# 2,3
# 3,4


def subs(l, k):
    a.sort()
    minpair = a[:k]
    count = 0
    for i in range(len(a) - k):
        for j in range(i + 1, len(a)):
            pair = [a[i]] + a[j : j + (k - 1)]
            if a[i:k] == pair:
                count += 1
            elif sum(pair) > sum(minpair):
                break
    print(count)


n = int(input())
while n != 0:
    i1 = list(map(int, input().split(" ")))
    s, k = i1[0], i1[1]
    a = list(map(int, input().split(" ")))
    subs(a, k)
    n -= 1

