"""Bir o`lchamli sonli massivni tоq qiymatli elеmеntlarini juft o`rinli
elеmеntlari yig’indisiga bo`lib chiqilsin"""
n=int(input())
s=input().split(" ")
for i in range(n):
    s[i]=int(s[i])
d=[]
q=0
for i in range(n):
    if (i-1)%2==0:
        q+=s[i]
for i in range(n):
    if s[i]%2==1 and s[i]>0:
        for j in range(n):
            d.append(s[j]/q)
ss=""
for i in range(len(d)):
    d[i]=float("%.2f"%d[i])
    ss+=str(d[i])+" "
print(ss)
#masala ishlanmadi !