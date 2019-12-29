# https://www.hackerrank.com/challenges/collections-counter/problem
from collections import Counter

input()
shoes = [int(i) for i in input().split(" ")]
n = int(input())
shoesWithRs = [[int(i) for i in input().split(" ")] for i in range(n)]
countShoes = Counter(shoes)
m = dict(countShoes)
total = 0
for i in shoesWithRs:
    size, prize = i[0], i[1]
    if size in m and m.get(i[0]) != 0:
        total += prize
        m[size] -= 1
print(total)
