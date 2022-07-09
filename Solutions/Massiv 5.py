""" Bir o`lchamli sonli massiv [a,b] qismda yotmaydigan elеmеntlarining o`rtacha
qiymati хisоblansin"""
n=int(input())
s=input().split(" ")
a1,b1=map(int,input().split(" "))
a=int(a1)
b=int(b1)
for i in range(n):
    s[i]=int(s[i])
d=[]
for i in range(n):
    if i<(a-1):
        d.append(s[i])
    elif i>(b-1):
        d.append(s[i])
m=0
for i in range(len(d)):
    m+=d[i]
print("%.2f"%(m/len(d)))
#masala ishlandi