a1,b1,d1=map(int,input().split(" "))
a=int(a1)
b=int(b1)
d=int(d1)
n=(a+b)/2
m=(d-a)/2
if n>m:
    print(int(n))
else:
    print(int(m))