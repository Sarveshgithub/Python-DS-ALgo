# https://www.hackerrank.com/challenges/finding-the-percentage/problem?h_r=next-challenge&h_v=zen
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
score = {}
n = int(input())
for i in range(n):
    s = input().split()
    score[s[0]] = [float(s[i]) for i in range(1, len(s))]
current = input()
lstScore = score.get(current)
print("{:.2f}".format(sum(lstScore) / float(len(lstScore))))
