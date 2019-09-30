# Using counter
# https://www.geeksforgeeks.org/counters-in-python-set-2-accessing-counters/
# from collections import Counter

# string = "bbbcccdeaaa"
# s = list(map(str, string))
# print(s)
# s.sort()
# print(s)
# x = Counter(s)
# print(x)
# print(x.most_common(3))
# for key, value in x.most_common(3):
#     print(key, value)
n = 17
print("{0:b}".format(n))
width = len("{0:b}".format(n))
for i in range(1, n + 1):
    print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))
