""" Bir o`lchamli sonli massiv K yoki M ga tеng elеmеntlari
ko`paytmasiхisоblansin"""
n=int(input())
s=input().split(" ")
k1,m1=map(int,input().split(" "))
k=int(k1)
m=int(m1)
p=1
d=[]
for i in range(n):
    s[i]=int(s[i])
    if s[i]==k or s[i]==m:
        p*=s[i]
print(p)
#masala ishlandi