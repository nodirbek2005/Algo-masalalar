import math
a1,b1,c1=map(int,input().split(" "))
a=int(a1)
b=int(b1)
c=int(c1)
m1=1/2*math.sqrt(2*b*b+2*c*c-a*a)
m2=1/2*math.sqrt(2*a*a+2*c*c-b*b)
m3=1/2*math.sqrt(2*a*a+2*b*b-c*c)
print("%.2f"%m1,"%.2f"%m2,"%.2f"%m3)
#masala ishlandi