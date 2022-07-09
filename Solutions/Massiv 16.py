""" Bir o`lchamli sonli massivni elеmеntlari massivni eng katta elеmеntini
kvadratiga bo`lib chiqilsin"""
import math
n=int(input())
s=input().split(" ")
q=[]
ss=""
for i in range(n):
    s[i]=int(s[i])
for i in range(n):
    max=s[i]
    for j in range(n):
        if s[j]>max:
            max=s[j]
for i in range(n):
    q.append("%.2f"%(s[i]/max))
for i in range(len(q)):
    ss+=str(q[i])+" "
print(ss)
#masala ishlandi