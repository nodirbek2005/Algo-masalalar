"""Bir o`lchamli sonli massiv manfiy elеmеntlarini o`rtacha
qiymati хisоblansin """
n=int(input())
s=input().split(" ")
d=[]
m=0
for i in range(n):
    s[i]=int(s[i])
    if s[i]<0:
        d.append(s[i])
for i in range(len(d)):
    m+=d[i]
print("%.2f"%(m/len(d)))
#masala ishlandi