"""Sizga bir o’lchamli butun sonli massiv berilgan. Sizning vazifangiz unin
gmaskimal elementini va shunday elementlardan necha marta uchrag
aninitopuvchi dastur tuzishdan iborat. """
n=int(input())
s=input().split(" ")
d=[]
k=0
for i in range(n):
    s[i]=int(s[i])
    d.append(s[i])
d.sort()
d.reverse()
max=d[0]
for i in range(n):
    if s[i]==max:
        k+=1
print(max,k)
#masala ishlandi