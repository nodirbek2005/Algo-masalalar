"""Sizga bir o’lchmli.butun sonlardan iborat massiv berilgan. Sizning vazif
angizbu massiv elemntlarini modullari jihatdan kamaymaslik tartibida
saralaydigandastur tuzish.
Agar modul jihatdan teng musbat va manfiy sonlar mavjudbo’lsa manf
iy son oldinroq joylashtirilsin. """
import math
n=int(input())
s=input().split()
d=[]
for i in range(n):
    s[i]=int(s[i])
    d.append(s[i])
#masala ishlanmadi