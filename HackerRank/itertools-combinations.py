from itertools import combinations
def main(word,size):
    combination = list(combinations(word,size))
    comboList = ["".join(i) for i in combination]
    comboList.sort()
    return comboList


word,size = input().split(' ')
for i in range(1,int(size)+1):
    print('\n'.join(main(word,i)))