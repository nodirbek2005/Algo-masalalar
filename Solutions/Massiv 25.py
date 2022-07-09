""" Bir o`lchamli sonli massiv k - elеmеntidan l – elеmеntigacha (yani
[k,l]) bo`lgan elеmеntlarining kublari yig’indisi хisоblansin"""
import math
n=int(input())
s=input().split(" ")
l1,r1=map(int,input().split(" "))
l=int(l1)
r=int(r1)
q=0
for i in range(n):
    s[i]=int(s[i])
for i in range(l-1,r):
    q+=math.pow(s[i],3)
print(int(q))
#masala ishlandi