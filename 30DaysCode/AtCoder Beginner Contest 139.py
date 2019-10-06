# https://atcoder.jp/contests/abc139/tasks/abc139_c
# A - Tenki
def a():
    p = list(input())
    a = list(input())
    o = [a[i] for i in range(len(p)) if p[i] == a[i]]
    print(len(o))


# C - Lower
# def c():
#     input()
#     a = list(map(int, input().split()))
#     m = 0
#     end = 0
#     for i in range(len(a)):
#         if end < len(a) - 2:
#             for j in range(i, len(a) - 1):
#                 if a[j] >= a[j + 1]:
#                     m += 1
#                     end = j
#                 else:
#                     m = 0
#                     break
#     print(m)

input()
a = list(map(int, input().split(" ")))
count = 0
arrayCount = []
for i in range(0, len(a) - 1):
    if a[i] >= a[i + 1]:
        count += 1
    else:
        arrayCount.append(count)
        count = 0
arrayCount.append(count)
print(max(arrayCount))

