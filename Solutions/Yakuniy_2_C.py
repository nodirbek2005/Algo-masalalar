a1,b1=map(int,input().split(" "))
a=int(a1)
b=int(b1)
if a>b:
    a1=a+b
else:
    a1=a*b
if a<b:
    b1+=a
else:
    b1=a*b
print(a1,b1)
