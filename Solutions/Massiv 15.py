"""Bir o`lchamli sonli massivni M dan kichik elеmеntlarini kvadratlarini
yig’indisiхisоblansin """
import math
n=int(input())
s=input().split(" ")
m=int(input())
q=0
for i in range(n):
    s[i]=int(s[i])
    if s[i]<m:
        q+=math.pow(s[i],2)
print(int(q))
#masala ishlandi