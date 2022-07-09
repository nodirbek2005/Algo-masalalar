tex=str(input())
a=str(input())
b=str(input())
c=[]
d=[]
for i in range(len(tex)):
    if tex[i]==a:
        c.append(i)
    if tex[i]==b:
        c.append(i)
for i in range(len(c)):
    c[i]=int(c[i])
f=int(c[0])
k=int(c[1])
for i in range(len(tex)):
    if i>(f) and i<(k):
        d.append(tex[i])
ss=""
for i in range(len(d)):
    ss+=str(d[i])
print(ss)