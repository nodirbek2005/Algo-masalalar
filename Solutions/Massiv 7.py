"""Bir o`lchamli sonli massivni barcha elеmеntlari massivni eng katta
elеmеntiga bo`lib chiqilsin """
n=int(input())
s=input().split(" ")
d=[]
k=[]
for i in range(n):
    s[i]=int(s[i])
    d.append(s[i])
d.sort()
d.reverse()
min=d[0]
for i in range(n):
    k.append("%.2f"%(s[i]/min))
ss=""
for i in range(len(k)):
    ss+=str(k[i])+" "
print(ss)
#masala ishlandi