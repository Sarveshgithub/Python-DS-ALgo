import math 
n = int(input())
s = math.sqrt(n)
nextN = math.floor(s)
if nextN*nextN == n:
    print((nextN*2)-2)
else:
    print((nextN*2)-1) 
