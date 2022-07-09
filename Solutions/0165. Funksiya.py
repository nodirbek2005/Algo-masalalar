import math
t1,s1=map(float,input().split(" "))
s=float(s1)
t=float(t1)
a1=t
b1=-2*s
c1=1.17
f1=(2*a1-b1-math.sin(c1))/(5+math.fabs(c1))
a2=2.2
b2=t
c2=s-t
f2=(2*a2-b2-math.sin(c2))/(5+math.fabs(c2))
f=f1+f2
print("%.2f"%f)