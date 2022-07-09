import math
t1,s1=map(float,input().split(" "))
s=float(s1)
t=float(t1)
a1=1.2
b1=s
g1=(a1*a1+b1*b1)/(a1*a1+2*a1*b1+3*b1*b1+4)
a2=t
b2=s
g2=(a2*a2+b2*b2)/(a2*a2+2*a2*b2+3*b2*b2+4)
a3=2*s-1
b3=s*t
g3=(a3*a3+b3*b3)/(a3*a3+2*a3*b3+3*b3*b3+4)
g=g1+g2+g3
print("%.2f"%g)
