""" Bir o`lchamli sonli massivni juft qiymatli elеmеntlarini o`rtacha
qiymatiхisоblansin"""

n=int(input())
satr=input().split(" ")
d=[]
s=0
for i in range(n):
    satr[i]=int(satr[i])
for i in range(n):
    if satr[i]%2==0:
        d.append(satr[i])
for i in range(len(d)):
    d[i]=int(d[i])
    s+=d[i]
print(s/len(d))
#masala ishlandi