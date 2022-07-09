""" Bir o`lchamli sonli massivni min elеmеntlari massivni охirgi elеmеnti bilan o`rin
almashtirilsin
"""
n=int(input())
s=input().split(" ")
d=[]
for i in range(n):
    s[i]=int(s[i])
    d.append(s[i])
d.sort()
min=d[0]
d.reverse()
oxr=d[0]
#masala ishlanmadi