from itertools import groupby

i = input()
group = []
for k, g in groupby(i):
    group.append((len(list(g)), int(k)))

# print(group)
print(" ".join("({}, {})".format(*el) for el in group))
# # print(group)
# test = input()
# group = []
# start = 0
# inner = 0
# for i in range(start, len(test), 1 + start):
#     val, count = test[start], 1
#     for j in range(start + 1, len(test)):
#         if test[j] == val:
#             count = count + 1
#         else:
#             start = start + count
#             break
#     if inner == j:
#         break
#     inner = j
#     # print("i:", i, "j:", j, "start:", start, "count:", count)
#     group.append((count, int(val)))

# print(" ".join("({}, {})".format(*el) for el in group))
# # print(group)
