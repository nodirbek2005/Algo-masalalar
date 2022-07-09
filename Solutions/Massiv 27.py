"""Bir o`lchamli sonli massivni manfiy elеmеntlari massivni eng kichik
elеmеntini kvadratiga almashtirilsin """
z
n=int(input())
s=input().split(" ")
d=[]
for i in range(n):
    s[i]=int(s[i])
    d.append(s[i])
d.sort()
min=d[0]
for i in range(len(s)):
    s[i]=int(s[i])
    if s[i]<0:
        s[i]=min*min
ss=""
for i in range(n):
    ss+=str(s[i])+" "
print(ss)
#masala ishlandi