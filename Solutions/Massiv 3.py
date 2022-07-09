"""Bir o`lchamli sonli massiv k – elеmеntidan l – elеmеntigacha bo`lgan
elеmеntlarining o`rtacha qiymati хisоblansin """
n=int(input())
s=input().split(" ")
a1,b1=map(int,input().split(" "))
k=int(a1)
l=int(b1)
d=[]
m=0
for i in range(n):
    s[i]=int(s[i])
    if i>=(k-1) and i<=(l-1):
        d.append(s[i])
for i in range(len(d)):
    m+=d[i]
print((m/len(d)))
#masala ishlanmadi
#wrong answer 5