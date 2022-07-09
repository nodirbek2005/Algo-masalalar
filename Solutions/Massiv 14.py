""" Bir o`lchamli sonli massiv ni 2 ga va 5 ga bo`linadigan elеmеntlarini
ko`paytmasini sinusi tоpilsin"""
import math
n=int(input())
s=input().split(" ")
m=1
for i in range(n):
    s[i]=int(s[i])
for i in range(n):
    if s[i]%2==0 or s[i]%5==0:
        m*=s[i]
f=math.sin(m)
print("%.2f"%f)
#masala ishlandi