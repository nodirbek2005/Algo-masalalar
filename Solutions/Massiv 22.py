"""Bir o`lchamli sonli massivni elеmеntlarini kvadratlari yig’indisi va
o`rtacha qiymati хisоblansin """
import math
n=int(input())
s=input().split(" ")
for i in range(n):
    s[i]=int(s[i])
q=0
p=0
for i in range(n):
    q+=math.pow(s[i],2)
    p+=s[i]
print(int(q),"%.2f"%(p/n))
#masala ishlandi