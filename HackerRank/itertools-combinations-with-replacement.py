from itertools import combinations_with_replacement


def main(s, k):
    combo = list(combinations_with_replacement(s, k))
    joinTuple = []
    for i in combo:
        l = list(i)
        l.sort()
        joinTuple.append("".join(l))
    joinTuple.sort()
    return joinTuple


s, k = input().split(" ")
k = int(k)

print("\n".join(main(s, k)))

