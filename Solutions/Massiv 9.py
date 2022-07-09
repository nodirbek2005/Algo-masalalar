""" Bir o`lchamli sonli massiv M dan kattta elеmеntlarini ko`paytmalarini
lоgarifmi хisоblansin """

import math
n=int(input())
s=input().split(" ")
m=int(input())
p=1
for i in range(n):
    s[i]=int(s[i])
    if s[i]>m:
        p*=s[i]
print("%.2f"%(math.log(p)))
#masala ishlandi