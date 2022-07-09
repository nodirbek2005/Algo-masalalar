""" Ikkita kamaymaslik tartibda saralangan massiv berilgan. Birinchi massiv
elementlari soni n ta, ikkinchi massiv elementlari soni m ta. Ularni
birlashtirib shunday n+m ta elementdan iborat massiv hosil qilingki bu
massiv yana kamaymaslik tartibda saralangan bo’lsin.
"""
x1,x2=map(int,input().split(" "))
n1=int(x1)
n2=int(x2)
s1=input().split(" ")
s2=input().split(" ")
for i in range(n1):
    s1[i]=int(s1[i])
for i in range(n2):
    s2[i]=int(s2[i])
s3=s1+s2
s3.sort()
ss=""
for i in range(len(s3)):
    ss+=str(s3[i])+" "
print(ss)
#masala ishlandi