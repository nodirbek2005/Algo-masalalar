""" Bir o`lchamli sonli massiv max elеmеnti bilan k chi elеmеnti o’rnini
almashtiring. max elementdan bir necha bo’lishi mumkin."""
n=int(input())
s=input().split(" ")
k=int(input())
d=[]
for i in range(n):
    s[i]=int(s[i])
    d.append(s[i])
d.sort()
d.reverse()
max=d[0]
c=s[k-1]
s[k-1]=max
max=c
ss=""
for i in range(n):
    ss+=str(s[i])+" "
print(ss)
#masala yakunlanmadi !