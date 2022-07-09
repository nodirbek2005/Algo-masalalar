a1,b1=map(int,input().split(" "))
a=int(a1)
b=int(b1)
s=0
i=0
while a>=i and i<=b:
    i=i+1
    if i%2==0:
        s+=i
print(i)