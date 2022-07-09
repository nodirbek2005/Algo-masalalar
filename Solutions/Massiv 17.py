""" Bir o`lchamli sonli massiv tоk o`rindagi elеmеntlarini yigindisi
хisоblansin
"""
import math
n=int(input())
s=input().split(" ")
q=0
for i in range(n):
    s[i]=int(s[i])
for i in range(n):
    if (i-1)%2==1:
        q+=s[i]
print(q)
#masala ishlandi
