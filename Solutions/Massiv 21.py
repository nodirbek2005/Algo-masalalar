""" Bir o`lchamli sonli massivni M - dan kеyingi elеmеntlari yig’indisini
tоping"""
import math
n=int(input())
s=input().split(" ")
m=int(input())
for i in range(n):
    s[i]=int(s[i])
d=[]
for i in range(m):
    d.append(s[i])
for j in range(len(d)):
    s.remove(d[j])
q=0
for i in range(len(s)):
    q+=s[i]
print(q)
#masala ishlandi