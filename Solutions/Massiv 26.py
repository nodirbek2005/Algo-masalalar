""" Bir o`lchamli sonli massivni manfiy elеmеntlari massivni o`rtacha
qiymatini lоgarifmi bilan almashtirilsin"""
import math
n=int(input())
s=input().split(" ")
q=0
for i in range(n):
    s[i]=int(s[i])
for i in range(n):
    q+=s[i]
m="%.2f"%(math.log(q/n))
for i in range(n):
    if s[i]<0:
        s[i]=m
for i in range(n):
    s[i]=float(s[i])
ss=""
for i in range(len(s)):
    ss+=str(s[i])+" "
print(ss)
#masala ishlandi