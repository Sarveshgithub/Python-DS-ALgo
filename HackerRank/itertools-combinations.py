from itertools import combinations
def main(word,size):
    combination = list(combinations(word,size))
    sortList = []
    for i in combination:
        l = list(i)
        l.sort()
        sortList.append("".join(l))
    sortList.sort()
    return sortList

word,size = input().split(' ')
for i in range(1,int(size)+1):
    print('\n'.join(main(word,i)))