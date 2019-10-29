# https://atcoder.jp/contests/abc144/tasks/abc144_b
n = int(input())
o = 'No'
if n <=81:
    for i in range(1,10):
        r = n%i
        q = n//i
        if r == 0 and 1<=q<= 9:
            o = 'Yes'
            break
print(o)