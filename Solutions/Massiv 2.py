"""Bir o`lchamli sonli massiv [a,b] qismidagi elеmеntlari massivni eng
kichik elеmеntiga bo`lib chiqilsin qolganlari o’zgartirishsiz qoldirilsin. """
n=int(input())
s=input().split(" ")
a1,b1=map(int,input().split(" "))
a=int(a1)
b=int(b1)
d=[]
c=[]
for i in range(n):
    s[i]=int(s[i])
    d.append(s[i])
d.sort()
min=d[0]
for i in range(n):
    if i>=(a-1) and i<=(b-1):
        c.append((s[i]))
#masala ishlanmadi
