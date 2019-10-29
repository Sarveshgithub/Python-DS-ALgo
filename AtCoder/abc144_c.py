import math 
n = int(input())
s = math.sqrt(n)
ps = math.floor(s)
for i in range(1,ps+1):
    for j in range(ps,ps*2+1):
        if i*j == n:
            print(i+(j-2))
            break

