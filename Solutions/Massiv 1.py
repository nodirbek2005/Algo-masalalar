""" Bir o`lchamli sonli massivni o`rtacha qiymatidandan kichik elеmеntlarini
o`rtacha qiymati хisоblansin."""
n=int(input())
s=input().split(" ")
k=0
for i in range(n):
    s[i]=int(s[i])
    k+=s[i]
med=k/n
d=[]
q=0
for i in range(n):
    if s[i] < med:
        d.append(s[i])
for i in range(len(d)):
    q+=d[i]
print("%.2f"%(q/len(d)))
#masala ishlandi