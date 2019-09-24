# Problem
# https://www.hackerrank.com/challenges/designer-door-mat/problem
a = input().split()
n, m = int(a[0]), int(a[1])
for i in range(n):
    if i % 2 != 0:
        print((".|." * i).center(m, "-"))
print("WELCOME".center(m, "-"))
for i in range(n):
    if i % 2 != 0:
        print((".|." * (n - i - 1)).center(m, "-"))
