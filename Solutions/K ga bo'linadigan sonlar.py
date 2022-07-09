import math
k1,a1,b1,=map(int,input().split(' '))
k=int(k1)
a=int(a1)
b=int(b1)
n=0
for i in range(a,b+1):
    if i%k==0:
     n+=1
print(n)
#time limit

