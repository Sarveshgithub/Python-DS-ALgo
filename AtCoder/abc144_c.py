import math 
n = int(input())
a,b=0,0
print(1,int(1+n**.5))
for i in range(1,int(1+n**.5)):
    if (n%i==0):
        a,b=i,n//i
print(a+(b-2))

