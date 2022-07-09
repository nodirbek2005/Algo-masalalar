import math

x1,n1=map(int,input().split(" "))
x=int(x1)
n=int(n1)
s=0
for i in range(1,n+1):
    s+=math.pow(x+1,1/i)
print("%.2f"%s)