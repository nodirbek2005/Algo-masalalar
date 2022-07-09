"""Bir o`lchamli sonli massivni 2 ga, 3 ga yoki 5 ga bo`linadigan
elеmеntlari yigindisi хisоblansin"""
n=int(input())
s=input().split(" ")
d=[]
p=0
for i in range(n):
    s[i]=int(s[i])
for i in range(n):
    if s[i]%2==0 or s[i]%3==0 or s[i]%5==0:
        d.append(s[i])
for i in range(len(d)):
    p+=d[i]
print(p)
#masala ishlandi