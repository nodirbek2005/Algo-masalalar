""" Bir o`lchamli sonli massiv elementlarini qiymati [x,y] oraliqda
yotmaydigan elеmеntlari sоni aniqlansin"""
import math
n=int(input())
s=input().split(" ")
x1,y1=map(int,input().split(" "))
x=int(x1)
y=int(y1)
d=[]
for i in range(n):
    s[i]=int(s[i])
    if y<s[i]:
        d.append(s[i])
    elif x>s[i]:
        d.append(s[i])
print(len(d))
#masala ishlandi