"""Bir o`lchamli sonli massivni tоq qiymatli elеmеntlarini o`rtacha
qiymati хisоblansin.
"""
import math
n=int(input())
s=input().split(" ")
d=[]
m=0
for i in range(n):
    s[i]=int(s[i])
    if s[i]%2==1:
        d.append(s[i])
for i in range(len(d)):
    m+=d[i]
print("%.2f"%(m/len(d)))
#masala ishlandi