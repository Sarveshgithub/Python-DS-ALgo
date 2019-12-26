from itertools import permutations
def main(word,size):
    permutation = list(permutations(list(word),size))
    comboList = ["".join(i) for i in permutation]
    comboList.sort()
    return comboList


word,size = input().split(' ')
print('\n'.join(main(word,int(size))))